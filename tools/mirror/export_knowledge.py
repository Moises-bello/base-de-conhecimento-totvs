"""Reexporta HTML/JSON do espelho raw para a camada knowledge/ em Markdown."""

from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from mirror.knowledge import (
    KnowledgeDoc,
    KnowledgeStore,
    html_to_markdown_body,
    knowledge_rel_path,
    should_export_markdown,
)
from mirror.catalog import is_blocklisted_url, load_blocklist
from mirror.manifest import Manifest
from mirror.zendesk import zendesk_article_rel_path, zendesk_article_to_markdown
from mirror.paths import KNOWLEDGE_DIR


def export_from_mirror(data_dir: Path, config: dict) -> int:
    """Regenera knowledge/ a partir de .cache/mirror/ existente."""
    from mirror.export_api import export_api_fluig

    manifest = Manifest(data_dir / "manifest.db")
    knowledge = KnowledgeStore(KNOWLEDGE_DIR)
    blocklist = load_blocklist(KNOWLEDGE_DIR)
    sources = config.get("sources", {})
    count = 0

    for record in manifest.iter_all():
        if is_blocklisted_url(record.url, blocklist):
            continue
        source_cfg = sources.get(record.source_id, {})
        if not source_cfg.get("export_markdown", True):
            continue

        product = source_cfg.get("product", "fluig")
        file_path = _resolve_file_path(data_dir, record)
        if not file_path or not file_path.exists():
            continue

        if (
            source_cfg.get("type") == "confluence-api"
            and file_path.name == "content.json"
        ):
            data = json.loads(file_path.read_text(encoding="utf-8"))
            title = data.get("title", record.url)
            storage_html = data.get("body", {}).get("storage", {}).get("value", "")
            md_body = html_to_markdown_body(f"<div>{storage_html}</div>", main_selector="div")
            page_id = data.get("id", "")
            rel = f"{record.source_id}/{file_path.parent.name}"
            knowledge.write(
                rel,
                KnowledgeDoc(
                    title=title,
                    source=record.source_id,
                    product=product,
                    url=record.url,
                    body=md_body,
                    doc_type="documentation",
                    content_hash=record.content_hash,
                    extra={"page_id": page_id},
                ),
            )
            count += 1
            continue

        if source_cfg.get("type") == "zendesk" and file_path.suffix == ".json":
            if "/articles/" not in record.url:
                continue
            payload = json.loads(file_path.read_text(encoding="utf-8"))
            article = payload.get("article", payload)
            if not article.get("body"):
                continue
            title, body = zendesk_article_to_markdown(article)
            section_name = str(article.get("section_id", "geral"))
            rel = zendesk_article_rel_path(record.source_id, article, section_name)
            knowledge.write(
                rel,
                KnowledgeDoc(
                    title=title,
                    source=record.source_id,
                    product=product,
                    url=record.url,
                    body=body,
                    doc_type="support-article",
                    category=section_name,
                    content_hash=record.content_hash,
                    extra={
                        "article_id": article.get("id"),
                        "section_id": article.get("section_id"),
                        "updated_at": article.get("updated_at"),
                    },
                ),
            )
            count += 1
            continue

        if should_export_markdown(record.url) and file_path.suffix in (".html", ".htm"):
            raw = file_path.read_bytes()
            html = raw.decode("utf-8", errors="replace")
            soup = BeautifulSoup(html, "html.parser")
            title_tag = soup.find("title")
            title = title_tag.get_text(strip=True) if title_tag else record.url
            body = html_to_markdown_body(
                html,
                main_selector=".fluig-style-guide" if record.source_id == "style-guide" else None,
            )
            rel = knowledge_rel_path(record.source_id, record.url)
            knowledge.write(
                rel,
                KnowledgeDoc(
                    title=title,
                    source=record.source_id,
                    product=product,
                    url=record.url,
                    body=body,
                    doc_type="documentation",
                    content_hash=record.content_hash,
                ),
            )
            count += 1

    knowledge.save_index()
    manifest.close()

    api_cfg = sources.get("api-fluig", {})
    if api_cfg.get("enabled", True):
        count += export_api_fluig(data_dir)

    knowledge.rebuild_index_from_disk()
    return count


def _resolve_file_path(data_dir: Path, record) -> Path | None:
    path = Path(record.file_path)
    if path.exists():
        return path
    marker = "/mirror/"
    if marker in record.file_path:
        rel = record.file_path.split(marker, 1)[1]
        candidate = data_dir / "mirror" / rel
        if candidate.exists():
            return candidate
    return None
