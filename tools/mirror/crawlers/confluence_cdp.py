"""Sync TDN conectando ao Chrome que VOCÊ já abriu (sessão real, sem novo Cloudflare)."""

from __future__ import annotations

import json
import logging
import re
import time
from pathlib import Path

from mirror.crawlers.confluence_api import _safe_filename
from mirror.crawlers import BaseCrawler, CrawlerConfig
from mirror.http_client import SyncStats
from mirror.knowledge import KnowledgeDoc, KnowledgeStore, html_to_markdown_body
from mirror.manifest import Manifest, ResourceRecord, content_hash, utc_now
from mirror.paths import KNOWLEDGE_DIR

logger = logging.getLogger(__name__)

CF_MARKERS = ("just a moment", "challenge-platform", "cf-browser-verification")


class ConfluenceCdpCrawler(BaseCrawler):
    """
    Conecta ao Chrome com remote debugging (porta 9222).
    Você passa o Cloudflare manualmente UMA VEZ no Chrome que abriu.
    """

    def run(self) -> SyncStats:
        try:
            from playwright.sync_api import sync_playwright
        except ImportError as exc:
            raise RuntimeError("Instale: ./tools/scripts/tdn/setup-tdn.sh") from exc

        cfg = self.cfg.config
        stats = SyncStats()
        base_url = cfg["base_url"].rstrip("/")
        cql = cfg.get("cql", "type=page AND space=fluig")
        rate = float(cfg.get("rate_limit_seconds", 0.5))
        page_limit = int(cfg.get("api_page_size", 50))
        cdp_url = cfg.get("cdp_url", "http://127.0.0.1:9222")

        data_dir = Path(self.cfg.data_dir)
        manifest = Manifest(data_dir / "manifest.db")
        output = data_dir / "mirror" / self.cfg.source_id
        output.mkdir(parents=True, exist_ok=True)
        product = cfg.get("product", "fluig")
        knowledge = KnowledgeStore(KNOWLEDGE_DIR)

        with sync_playwright() as p:
            try:
                browser = p.chromium.connect_over_cdp(cdp_url)
            except Exception as exc:
                raise RuntimeError(
                    f"Não conectou ao Chrome em {cdp_url}.\n\n"
                    "1. Feche o Chrome\n"
                    "2. Abra com:\n"
                    '   /Applications/Google\\ Chrome.app/Contents/MacOS/Google\\ Chrome \\\n'
                    '     --remote-debugging-port=9222 \\\n'
                    '     --user-data-dir="$HOME/.chrome-tdn"\n'
                    "3. Acesse tdn.totvs.com e passe o Cloudflare\n"
                    "4. Rode: .venv/bin/python tools/sync.py sync-tdn-cdp\n"
                ) from exc

            context = browser.contexts[0] if browser.contexts else browser.new_context()
            request = context.request

            pages = self._list_pages(request, base_url, cql, page_limit, rate)
            if not pages:
                raise RuntimeError("Nenhuma página encontrada. Verifique se está logado no TDN.")

            logger.info("%d páginas encontradas", len(pages))

            for page_meta in pages:
                page_id = page_meta["id"]
                title = page_meta.get("title", f"page-{page_id}")
                webui = page_meta.get("_links", {}).get("webui", "")
                url = f"{base_url}{webui}" if webui.startswith("/") else webui
                if not url.startswith("http"):
                    url = f"{base_url}/pages/viewpage.action?pageId={page_id}"

                api_url = f"{base_url}/rest/api/content/{page_id}?expand=body.storage,version"
                time.sleep(rate)

                try:
                    r = request.get(api_url, headers={"Accept": "application/json"})
                    text = r.text()
                    if _is_cf(text):
                        stats.errors += 1
                        continue
                    data = json.loads(text)
                except Exception as exc:
                    logger.warning("Erro %s: %s", title, exc)
                    stats.errors += 1
                    continue

                storage_html = data.get("body", {}).get("storage", {}).get("value", "")
                digest = content_hash(storage_html.encode("utf-8"))
                existing = manifest.get(url)
                safe_name = _safe_filename(url, page_id)
                dest = output / safe_name / "content.json"
                md_body = html_to_markdown_body(f"<div>{storage_html}</div>", main_selector="div")

                if not self.cfg.force and existing and existing.content_hash == digest:
                    stats.skipped += 1
                else:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    dest.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
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
                            extra={"page_id": page_id},
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

    def _list_pages(self, request, base_url, cql, limit, rate) -> list[dict]:
        pages: list[dict] = []
        start = 0
        while True:
            time.sleep(rate)
            r = request.get(
                f"{base_url}/rest/api/content/search",
                params={"cql": cql, "limit": limit, "start": start},
                headers={"Accept": "application/json"},
            )
            text = r.text()
            if _is_cf(text):
                raise RuntimeError("Cloudflare ativo — passe o desafio na janela do Chrome aberta.")
            data = json.loads(text)
            batch = data.get("results", [])
            if not batch:
                break
            pages.extend(batch)
            if len(batch) < limit:
                break
            start += limit
        return pages


def _is_cf(text: str) -> bool:
    lower = text.lower()
    return any(m in lower for m in CF_MARKERS)
