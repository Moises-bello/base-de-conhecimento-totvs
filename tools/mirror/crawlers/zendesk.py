from __future__ import annotations

import json
import time
from collections import defaultdict, deque
from pathlib import Path

import httpx

from mirror.catalog import classify_discontinued, is_blocklisted_url
from mirror.crawlers import BaseCrawler
from mirror.http_client import SyncStats
from mirror.knowledge import KnowledgeDoc, KnowledgeStore
from mirror.manifest import Manifest, ResourceRecord, content_hash, utc_now
from mirror.zendesk import zendesk_article_rel_path, zendesk_article_to_markdown
from mirror.paths import KNOWLEDGE_DIR


class ZendeskCrawler(BaseCrawler):
    """Baixa artigos da Central de Atendimento TOTVS (Zendesk Help Center)."""

    def run(self) -> SyncStats:
        cfg = self.cfg.config
        stats = SyncStats()
        rate = float(cfg.get("rate_limit_seconds", 0.5))
        category_id = cfg.get("category_id")
        root_section_id = cfg.get("root_section_id")
        locale = cfg.get("locale", "pt-br")
        base_url = cfg.get("base_url", "https://centraldeatendimento.totvs.com").rstrip("/")
        api_base = cfg.get(
            "api_base",
            f"{base_url}/api/v2/help_center/{locale}",
        ).rstrip("/")
        product = cfg.get("product", "totvs")
        include_descendants = cfg.get("include_descendants", True)
        extra_roots = [int(x) for x in cfg.get("extra_root_section_ids", [])]

        data_dir = Path(self.cfg.data_dir)
        manifest = Manifest(data_dir / "manifest.db")
        output = data_dir / "mirror" / self.cfg.source_id
        output.mkdir(parents=True, exist_ok=True)
        knowledge = KnowledgeStore(KNOWLEDGE_DIR)
        blocklist_path = KNOWLEDGE_DIR
        from mirror.catalog import load_blocklist

        blocklist = load_blocklist(blocklist_path)

        client = httpx.Client(
            timeout=120.0,
            follow_redirects=True,
            headers={"User-Agent": "TotvsKnowledgeMirror/1.0 (+local backup)"},
        )

        try:
            sections = _load_all_sections(client, api_base, output, rate)
            section_by_id = {s["id"]: s for s in sections}

            if category_id:
                section_ids = _collect_section_ids_from_category(
                    sections,
                    int(category_id),
                    include_descendants,
                )
            elif root_section_id:
                section_ids = _collect_section_ids(
                    sections,
                    int(root_section_id),
                    include_descendants,
                    extra_roots,
                )
            else:
                raise ValueError(
                    f"{self.cfg.source_id}: informe root_section_id ou category_id"
                )

            seen_articles: set[int] = set()

            for section_id in section_ids:
                section = section_by_id.get(section_id, {})
                section_name = section.get("name", str(section_id))

                for article in _iter_section_articles(client, api_base, section_id, rate):
                    article_id = article["id"]
                    if article_id in seen_articles:
                        continue
                    seen_articles.add(article_id)

                    changed = _save_article(
                        manifest=manifest,
                        knowledge=knowledge,
                        blocklist=blocklist,
                        source_id=self.cfg.source_id,
                        product=product,
                        output=output,
                        section_name=section_name,
                        article=article,
                        force=self.cfg.force,
                        stats=stats,
                    )
                    if not changed:
                        continue

        finally:
            client.close()
            knowledge.save_index()
            manifest.close()

        return stats


def _load_all_sections(
    client: httpx.Client,
    api_base: str,
    output: Path,
    rate: float,
) -> list[dict]:
    cache_path = output / "_sections_cache.json"
    if cache_path.exists():
        cached = json.loads(cache_path.read_text(encoding="utf-8"))
        age_hours = (time.time() - cache_path.stat().st_mtime) / 3600
        if age_hours < 24 and cached.get("sections"):
            return cached["sections"]

    sections: list[dict] = []
    page = 1
    while True:
        time.sleep(rate)
        response = client.get(f"{api_base}/sections.json?per_page=100&page={page}")
        response.raise_for_status()
        data = response.json()
        sections.extend(data.get("sections", []))
        if not data.get("next_page"):
            break
        page += 1

    cache_path.write_text(
        json.dumps({"sections": sections}, ensure_ascii=False),
        encoding="utf-8",
    )
    return sections


def _collect_section_ids(
    sections: list[dict],
    root_section_id: int,
    include_descendants: bool,
    extra_roots: list[int],
) -> list[int]:
    by_parent: dict[int | None, list[dict]] = defaultdict(list)
    for section in sections:
        by_parent[section.get("parent_section_id")].append(section)

    roots = [root_section_id, *extra_roots]
    result: list[int] = []
    seen: set[int] = set()

    for root in roots:
        if root in seen:
            continue
        seen.add(root)
        result.append(root)

        if not include_descendants:
            continue

        queue: deque[int] = deque([root])
        while queue:
            parent_id = queue.popleft()
            for child in by_parent.get(parent_id, []):
                child_id = child["id"]
                if child_id in seen:
                    continue
                seen.add(child_id)
                result.append(child_id)
                queue.append(child_id)

    return result


def _collect_section_ids_from_category(
    sections: list[dict],
    category_id: int,
    include_descendants: bool,
) -> list[int]:
    by_parent: dict[int | None, list[dict]] = defaultdict(list)
    for section in sections:
        by_parent[section.get("parent_section_id")].append(section)

    category_sections = [s for s in sections if s.get("category_id") == category_id]
    result: list[int] = []
    seen: set[int] = set()

    for section in category_sections:
        root_id = section["id"]
        if root_id in seen:
            continue
        seen.add(root_id)
        result.append(root_id)

        if not include_descendants:
            continue

        queue: deque[int] = deque([root_id])
        while queue:
            parent_id = queue.popleft()
            for child in by_parent.get(parent_id, []):
                child_id = child["id"]
                if child_id in seen:
                    continue
                seen.add(child_id)
                result.append(child_id)
                queue.append(child_id)

    return result


def _iter_section_articles(
    client: httpx.Client,
    api_base: str,
    section_id: int,
    rate: float,
):
    page = 1
    while True:
        time.sleep(rate)
        response = client.get(
            f"{api_base}/sections/{section_id}/articles.json?per_page=100&page={page}"
        )
        if response.status_code == 404:
            return
        response.raise_for_status()
        data = response.json()
        for article in data.get("articles", []):
            yield article
        if not data.get("next_page"):
            break
        page += 1


def _relative_path(article: dict) -> Path:
    article_id = article.get("id", 0)
    return Path("articles") / f"{article_id}.json"


def _save_article(
    manifest: Manifest,
    knowledge: KnowledgeStore,
    blocklist: dict,
    source_id: str,
    product: str,
    output: Path,
    section_name: str,
    article: dict,
    force: bool,
    stats: SyncStats,
) -> bool:
    url = article.get("html_url") or article.get("url", "")
    if is_blocklisted_url(url, blocklist):
        stats.skipped += 1
        return False

    title = article.get("title", "")
    body_html = article.get("body", "")
    if classify_discontinued(title, body_html[:2000], aggressive=True):
        stats.skipped += 1
        return False

    payload = {"article": article}
    raw = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
    digest = content_hash(raw)
    dest = output / _relative_path(article)
    existing = manifest.get(url)

    if not force and existing and existing.content_hash == digest:
        stats.skipped += 1
        manifest.upsert(
            ResourceRecord(
                url=url,
                source_id=source_id,
                file_path=str(dest),
                content_hash=digest,
                etag=None,
                last_modified=article.get("updated_at"),
                content_length=len(raw),
                status_code=200,
                fetched_at=utc_now(),
            )
        )
        return False

    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(raw)
    stats.downloaded += 1
    manifest.upsert(
        ResourceRecord(
            url=url,
            source_id=source_id,
            file_path=str(dest),
            content_hash=digest,
            etag=None,
            last_modified=article.get("updated_at"),
            content_length=len(raw),
            status_code=200,
            fetched_at=utc_now(),
        )
    )

    title, body = zendesk_article_to_markdown(article)
    rel = zendesk_article_rel_path(source_id, article, section_name)
    knowledge.write(
        rel,
        KnowledgeDoc(
            title=title,
            source=source_id,
            product=product,
            url=url,
            body=body,
            doc_type="support-article",
            category=section_name,
            content_hash=digest,
            extra={
                "article_id": article.get("id"),
                "section_id": article.get("section_id"),
                "updated_at": article.get("updated_at"),
            },
        ),
    )
    return True
