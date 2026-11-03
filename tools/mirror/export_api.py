"""Exporta specs OpenAPI da API Fluig para Markdown na camada knowledge/."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import httpx

from mirror.knowledge import KnowledgeDoc, KnowledgeStore, slugify
from mirror.manifest import content_hash
from mirror.paths import KNOWLEDGE_DIR

API_BASE = "https://api.fluig.com/latest/"
CARDS_REL = "mirror/api-fluig/api.fluig.com/latest/assets/data/cards.json"
SWAGGER_MIRROR_DIR = "mirror/api-fluig/swagger"


def export_api_fluig(data_dir: Path, fetch_live: bool = True) -> int:
    """Baixa swagger.json de cada módulo e gera um .md por módulo."""
    cards_path = data_dir / CARDS_REL
    if not cards_path.exists():
        raise FileNotFoundError(f"cards.json não encontrado: {cards_path}")

    cards = json.loads(cards_path.read_text(encoding="utf-8"))
    knowledge = KnowledgeStore(KNOWLEDGE_DIR)
    mirror_dir = data_dir / SWAGGER_MIRROR_DIR
    mirror_dir.mkdir(parents=True, exist_ok=True)

    count = 0
    with httpx.Client(timeout=60, follow_redirects=True) as client:
        for item in cards.get("items", []):
            if not item.get("enable"):
                continue

            link = item["link"].strip("./")
            module_slug = link.split("/")[0]
            title = item.get("title", module_slug)
            description = item.get("description", "")
            swagger_url = f"{API_BASE}{module_slug}/swagger-ui/swagger.json"

            spec = _load_spec(client, swagger_url, mirror_dir / f"{module_slug}.json", fetch_live)
            if not spec:
                continue

            body = openapi_spec_to_markdown(spec, title, description, swagger_url)
            raw = body.encode("utf-8")
            knowledge.write(
                f"api-fluig/{slugify(module_slug)}",
                KnowledgeDoc(
                    title=f"API Fluig — {title}",
                    source="api-fluig",
                    product="fluig",
                    url=f"{API_BASE}{module_slug}/swagger-ui/",
                    body=body,
                    doc_type="api-reference",
                    category=module_slug,
                    content_hash=content_hash(raw),
                    extra={
                        "module": module_slug,
                        "endpoints": _count_operations(spec),
                        "openapi_version": spec.get("swagger") or spec.get("openapi", ""),                    },
                ),
            )
            count += 1

    knowledge.save_index()
    return count


def _load_spec(
    client: httpx.Client,
    url: str,
    mirror_path: Path,
    fetch_live: bool,
) -> dict[str, Any] | None:
    if fetch_live:
        try:
            response = client.get(url)
            response.raise_for_status()
            spec = response.json()
            mirror_path.write_text(
                json.dumps(spec, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            return spec
        except Exception:
            if mirror_path.exists():
                return json.loads(mirror_path.read_text(encoding="utf-8"))
            return None

    if mirror_path.exists():
        return json.loads(mirror_path.read_text(encoding="utf-8"))
    return None


def _count_operations(spec: dict[str, Any]) -> int:
    total = 0
    for path_item in spec.get("paths", {}).values():
        for method in path_item:
            if method in ("get", "post", "put", "patch", "delete", "head", "options"):
                total += 1
    return total


def openapi_spec_to_markdown(
    spec: dict[str, Any],
    module_title: str,
    module_description: str,
    swagger_url: str,
) -> str:
    info = spec.get("info", {})
    lines = [
        f"# {module_title}",
        "",
        module_description or info.get("description", ""),
        "",
        f"**Spec:** {swagger_url}",
        "",
    ]

    host = spec.get("host", "")
    base_path = spec.get("basePath", "")
    schemes = spec.get("schemes", ["https"])
    if host:
        lines.append(f"**Base URL:** `{schemes[0]}://{host}{base_path}`")
        lines.append("")

    for path, path_item in sorted(spec.get("paths", {}).items()):
        for method, operation in sorted(path_item.items()):
            if method not in ("get", "post", "put", "patch", "delete", "head", "options"):
                continue
            lines.extend(_operation_section(method.upper(), path, operation))

    return "\n".join(lines).strip()


def _operation_section(method: str, path: str, operation: dict[str, Any]) -> list[str]:
    summary = operation.get("summary", "")
    description = operation.get("description", "")
    operation_id = operation.get("operationId", "")

    lines = [
        f"## {method} `{path}`",
        "",
    ]
    if summary:
        lines.append(f"**{summary}**")
        lines.append("")
    if description and description != summary:
        lines.append(description)
        lines.append("")
    if operation_id:
        lines.append(f"- **operationId:** `{operation_id}`")

    tags = operation.get("tags", [])
    if tags:
        lines.append(f"- **tags:** {', '.join(tags)}")

    params = operation.get("parameters", [])
    if params:
        lines.append("")
        lines.append("### Parâmetros")
        lines.append("")
        lines.append("| Nome | Em | Tipo | Obrigatório | Descrição |")
        lines.append("|------|-----|------|-------------|-----------|")
        for param in params:
            name = param.get("name", "")
            location = param.get("in", "")
            required = "sim" if param.get("required") else "não"
            ptype = _param_type(param)
            desc = (param.get("description") or "").replace("\n", " ").strip()
            lines.append(f"| `{name}` | {location} | {ptype} | {required} | {desc} |")

    body_param = operation.get("requestBody") or _find_body_param(params)
    if body_param:
        lines.append("")
        lines.append("### Corpo da requisição")
        lines.append("")
        lines.append(_format_body(body_param))

    responses = operation.get("responses", {})
    if responses:
        lines.append("")
        lines.append("### Respostas")
        lines.append("")
        for code, response in sorted(responses.items(), key=lambda x: x[0]):
            desc = (response.get("description") or "").replace("\n", " ").strip()
            lines.append(f"- **{code}:** {desc}")

    lines.append("")
    return lines


def _find_body_param(params: list[dict[str, Any]]) -> dict[str, Any] | None:
    for param in params:
        if param.get("in") == "body":
            return param
    return None


def _param_type(param: dict[str, Any]) -> str:
    if "schema" in param:
        return _schema_type(param["schema"])
    return param.get("type", "")


def _format_body(body: dict[str, Any]) -> str:
    schema = body.get("schema", body)
    if "content" in body:
        parts = []
        for content_type, media in body["content"].items():
            parts.append(f"**{content_type}:** `{_schema_type(media.get('schema', {}))}`")
        return "\n".join(parts)
    return f"`{_schema_type(schema)}`"


def _schema_type(schema: dict[str, Any]) -> str:
    if not schema:
        return "object"
    if "$ref" in schema:
        return schema["$ref"].split("/")[-1]
    schema_type = schema.get("type", "object")
    if schema_type == "array":
        return f"array[{_schema_type(schema.get('items', {}))}]"
    return schema_type
