"""Busca full-text (SQLite FTS5) e leitura por seção — saída enxuta para gastar poucos tokens.

    build_search_index()  lê knowledge/**/*.md e grava .cache/search.db (regenerável)
    search()              ranking bm25 em título > headings > corpo, sem acentos, com prefixo
    snippet_for()         linha mais relevante + heading onde ela está
    outline() / section() lê só o pedaço necessário de documentos grandes
"""

from __future__ import annotations

import re
import sqlite3
import subprocess
import unicodedata
from dataclasses import dataclass
from pathlib import Path

from mirror.paths import INDEX_PATH, KNOWLEDGE_DIR, SEARCH_DB

BODY_LIMIT = 200_000  # caracteres indexados por documento
HEADING_RE = re.compile(r"^\s*(?:[-*+]\s+)?(#{1,6})\s+(.+?)\s*#*\s*$")
LINK_URL_RE = re.compile(r"\]\((?:https?://|knowledge/)[^)]*\)")
TOKEN_RE = re.compile(r"[\wÀ-ɏ]+", re.UNICODE)


@dataclass
class Hit:
    path: str
    title: str
    source: str
    product: str
    url: str
    size: int


def fold(text: str) -> str:
    """Minúsculas sem acento — mesma normalização do tokenizer unicode61."""
    return "".join(
        c for c in unicodedata.normalize("NFKD", text.lower()) if not unicodedata.combining(c)
    )


def split_doc(text: str) -> tuple[dict[str, str], str]:
    meta: dict[str, str] = {}
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            for line in text[4:end].splitlines():
                key, sep, value = line.partition(":")
                if sep and not line.startswith(" "):
                    meta[key.strip()] = value.strip().strip("'\"")
            text = text[end + 4:].lstrip("\n")
    return meta, text


def doc_path(path: str) -> Path:
    """Aceita `knowledge/fluig/x.md`, `fluig/x.md` ou caminho absoluto."""
    p = Path(path).expanduser()
    if p.is_absolute():
        return p
    rel = path.removeprefix("knowledge/")
    return KNOWLEDGE_DIR / rel


def build_search_index() -> int:
    tmp = SEARCH_DB.with_suffix(".tmp")
    tmp.parent.mkdir(parents=True, exist_ok=True)
    tmp.unlink(missing_ok=True)
    con = sqlite3.connect(tmp)
    con.executescript(
        """
        CREATE TABLE docs (id INTEGER PRIMARY KEY, path TEXT, title TEXT, source TEXT,
                           product TEXT, url TEXT, size INTEGER);
        CREATE VIRTUAL TABLE docs_fts USING fts5(
            title, headings, body,
            content='', tokenize='unicode61 remove_diacritics 2', prefix='3'
        );
        """
    )
    count = 0
    for md in sorted(KNOWLEDGE_DIR.rglob("*.md")):
        text = md.read_text(encoding="utf-8", errors="ignore")
        meta, body = split_doc(text)
        rel = md.relative_to(KNOWLEDGE_DIR).as_posix()
        title = meta.get("title") or md.stem
        headings = " ".join(m.group(2) for m in map(HEADING_RE.match, body.splitlines()) if m)
        count += 1
        con.execute(
            "INSERT INTO docs VALUES (?,?,?,?,?,?,?)",
            (count, rel, title, meta.get("source", ""), meta.get("product", ""),
             meta.get("url", ""), len(text)),
        )
        con.execute(
            "INSERT INTO docs_fts(rowid, title, headings, body) VALUES (?,?,?,?)",
            (count, title, headings, LINK_URL_RE.sub("]", body[:BODY_LIMIT])),
        )
    con.execute("INSERT INTO docs_fts(docs_fts) VALUES ('optimize')")
    con.execute("CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT)")
    con.execute("INSERT INTO meta VALUES ('git_head', ?)", (_git_head(),))
    con.commit()
    con.close()
    tmp.replace(SEARCH_DB)
    return count


def _git_head() -> str:
    """Commit atual do repositório da base ('' fora de um git) — muda após git pull."""
    try:
        out = subprocess.run(
            ["git", "-C", str(KNOWLEDGE_DIR.parent), "rev-parse", "HEAD"],
            capture_output=True, text=True, timeout=5,
        )
        return out.stdout.strip() if out.returncode == 0 else ""
    except (OSError, subprocess.SubprocessError):
        return ""


def index_is_stale() -> bool:
    """Reindexar quando: não existe, catálogo mudou (import/export/prune) ou outro commit (git pull)."""
    if not SEARCH_DB.exists():
        return True
    if INDEX_PATH.exists() and INDEX_PATH.stat().st_mtime > SEARCH_DB.stat().st_mtime:
        return True
    try:
        con = sqlite3.connect(SEARCH_DB)
        row = con.execute("SELECT value FROM meta WHERE key = 'git_head'").fetchone()
        con.close()
    except sqlite3.Error:
        return True  # índice de versão anterior, sem tabela meta
    return (row[0] if row else "") != _git_head()


def _tokens(query: str) -> list[str]:
    return [t for t in TOKEN_RE.findall(fold(query)) if len(t) >= 2]


def search(
    query: str,
    *,
    product: str | None = None,
    source: str | None = None,
    limit: int = 5,
) -> tuple[list[Hit], list[str]]:
    tokens = _tokens(query)
    if not tokens:
        return [], []
    if index_is_stale():  # import/export/prune alteraram o catálogo: reindexa (~20 s)
        build_search_index()
    con = sqlite3.connect(SEARCH_DB)
    sql = (
        "SELECT d.path, d.title, d.source, d.product, d.url, d.size "
        "FROM docs_fts JOIN docs d ON d.id = docs_fts.rowid "
        "WHERE docs_fts MATCH ? AND (? IS NULL OR d.product = ?) AND (? IS NULL OR d.source = ?) "
        "ORDER BY bm25(docs_fts, 10.0, 4.0, 1.0) LIMIT ?"
    )
    terms = [f'"{t}"*' if len(t) >= 3 else f'"{t}"' for t in tokens]
    rows: list[tuple] = []
    # Primeiro todos os termos (AND); se nada casar, qualquer termo (OR)
    for joiner in (" ", " OR "):
        rows = con.execute(sql, (joiner.join(terms), product, product, source, source, limit)).fetchall()
        if rows:
            break
    con.close()
    return [Hit(*row) for row in rows], tokens


def snippet_for(path: str, tokens: list[str], width: int = 220) -> tuple[str, str]:
    """(heading da seção, linha com mais termos da busca)."""
    try:
        _, body = split_doc(doc_path(path).read_text(encoding="utf-8", errors="ignore"))
    except OSError:
        return "", ""
    best, best_score, best_heading, heading = "", 0, "", ""
    for line in body.splitlines():
        h = HEADING_RE.match(line)
        if h:
            heading = h.group(2)
            continue  # o heading já aparece em "§"; o trecho deve trazer conteúdo
        folded = fold(line)
        score = sum(1 for t in tokens if t in folded)
        if score > best_score and line.strip():
            best, best_score, best_heading = line.strip(), score, heading
            if score == len(tokens):
                break
    best = re.sub(r"\s+", " ", LINK_URL_RE.sub("]", best))
    return best_heading, (best[: width - 1] + "…") if len(best) > width else best


MD_LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")


def _sections(body: str) -> list[tuple[int, str, int]]:
    """(nível, título sem links/ênfase, nº da linha) de cada heading."""
    out = []
    for i, line in enumerate(body.splitlines()):
        m = HEADING_RE.match(line)
        if m:
            title = MD_LINK_RE.sub(r"\1", m.group(2)).replace("\\", "").strip("*_ ")
            out.append((len(m.group(1)), title, i))
    return out


def body_of(path: str) -> tuple[dict[str, str], str]:
    return split_doc(doc_path(path).read_text(encoding="utf-8", errors="ignore"))


def outline(path: str) -> tuple[dict[str, str], list[str], int]:
    meta, body = split_doc(doc_path(path).read_text(encoding="utf-8", errors="ignore"))
    lines = body.splitlines()
    secs = _sections(body)
    items = []
    for idx, (level, title, start) in enumerate(secs):
        end = next((s for lv, _, s in secs[idx + 1:] if lv <= level), len(lines))
        size = sum(len(x) + 1 for x in lines[start:end])
        items.append(f"{'  ' * (level - 1)}- {title}  ({size // 1024 or '<1'} KB)")
    return meta, items, len(body)


def section(path: str, name: str) -> tuple[dict[str, str], str | None, list[str]]:
    """Texto da primeira seção cujo heading contém `name` (sem acento/caixa)."""
    meta, body = split_doc(doc_path(path).read_text(encoding="utf-8", errors="ignore"))
    lines = body.splitlines()
    secs = _sections(body)
    wanted = fold(name)
    matches = [s for s in secs if wanted in fold(s[1])]
    if not matches:
        return meta, None, [t for _, t, _ in secs]
    # Prefere heading idêntico ao pedido; senão o primeiro que contém
    level, _, start = next((s for s in matches if fold(s[1]) == wanted), matches[0])
    end = next((s for lv, _, s in secs if s > start and lv <= level), len(lines))
    return meta, "\n".join(lines[start:end]).strip(), []
