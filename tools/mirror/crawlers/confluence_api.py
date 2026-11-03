"""Crawler TDN via API REST — usa sessão Playwright (mesmo Chrome do auth-tdn)."""

from __future__ import annotations

import json
import logging
import re
import time
from pathlib import Path

from mirror.crawlers import BaseCrawler, CrawlerConfig
from mirror.http_client import SyncStats
from mirror.knowledge import KnowledgeDoc, KnowledgeStore, html_to_markdown_body
from mirror.manifest import Manifest, ResourceRecord, content_hash, utc_now
from mirror.paths import KNOWLEDGE_DIR
from mirror.session import (
    PlaywrightTdnSession,
    browser_profile_dir,
    resolve_session_file,
    save_playwright_state,
    session_path,
    test_api_access,
)

logger = logging.getLogger(__name__)

CF_MARKERS = ("just a moment", "challenge-platform", "cf-browser-verification")


class ConfluenceApiCrawler(BaseCrawler):
    """
    Baixa páginas do TDN pela API REST do Confluence.
    Requer: python tools/sync.py auth-tdn (uma vez)
    """

    def run(self) -> SyncStats:
        cfg = self.cfg.config
        stats = SyncStats()
        base_url = cfg["base_url"].rstrip("/")
        cql = cfg.get("cql", "type=page AND space=fluig")
        rate = float(cfg.get("rate_limit_seconds", 0.5))
        page_limit = int(cfg.get("api_page_size", 50))
        test_url = cfg.get(
            "session_test_url",
            f"{base_url}/display/public/fluig/Central+de+ajuda",
        )

        data_dir = Path(self.cfg.data_dir)
        manifest = Manifest(data_dir / "manifest.db")
        output = data_dir / "mirror" / self.cfg.source_id
        output.mkdir(parents=True, exist_ok=True)
        product = cfg.get("product", "fluig")
        knowledge = KnowledgeStore(KNOWLEDGE_DIR)
        session_file = resolve_session_file(cfg, data_dir)

        with PlaywrightTdnSession(
            data_dir,
            headless=True,
            session_backup=session_file if session_file.exists() else None,
        ) as session:
            if not session.is_valid(test_url):
                raise RuntimeError(
                    "Sessão TDN inválida ou expirada.\n"
                    "Execute novamente:\n"
                    "  .venv/bin/python tools/sync.py auth-tdn"
                )

            pages = self._list_all_pages(session, base_url, cql, page_limit, rate)
            if not pages:
                pages = self._discover_pages(session, base_url, cfg, page_limit, rate)
            logger.info("Encontradas %d páginas via API", len(pages))

            if not pages:
                raise RuntimeError(
                    "Nenhuma página encontrada. Ajuste 'cql' em tools/config/sources.yaml"
                )

            for page_meta in pages:
                page_id = page_meta["id"]
                title = page_meta.get("title", f"page-{page_id}")
                webui = page_meta.get("_links", {}).get("webui", "")
                url = f"{base_url}{webui}" if webui.startswith("/") else webui
                if not url.startswith("http"):
                    url = f"{base_url}/pages/viewpage.action?pageId={page_id}"

                api_url = (
                    f"{base_url}/rest/api/content/{page_id}"
                    "?expand=body.storage,version"
                )
                time.sleep(rate)

                try:
                    data = session.get_json(api_url)
                except Exception as exc:
                    logger.warning("Erro ao baixar %s: %s", title, exc)
                    stats.errors += 1
                    continue

                storage_html = (
                    data.get("body", {}).get("storage", {}).get("value", "")
                )
                version = data.get("version", {}).get("number", 1)
                digest = content_hash(storage_html.encode("utf-8"))
                existing = manifest.get(url)
                safe_name = _safe_filename(url, page_id)
                dest = output / safe_name / "content.json"
                md_body = html_to_markdown_body(
                    f"<div>{storage_html}</div>",
                    main_selector="div",
                )

                if not self.cfg.force and existing and existing.content_hash == digest:
                    stats.skipped += 1
                else:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_text(
                        json.dumps(data, ensure_ascii=False, indent=2),
                        encoding="utf-8",
                    )
                    knowledge.write(
                        f"{self.cfg.source_id}/{safe_name}",
                        KnowledgeDoc(
                            title=title,
                            source=self.cfg.source_id,
                            product=product,
                            url=url,
                            body=md_body,
                            doc_type="documentation",
                            content_hash=digest,
                            extra={"page_id": page_id, "version": version},
                        ),
                    )
                    stats.downloaded += 1
                    logger.info("Baixado: %s", title)

                manifest.upsert(
                    ResourceRecord(
                        url=url,
                        source_id=self.cfg.source_id,
                        file_path=str(dest),
                        content_hash=digest,
                        etag=None,
                        last_modified=None,
                        content_length=len(storage_html),
                        status_code=200,
                        fetched_at=utc_now(),
                    )
                )

        knowledge.save_index()
        manifest.close()
        return stats

    def _list_all_pages(
        self,
        session: PlaywrightTdnSession,
        base_url: str,
        cql: str,
        limit: int,
        rate: float,
    ) -> list[dict]:
        pages: list[dict] = []
        start = 0

        while True:
            time.sleep(rate)
            data = session.get_json(
                f"{base_url}/rest/api/content/search",
                params={"cql": cql, "limit": limit, "start": start, "expand": "version"},
            )
            batch = data.get("results", [])
            if not batch:
                break
            pages.extend(batch)
            if len(batch) < limit:
                break
            start += limit

        return pages

    def _discover_pages(
        self,
        session: PlaywrightTdnSession,
        base_url: str,
        cfg: dict,
        limit: int,
        rate: float,
    ) -> list[dict]:
        fallbacks = cfg.get(
            "cql_fallbacks",
            [
                "type=page AND text ~ \"fluig\"",
                "type=page AND title ~ \"Fluig\"",
            ],
        )
        for cql in fallbacks:
            logger.info("Tentando CQL alternativo: %s", cql)
            pages = self._list_all_pages(session, base_url, cql, limit, rate)
            if pages:
                return pages

        for title in ("Central de ajuda", "Central de Ajuda", "Fluig"):
            time.sleep(rate)
            try:
                data = session.get_json(
                    f"{base_url}/rest/api/content",
                    params={"title": title, "expand": "children.page", "limit": 5},
                )
            except Exception:
                continue
            results = data.get("results", [])
            if not results:
                continue
            root_id = results[0]["id"]
            pages = self._list_all_pages(
                session, base_url, f"type=page AND ancestor={root_id}", limit, rate
            )
            if pages:
                return pages

        return []


def _safe_filename(url: str, page_id: str) -> str:
    from urllib.parse import urlparse

    parsed = urlparse(url)
    path = parsed.path.strip("/").replace("/", "_")
    if parsed.query:
        q = re.sub(r"[^\w.-]", "_", parsed.query)[:60]
        path = f"{path}__{q}"
    return path or f"page-{page_id}"
