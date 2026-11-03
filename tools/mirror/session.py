"""Persistência de sessão TDN — perfil Chrome persistente + storage_state."""

from __future__ import annotations

import json
from pathlib import Path

import httpx

from mirror.paths import SECRETS_DIR

DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/131.0.0.0 Safari/537.36"
)

CF_MARKERS = (
    "just a moment",
    "challenge-platform",
    "cf-browser-verification",
    "um momento",
)

CONFLUENCE_MARKERS = ("wiki-content", "main-content", "title-heading")


def browser_profile_dir(data_dir: Path) -> Path:
    return SECRETS_DIR / ".tdn-browser-profile"


def session_path(data_dir: Path) -> Path:
    return SECRETS_DIR / "tdn-session.json"


def resolve_session_file(cfg: dict, data_dir: Path) -> Path:
    rel = cfg.get("session_file", "tdn-session.json")
    path = Path(rel)
    if not path.is_absolute():
        path = SECRETS_DIR / path.name
    return path


def save_playwright_state(context, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    context.storage_state(path=str(path))


def page_is_tdn_content(html: str) -> bool:
    lower = html.lower()
    if any(m in lower for m in CF_MARKERS):
        return False
    return any(m in lower for m in CONFLUENCE_MARKERS)


class PlaywrightTdnSession:
    """Reutiliza o perfil Chrome criado no auth-tdn."""

    def __init__(
        self,
        data_dir: Path,
        headless: bool = True,
        session_backup: Path | None = None,
    ) -> None:
        self.profile_dir = browser_profile_dir(data_dir)
        self.headless = headless
        self.session_backup = session_backup
        self._pw = None
        self.context = None

    def __enter__(self) -> "PlaywrightTdnSession":
        from playwright.sync_api import sync_playwright

        if not self.profile_dir.exists():
            raise FileNotFoundError(
                f"Perfil TDN não encontrado: {self.profile_dir}\n"
                "Execute: .venv/bin/python tools/sync.py auth-tdn"
            )

        self._pw = sync_playwright().start()
        launch_kwargs: dict = {
            "headless": self.headless,
            "locale": "pt-BR",
            "viewport": {"width": 1440, "height": 900},
            "user_agent": DEFAULT_USER_AGENT,
            "ignore_default_args": ["--enable-automation"],
            "args": ["--disable-blink-features=AutomationControlled"],
        }

        try:
            self.context = self._pw.chromium.launch_persistent_context(
                str(self.profile_dir),
                channel="chrome",
                **launch_kwargs,
            )
        except Exception:
            self.context = self._pw.chromium.launch_persistent_context(
                str(self.profile_dir),
                **launch_kwargs,
            )

        if self.session_backup and self.session_backup.exists():
            try:
                state = json.loads(self.session_backup.read_text(encoding="utf-8"))
                self.context.add_cookies(state.get("cookies", []))
            except Exception:
                pass

        return self

    def __exit__(self, *args) -> None:
        if self.context:
            self.context.close()
        if self._pw:
            self._pw.stop()

    def get(self, url: str, params: dict | None = None):
        return self.context.request.get(
            url,
            params=params,
            headers={"Accept": "application/json, text/html"},
        )

    def is_valid(self, test_url: str) -> bool:
        try:
            r = self.get(test_url)
            return page_is_tdn_content(r.text())
        except Exception:
            return False

    def get_json(self, url: str, params: dict | None = None) -> dict:
        r = self.get(url, params=params)
        text = r.text()
        if _is_cloudflare(text):
            raise RuntimeError(
                "Cloudflare bloqueou. Renove a sessão:\n"
                "  .venv/bin/python tools/sync.py auth-tdn"
            )
        if r.status >= 400:
            raise RuntimeError(f"HTTP {r.status}: {text[:200]}")
        try:
            return json.loads(text)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"Resposta não é JSON: {text[:200]}") from exc


def _is_cloudflare(text: str) -> bool:
    lower = text.lower()
    return any(m in lower for m in CF_MARKERS)


def test_api_access(context, base_url: str = "https://tdn.totvs.com") -> tuple[bool, str]:
    """Valida se a API REST responde após autenticação."""
    try:
        r = context.request.get(
            f"{base_url}/rest/api/content/search",
            params={"cql": "type=page", "limit": 1},
            headers={"Accept": "application/json"},
        )
        text = r.text()
        if _is_cloudflare(text):
            return False, "Cloudflare ainda ativo — aguarde a página carregar completamente"
        if r.status >= 400:
            return False, f"API retornou HTTP {r.status}"
        data = json.loads(text)
        if "results" in data:
            return True, f"OK — API acessível ({len(data['results'])} resultado de teste)"
        return False, "Resposta da API inesperada"
    except Exception as exc:
        return False, str(exc)
