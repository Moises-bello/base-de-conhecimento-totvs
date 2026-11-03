"""Importa export JSON gerado pelo script do console do browser."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse

from mirror.catalog import classify_discontinued, is_blocklisted_url, load_blocklist, update_blocklist
from mirror.knowledge import KnowledgeDoc, KnowledgeStore, html_to_markdown_body
from mirror.manifest import Manifest, ResourceRecord, content_hash, utc_now
from mirror.paths import KNOWLEDGE_DIR


def import_tdn_pages(
    pages: list[dict],
    data_dir: Path,
    source_id: str = "tdn-fluig",
    product: str = "fluig",
    force: bool = False,
) -> tuple[int, int]:
    """Importa lista de páginas Confluence. Retorna (baixados, ignorados)."""
    if not pages:
        return 0, 0

    manifest = Manifest(data_dir / "manifest.db")
    output = data_dir / "mirror" / source_id
    knowledge = KnowledgeStore(KNOWLEDGE_DIR)
    blocklist = load_blocklist(KNOWLEDGE_DIR)
    downloaded = skipped = 0

    for data in pages:
        page_id = str(data.get("id", ""))
        title = data.get("title", f"page-{page_id}")
        links = data.get("_links", {})
        webui = links.get("webui", "")
        base = links.get("base", "https://tdn.totvs.com")
        url = f"{base.rstrip('/')}{webui}" if webui.startswith("/") else webui
        if not url.startswith("http"):
            url = f"https://tdn.totvs.com/pages/viewpage.action?pageId={page_id}"

        if is_blocklisted_url(url, blocklist):
            skipped += 1
            continue

        storage_html = data.get("body", {}).get("storage", {}).get("value", "")
        md_body = html_to_markdown_body(f"<div>{storage_html}</div>", main_selector="div")
        if classify_discontinued(title, md_body[:2000], aggressive=True, scan_body=True):
            update_blocklist(
                KNOWLEDGE_DIR,
                [
                    {
                        "path": "",
                        "url": url,
                        "title": title,
                        "product": product,
                        "source": source_id,
                        "removal_reason": "descontinuado-import",
                    }
                ],
            )
            skipped += 1
            continue

        digest = content_hash(storage_html.encode("utf-8"))
        existing = manifest.get(url)
        safe_name = _safe_filename(url, page_id)
        dest = output / safe_name / "content.json"
        version = data.get("version", {}).get("number", 1)

        if not force and existing and existing.content_hash == digest:
            skipped += 1
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
            knowledge.write(
                f"{source_id}/{safe_name}",
                KnowledgeDoc(
                    title=title,
                    source=source_id,
                    product=product,
                    url=url,
                    body=md_body,
                    doc_type="documentation",
                    content_hash=digest,
                    extra={"page_id": page_id, "version": version},
                ),
            )
            downloaded += 1

        manifest.upsert(
            ResourceRecord(
                url=url,
                source_id=source_id,
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
    return downloaded, skipped


def import_tdn_export(
    export_path: Path,
    data_dir: Path,
    source_id: str = "tdn-fluig",
    product: str = "fluig",
    force: bool = False,
) -> tuple[int, int]:
    """Retorna (baixados, ignorados)."""
    raw = json.loads(export_path.read_text(encoding="utf-8"))
    pages = raw.get("pages", [])
    skipped_meta = raw.get("skipped", [])
    if not pages:
        raise ValueError("Arquivo sem páginas.")

    if skipped_meta:
        print(f"  ({len(skipped_meta)} páginas ignoradas no export por 403/erro)")

    return import_tdn_pages(pages, data_dir, source_id, product, force)


def import_tdn_directory(
    dir_path: Path,
    data_dir: Path,
    source_id: str = "tdn-fluig",
    product: str = "fluig",
    force: bool = False,
) -> tuple[int, int]:
    """Importa todos tdn-chunk-*.json de uma pasta."""
    chunks = sorted(dir_path.glob("tdn-chunk-*.json"))
    if not chunks:
        chunks = sorted(dir_path.glob("*.json"))
    if not chunks:
        raise ValueError(f"Nenhum JSON em {dir_path}")

    total_dl = total_skip = 0
    for chunk in chunks:
        raw = json.loads(chunk.read_text(encoding="utf-8"))
        pages = raw.get("pages", [])
        dl, skip = import_tdn_pages(pages, data_dir, source_id, product, force)
        total_dl += dl
        total_skip += skip
        print(f"  {chunk.name}: {dl} novos, {skip} ignorados")

    return total_dl, total_skip


def _safe_filename(url: str, page_id: str) -> str:
    parsed = urlparse(url)
    path = parsed.path.strip("/").replace("/", "_")
    if parsed.query:
        q = re.sub(r"[^\w.-]", "_", parsed.query)[:60]
        path = f"{path}__{q}"
    return path or f"page-{page_id}"
