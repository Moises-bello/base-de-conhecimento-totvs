from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml
from bs4 import BeautifulSoup

from mirror.paths import INDEX_PATH

SKIP_EXTENSIONS = {
    ".css", ".js", ".map", ".png", ".jpg", ".jpeg", ".gif", ".svg",
    ".ico", ".woff", ".woff2", ".ttf", ".eot", ".mp4", ".webm", ".json",
}


@dataclass
class KnowledgeDoc:
    title: str
    source: str
    product: str
    url: str
    body: str
    doc_type: str = "documentation"
    category: str = ""
    content_hash: str = ""
    extra: dict[str, Any] = field(default_factory=dict)


class KnowledgeStore:
    """Grava documentos em Markdown com frontmatter YAML para uso com IA/RAG."""

    def __init__(self, base_dir: Path) -> None:
        self.base_dir = base_dir
        self.base_dir.mkdir(parents=True, exist_ok=True)
        self._index: list[dict[str, Any]] = []

    def write(self, rel_path: str, doc: KnowledgeDoc) -> Path:
        """Salva em knowledge/{product}/{rel_path}.md"""
        rel = rel_path.strip("/")
        if not rel.endswith(".md"):
            rel = f"{rel}.md"

        dest = self.base_dir / doc.product / rel
        dest.parent.mkdir(parents=True, exist_ok=True)

        frontmatter = {
            "title": doc.title,
            "source": doc.source,
            "product": doc.product,
            "type": doc.doc_type,
            "url": doc.url,
            "fetched_at": datetime.now(timezone.utc).isoformat(),
        }
        if doc.category:
            frontmatter["category"] = doc.category
        if doc.content_hash:
            frontmatter["content_hash"] = doc.content_hash
        frontmatter.update(doc.extra)

        yaml_block = yaml.dump(
            frontmatter, allow_unicode=True, default_flow_style=False
        ).strip()
        content = f"---\n{yaml_block}\n---\n\n{doc.body.strip()}\n"
        dest.write_text(content, encoding="utf-8")

        self._index.append(
            {
                "path": str(dest.relative_to(self.base_dir)),
                "title": doc.title,
                "source": doc.source,
                "product": doc.product,
                "type": doc.doc_type,
                "url": doc.url,
                "category": doc.category,
            }
        )
        return dest

    def save_index(self) -> Path:
        index_path = INDEX_PATH
        index_path.parent.mkdir(parents=True, exist_ok=True)
        if index_path.exists():
            existing = json.loads(index_path.read_text(encoding="utf-8"))
        else:
            existing = []

        by_path = {item["path"]: item for item in existing}
        for item in self._index:
            by_path[item["path"]] = item

        merged = sorted(by_path.values(), key=lambda x: x["path"])
        index_path.write_text(
            json.dumps(merged, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        return index_path

    def rebuild_index_from_disk(self) -> Path:
        """Reconstrói index.json lendo frontmatter de todos os .md."""
        entries: list[dict[str, Any]] = []
        for md_path in sorted(self.base_dir.rglob("*.md")):
            rel = str(md_path.relative_to(self.base_dir))
            if Path(rel).name.startswith("_INDEX"):
                continue
            meta = _read_frontmatter(md_path)
            entries.append(
                {
                    "path": rel,
                    "title": meta.get("title", rel),
                    "source": meta.get("source", ""),
                    "product": meta.get("product", ""),
                    "type": meta.get("type", ""),
                    "url": meta.get("url", ""),
                    "category": meta.get("category", ""),
                    "table": meta.get("table", ""),
                    "keywords": meta.get("keywords", ""),
                }
            )
        index_path = INDEX_PATH
        index_path.parent.mkdir(parents=True, exist_ok=True)
        index_path.write_text(
            json.dumps(entries, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        return index_path


def _read_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {}


def should_export_markdown(url: str) -> bool:
    path = url.split("?")[0].lower()
    if any(path.endswith(ext) for ext in SKIP_EXTENSIONS):
        return False
    return path.endswith((".html", ".htm")) or path.endswith("/")


def html_to_markdown_body(html: str, main_selector: str | None = None) -> str:
    try:
        from markdownify import markdownify
    except ImportError:
        return _fallback_text(html)

    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style", "nav", "header", "footer", "noscript"]):
        tag.decompose()

    if main_selector:
        main = soup.select_one(main_selector)
    else:
        main = (
            soup.select_one("#main-content")
            or soup.select_one(".wiki-content")
            or soup.select_one(".fluig-style-guide")
            or soup.select_one("main")
            or soup.select_one('[role="main"]')
            or soup.body
        )

    target = main or soup
    try:
        return markdownify(str(target), heading_style="ATX").strip()
    except RecursionError:
        return _fallback_text(str(target))
    except Exception:
        return _fallback_text(str(target))


def _fallback_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose()
    return soup.get_text("\n", strip=True)


def slugify(text: str, max_len: int = 80) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"[\s_-]+", "-", text)
    return text[:max_len].strip("-") or "documento"


def knowledge_rel_path(source_id: str, url: str) -> str:
    """Caminho relativo estável para knowledge/{product}/{source}/{slug}.md"""
    from urllib.parse import urlparse

    path = urlparse(url).path.strip("/") or "index"
    if path.endswith(".html"):
        path = path[:-5]
    slug = slugify(path.replace("/", "-") or "index")
    return f"{source_id}/{slug}"
