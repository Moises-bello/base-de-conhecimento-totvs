"""Catálogo navegável, busca e limpeza da base knowledge/."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import unquote

from mirror.paths import BLOCKLIST_PATH, CATALOG_DIR, INDEX_PATH


# Título indica que o documento É sobre algo descontinuado/obsoleto.
STRONG_DISCONTINUED_TITLE = (
    re.compile(r"^\[obsoleto\]", re.I),
    re.compile(r"\[obsoleto\]", re.I),
    re.compile(r"\(descontinuad[oa]\)", re.I),
    re.compile(r"\(revogado\)", re.I),
    re.compile(r"documentos descontinuados", re.I),
    re.compile(r"versões anteriores \(descontinuadas\)", re.I),
    re.compile(r"^aviso de descontinuação$", re.I),
    re.compile(r"eai 1\.0 \(descontinuado\)", re.I),
    re.compile(r"descontinuação do gerador", re.I),
    re.compile(r"^deploy granular - descontinuação$", re.I),
    re.compile(r"relatórios descontinuados", re.I),
    re.compile(r"relatórios descontinuad", re.I),
    re.compile(r"eventos descontinuados", re.I),
    re.compile(r"layout .* descontinuados", re.I),
    re.compile(r"ponto de entrada .* descontinuado", re.I),
    re.compile(r"fast startup descontinuado", re.I),
    re.compile(r"descontinuidade dos relatórios", re.I),
    re.compile(r"documento obsoleto", re.I),
    re.compile(r"tornar catalogo obsoleto", re.I),
    re.compile(r"descontinuado a partir", re.I),
    re.compile(r"descontinuidade da geração", re.I),
    re.compile(r"descontinuidade gradual", re.I),
    re.compile(r"descontinuação da guia", re.I),
    re.compile(r"qualificação cadastral - descontinuação", re.I),
    re.compile(r"mensagem de descontinuidade", re.I),
    re.compile(r"mensagem de futura descontinuação", re.I),
    re.compile(r"descontinuar_", re.I),
    re.compile(r"_descontinu", re.I),
    re.compile(r"grade numerada \(descontinuada\)", re.I),
    re.compile(r"integração.*descontinuada", re.I),
)

AGGRESSIVE_DISCONTINUED_TITLE = (
    re.compile(r"\bdescontinuad", re.I),
    re.compile(r"\bobsoleto\b", re.I),
    re.compile(r"\brevogad", re.I),
)

# Artigos de suporte que mencionam descontinuação mas ainda ajudam no dia a dia.
EXCLUDE_DISCONTINUED_TITLE = (
    re.compile(r"erro.*descontinu", re.I),
    re.compile(r"inconsistência", re.I),
    re.compile(r"qual incidência", re.I),
    re.compile(r"qual código", re.I),
    re.compile(r"código da ocorrência", re.I),
    re.compile(r"como preencher", re.I),
    re.compile(r"como migrar", re.I),
    re.compile(r"como configurar", re.I),
    re.compile(r"é possível", re.I),
    re.compile(r"status descontinuado", re.I),
    re.compile(r"empréstimo", re.I),
    re.compile(r"período letivo encerrado", re.I),
    re.compile(r"encerrado para geração", re.I),
    re.compile(r"not supported against", re.I),
    re.compile(r"indicador de contrib", re.I),
    re.compile(r"descontinuar uma action", re.I),
)

DISCONTINUED_BODY = re.compile(
    r"(?:^|\n)(?:#{1,3}\s*)?"
    r"(?:\[obsoleto\]|aviso de descontinuação|versões anteriores \(descontinuadas\))",
    re.I | re.M,
)

# Modo conservador (prune padrão anterior).
OBSOLETE_TITLE_PATTERNS = STRONG_DISCONTINUED_TITLE[:12]


def load_index(knowledge_dir: Path) -> list[dict[str, Any]]:
    if not INDEX_PATH.exists():
        return []
    return json.loads(INDEX_PATH.read_text(encoding="utf-8"))


def save_index(knowledge_dir: Path, entries: list[dict[str, Any]]) -> Path:
    index_path = INDEX_PATH
    index_path.parent.mkdir(parents=True, exist_ok=True)
    merged = sorted(entries, key=lambda x: x["path"])
    index_path.write_text(
        json.dumps(merged, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return index_path


def normalize_url(url: str) -> str:
    u = unquote(url or "").lower().rstrip("/")
    u = u.replace("+", " ").replace("%2c", ",")
    return re.sub(r"\s+", " ", u)


def is_obsolete_for_removal(title: str) -> bool:
    """Modo conservador — compatível com prune anterior."""
    t = title.strip()
    if not t:
        return False
    tl = t.lower()
    return any(p.search(tl) for p in OBSOLETE_TITLE_PATTERNS)


def _read_body_preview(knowledge_dir: Path, rel_path: str, limit: int = 2000) -> str:
    path = knowledge_dir / rel_path
    if not path.exists():
        return ""
    text = path.read_text(encoding="utf-8", errors="ignore")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2][:limit]
    return text[:limit]


def classify_discontinued(
    title: str,
    body: str = "",
    *,
    aggressive: bool = False,
    scan_body: bool = False,
) -> str | None:
    """Retorna motivo da remoção ou None se deve manter."""
    tl = title.strip().lower()
    if not tl:
        return None
    if any(p.search(tl) for p in EXCLUDE_DISCONTINUED_TITLE):
        return None
    if any(p.search(tl) for p in STRONG_DISCONTINUED_TITLE):
        return "descontinuado"
    if aggressive and any(p.search(tl) for p in AGGRESSIVE_DISCONTINUED_TITLE):
        return "descontinuado"
    if scan_body and body and DISCONTINUED_BODY.search(body):
        return "descontinuado-corpo"
    return None


def is_discontinued_for_removal(
    title: str,
    body: str = "",
    *,
    aggressive: bool = False,
    scan_body: bool = False,
) -> bool:
    return classify_discontinued(
        title,
        body,
        aggressive=aggressive,
        scan_body=scan_body,
    ) is not None


def load_blocklist(knowledge_dir: Path) -> dict[str, Any]:
    path = BLOCKLIST_PATH
    if not path.exists():
        return {"urls": [], "paths": [], "entries": []}
    return json.loads(path.read_text(encoding="utf-8"))


def save_blocklist(knowledge_dir: Path, blocklist: dict[str, Any]) -> Path:
    path = BLOCKLIST_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(blocklist, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return path


def is_blocklisted_url(url: str, blocklist: dict[str, Any]) -> bool:
    norm = normalize_url(url)
    blocked = {normalize_url(u) for u in blocklist.get("urls", [])}
    return norm in blocked


def update_blocklist(
    knowledge_dir: Path,
    removed: list[dict[str, Any]],
) -> Path:
    blocklist = load_blocklist(knowledge_dir)
    urls = set(blocklist.get("urls", []))
    paths = set(blocklist.get("paths", []))
    entries = blocklist.get("entries", [])
    now = datetime.now(timezone.utc).isoformat()

    for item in removed:
        url = item.get("url", "")
        path = item.get("path", "")
        if url:
            urls.add(url)
        if path:
            paths.add(path)
        entries.append(
            {
                "path": path,
                "url": url,
                "title": item.get("title", ""),
                "product": item.get("product", ""),
                "source": item.get("source", ""),
                "reason": item.get("removal_reason", ""),
                "removed_at": now,
            }
        )

    blocklist["urls"] = sorted(urls)
    blocklist["paths"] = sorted(paths)
    blocklist["entries"] = entries
    return save_blocklist(knowledge_dir, blocklist)


def _pick_duplicate_to_keep(items: list[dict[str, Any]]) -> dict[str, Any]:
    """Prefere path com nome de categoria legível em vez de pasta numérica."""

    def score(item: dict[str, Any]) -> tuple[int, int, str]:
        path = item["path"]
        numeric_folder = bool(re.search(r"/\d+/", path))
        return (numeric_folder, len(path), path)

    return sorted(items, key=score)[0]


def find_removable(
    entries: list[dict[str, Any]],
    knowledge_dir: Path | None = None,
    *,
    product: str | None = None,
    include_obsolete: bool = True,
    include_duplicates: bool = True,
    aggressive: bool = False,
    scan_body: bool = False,
) -> list[dict[str, Any]]:
    filtered = [
        e
        for e in entries
        if not product or e.get("product") == product
    ]
    to_remove: dict[str, dict[str, Any]] = {}
    reasons: dict[str, str] = {}

    if include_obsolete:
        for item in filtered:
            body = ""
            if knowledge_dir and (aggressive or scan_body):
                body = _read_body_preview(knowledge_dir, item["path"])
            reason = classify_discontinued(
                item.get("title", ""),
                body,
                aggressive=aggressive,
                scan_body=scan_body,
            )
            if not reason and not aggressive:
                if is_obsolete_for_removal(item.get("title", "")):
                    reason = "obsoleto"
            if reason:
                to_remove[item["path"]] = item
                reasons[item["path"]] = reason

    if include_duplicates:
        by_url: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for item in filtered:
            url = normalize_url(item.get("url", ""))
            if url:
                by_url[url].append(item)
        for group in by_url.values():
            if len(group) < 2:
                continue
            keep = _pick_duplicate_to_keep(group)
            for item in group:
                if item["path"] != keep["path"]:
                    to_remove[item["path"]] = item
                    reasons[item["path"]] = "duplicata"

    return [
        {**to_remove[path], "removal_reason": reasons[path]}
        for path in sorted(to_remove)
    ]


def prune_knowledge(
    knowledge_dir: Path,
    *,
    product: str | None = None,
    dry_run: bool = True,
    include_obsolete: bool = True,
    include_duplicates: bool = True,
    aggressive: bool = False,
    scan_body: bool = False,
) -> tuple[list[dict[str, Any]], int]:
    entries = load_index(knowledge_dir)
    removable = find_removable(
        entries,
        knowledge_dir,
        product=product,
        include_obsolete=include_obsolete,
        include_duplicates=include_duplicates,
        aggressive=aggressive,
        scan_body=scan_body,
    )
    remove_paths = {item["path"] for item in removable}

    if not dry_run:
        discontinued = [
            item
            for item in removable
            if item.get("removal_reason", "").startswith("descontinuado")
            or item.get("removal_reason") == "obsoleto"
        ]
        if discontinued:
            update_blocklist(knowledge_dir, discontinued)

        for rel in remove_paths:
            target = knowledge_dir / rel
            if target.exists():
                target.unlink()
        remaining = [e for e in entries if e["path"] not in remove_paths]
        save_index(knowledge_dir, remaining)

    return removable, len(remove_paths)


# Roteador único (tools/catalog/_INDEX.md): diz QUAL fonte usar, não lista documentos.
# Listas completas custavam até ~200 mil tokens por arquivo; a busca FTS substitui isso.
SOURCES = [
    # (produto, fonte, rótulo, quando usar)
    ("fluig", "tdn-fluig", "TDN Fluig", "processos/BPM, datasets, formulários, widgets, servidor, instalação, FAQ"),
    ("fluig", "api-fluig", "API REST (OpenAPI)", "endpoints novos: admin, process-management, dataset, ecm-forms…"),
    ("fluig", "rest-fluig", "API REST pública /api/public", "endpoints /2.0, /ecm, /bpm, /alert e VOs JSON (campos, obrigatórios)"),
    ("fluig", "sdk-fluig", "Fluig SDK Java", "fluigAPI, WorkflowAPIService e VOs Java do fluig-sdk-api.jar"),
    ("fluig", "style-guide", "Style Guide", "componentes visuais, CSS, FLUIGC"),
    ("rm", "central-rm", "Central de Atendimento RM", "como fazer, erro, rotina, configuração (perguntas vagas: comece aqui)"),
    ("rm", "tdn-rm", "TDN RM (LRM)", "parâmetros, eSocial/CLT, WebServices, releases (técnico)"),
    ("protheus", "central-protheus", "Central de Atendimento Protheus", "como fazer, erro, rotina, configuração"),
    ("protheus", "tdn-tec", "TDN TEC", "AdvPL/TLPP, AppServer, SmartClient, TOTVS Platform"),
    ("totvs", "central-ciclo-vida", "Ciclo de Vida TOTVS", "comunicados, políticas, fim de suporte de versões"),
]


def build_indexes(knowledge_dir: Path, products: list[str] | None = None) -> list[Path]:
    """Gera tools/catalog/_INDEX.md (roteador compacto) e o índice de busca .cache/search.db."""
    from collections import Counter

    from mirror.knowledge import KnowledgeStore
    from mirror.search import build_search_index

    # index.json não é versionado: recria a partir do frontmatter (clone novo já sai pronto)
    KnowledgeStore(knowledge_dir).rebuild_index_from_disk()
    counts = Counter(e.get("source", "") for e in load_index(knowledge_dir))
    lines = [
        "# Base TOTVS — roteador",
        "",
        "Não liste pastas: **busque** e abra só o necessário.",
        "",
        "```bash",
        '.venv/bin/python tools/sync.py search "termos" --product <produto> [--source <fonte>]',
        ".venv/bin/python tools/sync.py show knowledge/<arquivo>.md                # pequeno: inteiro; grande: sumário",
        '.venv/bin/python tools/sync.py show knowledge/<arquivo>.md --secao "nome" # só uma seção',
        "```",
        "",
        "| Produto | Fonte (`--source`) | Docs | Quando usar |",
        "|---|---|---|---|",
    ]
    for product, source, label, when in SOURCES:
        lines.append(f"| {product} | `{source}` — {label} | {counts.get(source, 0)} | {when} |")
    router = CATALOG_DIR / "_INDEX.md"
    router.parent.mkdir(parents=True, exist_ok=True)
    router.write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Remove índices antigos por produto/fonte (listas enormes)
    for old in CATALOG_DIR.glob("*/**/_INDEX*.md"):
        old.unlink()
    for folder in sorted((d for d in CATALOG_DIR.glob("**/") if d != CATALOG_DIR), reverse=True):
        if not any(folder.iterdir()):
            folder.rmdir()

    build_search_index()
    return [router]
