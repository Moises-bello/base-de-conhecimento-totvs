"""Converte artigos Zendesk Help Center para Markdown."""

from __future__ import annotations

from mirror.knowledge import html_to_markdown_body, slugify


def zendesk_article_to_markdown(article: dict) -> tuple[str, str]:
    title = article.get("title", "sem-titulo")
    body_html = article.get("body", "") or ""
    body = html_to_markdown_body(f"<article>{body_html}</article>")
    return title, body


def zendesk_article_rel_path(source_id: str, article: dict, section_name: str = "") -> str:
    article_id = article.get("id", 0)
    title_slug = slugify(article.get("title", str(article_id)))
    section_slug = slugify(section_name) if section_name else "geral"
    return f"{source_id}/{section_slug}/{article_id}-{title_slug}"
