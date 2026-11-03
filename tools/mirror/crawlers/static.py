from __future__ import annotations

import json
import re
from collections import deque
from pathlib import Path
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from mirror.crawlers import BaseCrawler, CrawlerConfig
from mirror.http_client import HttpFetcher, SyncStats
from mirror.knowledge import (
    KnowledgeDoc,
    KnowledgeStore,
    html_to_markdown_body,
    knowledge_rel_path,
    should_export_markdown,
)
from mirror.manifest import Manifest
from mirror.paths import KNOWLEDGE_DIR


ASSET_PATTERN = re.compile(
    r"""['"]([/\w][^'"]*\.(?:js|css|json|html?|map|png|svg|woff2?|ttf|ico))['"]""",
    re.IGNORECASE,
)


class StaticCrawler(BaseCrawler):
    """Crawler BFS para sites estáticos (api.fluig.com, style.fluig.com)."""

    def run(self) -> SyncStats:
        cfg = self.cfg.config
        stats = SyncStats()
        manifest = Manifest(Path(self.cfg.data_dir) / "manifest.db")
        output = str(Path(self.cfg.data_dir) / "mirror" / self.cfg.source_id)
        product = cfg.get("product", "fluig")
        export_md = cfg.get("export_markdown", True)
        knowledge = KnowledgeStore(KNOWLEDGE_DIR) if export_md else None
        fetcher = HttpFetcher(
            manifest=manifest,
            source_id=self.cfg.source_id,
            output_dir=output,
            rate_limit=float(cfg.get("rate_limit_seconds", 0.5)),
        )

        base_url = cfg["base_url"]
        allowed_hosts = set(cfg.get("allowed_hosts", []))
        extra_hosts = set(cfg.get("extra_hosts", []))
        max_depth = int(cfg.get("max_depth", 8))
        all_hosts = allowed_hosts | extra_hosts

        visited: set[str] = set()
        queue: deque[tuple[str, int]] = deque([(base_url, 0)])

        try:
            while queue:
                url, depth = queue.popleft()
                if url in visited:
                    continue
                visited.add(url)

                result = fetcher.fetch(url, force=self.cfg.force)
                if result.action == "downloaded":
                    stats.downloaded += 1
                elif result.action == "skipped":
                    stats.skipped += 1
                else:
                    stats.errors += 1
                    continue

                if depth >= max_depth:
                    continue

                parsed = urlparse(url)
                if parsed.netloc not in all_hosts:
                    continue

                # Descobre links a partir do conteúdo salvo
                record = manifest.get(url)
                if not record:
                    continue
                content_path = Path(record.file_path)
                if not content_path.exists():
                    continue

                raw = content_path.read_bytes()
                content_type = _guess_type(url)

                new_urls: set[str] = set()
                if content_type in ("html", "unknown"):
                    new_urls |= _extract_html_links(raw, url, all_hosts)
                if content_type in ("js", "html", "unknown"):
                    new_urls |= _extract_js_assets(raw, url, all_hosts)

                if knowledge and content_type == "html" and should_export_markdown(url):
                    _export_html_to_knowledge(
                        knowledge, raw, url, self.cfg.source_id, product
                    )

                for link in sorted(new_urls):
                    if link not in visited:
                        queue.append((link, depth + 1))
        finally:
            fetcher.close()
            if knowledge:
                knowledge.save_index()
            manifest.close()

        return stats


def _export_html_to_knowledge(
    store: KnowledgeStore,
    raw: bytes,
    url: str,
    source_id: str,
    product: str,
) -> None:
    from urllib.parse import urlparse

    from mirror.manifest import content_hash

    html = raw.decode("utf-8", errors="replace")
    soup = BeautifulSoup(html, "html.parser")
    title_tag = soup.find("title")
    title = title_tag.get_text(strip=True) if title_tag else urlparse(url).path

    body = html_to_markdown_body(html, main_selector=".fluig-style-guide")
    rel = knowledge_rel_path(source_id, url)

    store.write(
        rel,
        KnowledgeDoc(
            title=title,
            source=source_id,
            product=product,
            url=url,
            body=body,
            doc_type="documentation",
            content_hash=content_hash(raw),
        ),
    )


def _guess_type(url: str) -> str:
    path = urlparse(url).path.lower()
    if path.endswith((".html", ".htm")):
        return "html"
    if path.endswith(".js"):
        return "js"
    if path.endswith(".css"):
        return "css"
    return "unknown"


def _extract_html_links(
    raw: bytes, base_url: str, allowed_hosts: set[str]
) -> set[str]:
    links: set[str] = set()
    try:
        soup = BeautifulSoup(raw, "html.parser")
    except Exception:
        return links

    for tag in soup.find_all(["a", "link", "script", "img", "source"]):
        attr = "href" if tag.name in ("a", "link") else "src"
        href = tag.get(attr)
        if not href or href.startswith(("#", "mailto:", "javascript:")):
            continue
        absolute = urljoin(base_url, href)
        parsed = urlparse(absolute)
        if parsed.scheme not in ("http", "https"):
            continue
        if parsed.netloc not in allowed_hosts:
            continue
        clean = absolute.split("#")[0]
        if clean:
            links.add(clean)
    return links


def _extract_js_assets(
    raw: bytes, base_url: str, allowed_hosts: set[str]
) -> set[str]:
    links: set[str] = set()
    try:
        text = raw.decode("utf-8", errors="ignore")
    except Exception:
        return links

    for match in ASSET_PATTERN.finditer(text):
        ref = match.group(1)
        absolute = urljoin(base_url, ref)
        parsed = urlparse(absolute)
        if parsed.netloc in allowed_hosts:
            links.add(absolute.split("#")[0])
    return links
