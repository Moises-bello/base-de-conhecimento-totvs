"""Caminhos fixos da base de conhecimento (fonte única — não montar à mão em outros módulos).

    knowledge/       somente documentação oficial TOTVS (Markdown com frontmatter)
    tools/catalog/   gerado: _INDEX.md (roteador), index.json (metadados), blocklist de descontinuados
    tools/inputs/    arquivos exportados manualmente (ex.: schema RM) — não regeneráveis
    .cache/          mirror HTML, chunks do console, manifest.db — pode apagar e regenerar
    .cache/secrets/  cookies, sessões e perfis de browser do TDN
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOLS_DIR = ROOT / "tools"
CONFIG_PATH = TOOLS_DIR / "config" / "sources.yaml"

KNOWLEDGE_DIR = ROOT / "knowledge"
CATALOG_DIR = TOOLS_DIR / "catalog"
INDEX_PATH = CATALOG_DIR / "index.json"
BLOCKLIST_PATH = CATALOG_DIR / "blocklist-discontinued.json"
INPUTS_DIR = TOOLS_DIR / "inputs"
SCHEMA_EXPORTS_DIR = INPUTS_DIR / "schema-exports"

CACHE_DIR = ROOT / ".cache"
SECRETS_DIR = CACHE_DIR / "secrets"
SEARCH_DB = CACHE_DIR / "search.db"  # índice full-text (build-index)
CHUNKS_DIR = CACHE_DIR / "chunks"
