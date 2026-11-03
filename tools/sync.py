#!/usr/bin/env python3
"""CLI para sincronizar documentação Fluig localmente."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml
from rich.console import Console
from rich.table import Table

from mirror.crawlers import CrawlerConfig
from mirror.crawlers.confluence_api import ConfluenceApiCrawler
from mirror.crawlers.confluence_cdp import ConfluenceCdpCrawler
from mirror.crawlers.static import StaticCrawler
from mirror.crawlers.zendesk import ZendeskCrawler
from mirror.manifest import Manifest
from mirror.paths import CACHE_DIR, CONFIG_PATH, KNOWLEDGE_DIR, ROOT, SEARCH_DB, TOOLS_DIR

CRAWLERS = {
    "static": StaticCrawler,
    "confluence-api": ConfluenceApiCrawler,
    "zendesk": ZendeskCrawler,
}

console = Console()


def load_config(config_path: Path) -> dict:
    with config_path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def resolve_data_dir(config_path: Path, config: dict) -> Path:
    """Cache regenerável (mirror, chunks, manifest) — ver mirror/paths.py."""
    return CACHE_DIR


def resolve_knowledge_dir(config_path: Path, config: dict) -> Path:
    return KNOWLEDGE_DIR


def resolve_tdn_source(config: dict, source_id: str) -> tuple[str, str, str]:
    sources = config.get("sources", {})
    if source_id not in sources:
        raise ValueError(f"Fonte desconhecida: {source_id}")
    cfg = sources[source_id]
    chunks_dir = cfg.get("chunks_dir", "chunks/tdn-fluig")
    return source_id, cfg.get("product", "fluig"), chunks_dir


def run_sync(
    config_path: Path,
    sources: list[str] | None,
    force: bool,
) -> int:
    config = load_config(config_path)
    data_dir = resolve_data_dir(config_path, config)
    data_dir.mkdir(parents=True, exist_ok=True)

    all_sources = config.get("sources", {})
    selected = sources or [k for k, v in all_sources.items() if v.get("enabled", True)]

    table = Table(title="Fluig Docs Mirror — Sync")
    table.add_column("Fonte")
    table.add_column("Baixados", justify="right")
    table.add_column("Ignorados", justify="right")
    table.add_column("Erros", justify="right")

    total_errors = 0

    for source_id in selected:
        if source_id not in all_sources:
            console.print(f"[red]Fonte desconhecida: {source_id}[/red]")
            total_errors += 1
            continue

        source_cfg = all_sources[source_id]
        if not source_cfg.get("enabled", True) and not sources:
            continue

        crawler_type = source_cfg.get("type", "static")
        crawler_cls = CRAWLERS.get(crawler_type)
        if not crawler_cls:
            console.print(f"[red]Tipo de crawler inválido: {crawler_type}[/red]")
            total_errors += 1
            continue

        console.print(f"\n[bold cyan]Sincronizando:[/bold cyan] {source_id} ({crawler_type})")
        crawler = crawler_cls(
            CrawlerConfig(
                source_id=source_id,
                config=source_cfg,
                data_dir=str(data_dir),
                force=force,
            )
        )

        try:
            stats = crawler.run()
        except Exception as exc:
            console.print(f"[red]Erro em {source_id}: {exc}[/red]")
            total_errors += 1
            continue

        table.add_row(
            source_id,
            str(stats.downloaded),
            str(stats.skipped),
            str(stats.errors),
        )
        total_errors += stats.errors

    console.print()
    console.print(table)

    manifest = Manifest(data_dir / "manifest.db")
    total = manifest.stats()["total_resources"]
    manifest.close()
    console.print(f"\n[green]Total de recursos no manifest:[/green] {total}")
    console.print(f"[dim]Dados em:[/dim] {data_dir / 'mirror'}")

    return 1 if total_errors else 0


def cmd_export(config_path: Path) -> int:
    from mirror.export_knowledge import export_from_mirror

    config = load_config(config_path)
    data_dir = resolve_data_dir(config_path, config)
    count = export_from_mirror(data_dir, config)
    console.print(
        f"[green]{count} documentos exportados para[/green] {KNOWLEDGE_DIR}"
    )
    return 0


def cmd_export_api(config_path: Path) -> int:
    from mirror.export_api import export_api_fluig
    from mirror.knowledge import KnowledgeStore

    config = load_config(config_path)
    data_dir = resolve_data_dir(config_path, config)
    count = export_api_fluig(data_dir)
    KnowledgeStore(KNOWLEDGE_DIR).rebuild_index_from_disk()
    console.print(
        f"[green]{count} módulos API exportados para[/green] {KNOWLEDGE_DIR / 'fluig' / 'api-fluig'}"
    )
    return 0


def cmd_auth_tdn(config_path: Path) -> int:
    """Abre o browser UMA VEZ para passar o Cloudflare e salvar cookies."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        console.print("[red]Instale dependências TDN: ./tools/scripts/tdn/setup-tdn.sh[/red]")
        return 1

    from mirror.session import (
        browser_profile_dir,
        save_playwright_state,
        session_path,
        test_api_access,
    )

    config = load_config(config_path)
    data_dir = resolve_data_dir(config_path, config)
    tdn_cfg = config.get("sources", {}).get("tdn-fluig", {})
    login_url = tdn_cfg.get(
        "session_test_url",
        "https://tdn.totvs.com/display/public/fluig/Central+de+ajuda",
    )

    session_file = session_path(data_dir)
    profile_dir = browser_profile_dir(data_dir)

    console.print(
        "\n[bold]Autenticação TDN (uma única vez)[/bold]\n"
        "1. O Chrome vai abrir no TDN\n"
        "2. Se aparecer o desafio Cloudflare, confirme que é humano\n"
        "3. [yellow]Aguarde a Central de Ajuda carregar por completo[/yellow]\n"
        "4. Volte aqui e pressione Enter\n"
    )

    with sync_playwright() as p:
        profile_dir.mkdir(parents=True, exist_ok=True)
        try:
            context = p.chromium.launch_persistent_context(
                str(profile_dir),
                headless=False,
                channel="chrome",
                locale="pt-BR",
                viewport={"width": 1440, "height": 900},
                user_agent=(
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/131.0.0.0 Safari/537.36"
                ),
                ignore_default_args=["--enable-automation"],
                args=["--disable-blink-features=AutomationControlled"],
            )
        except Exception:
            context = p.chromium.launch_persistent_context(
                str(profile_dir),
                headless=False,
                locale="pt-BR",
                viewport={"width": 1440, "height": 900},
                user_agent=(
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/131.0.0.0 Safari/537.36"
                ),
                ignore_default_args=["--enable-automation"],
                args=["--disable-blink-features=AutomationControlled"],
            )

        page = context.pages[0] if context.pages else context.new_page()
        page.goto(login_url, wait_until="domcontentloaded", timeout=120000)

        while True:
            input("\n>>> Pressione Enter quando a Central de Ajuda estiver carregada... ")

            ok, msg = test_api_access(context)
            if ok:
                console.print(f"[green]✓ {msg}[/green]")
                break
            console.print(f"[red]✗ {msg}[/red]")
            console.print("[yellow]Resolva o Cloudflare no Chrome e tente novamente.[/yellow]")

        save_playwright_state(context, session_file)
        context.close()

    console.print(f"\n[green]Perfil salvo em:[/green] {profile_dir}")
    console.print(f"[green]Sessão em:[/green] {session_file}")
    console.print(
        "\nAgora o sync é 100% automático (headless, centenas de páginas):\n"
        "  .venv/bin/python tools/sync.py sync --source tdn-fluig"
    )
    return 0


def cmd_import_tdn(
    config_path: Path, export_file: Path, force: bool, source_id: str
) -> int:
    from mirror.import_tdn import import_tdn_export

    if not export_file.exists():
        console.print(f"[red]Arquivo não encontrado:[/red] {export_file}")
        return 1

    config = load_config(config_path)
    data_dir = resolve_data_dir(config_path, config)
    source_id, product, _ = resolve_tdn_source(config, source_id)
    downloaded, skipped = import_tdn_export(
        export_file, data_dir, source_id=source_id, product=product, force=force
    )
    console.print(
        f"[green]Importado ({source_id}):[/green] {downloaded} novos, {skipped} ignorados\n"
        f"Markdown em: {KNOWLEDGE_DIR / product / source_id}"
    )
    return 0


def cmd_import_tdn_dir(
    config_path: Path, dir_path: Path, force: bool, source_id: str
) -> int:
    from mirror.import_tdn import import_tdn_directory

    if not dir_path.is_dir():
        console.print(f"[red]Pasta não encontrada:[/red] {dir_path}")
        return 1

    config = load_config(config_path)
    data_dir = resolve_data_dir(config_path, config)
    source_id, product, _ = resolve_tdn_source(config, source_id)
    downloaded, skipped = import_tdn_directory(
        dir_path, data_dir, source_id=source_id, product=product, force=force
    )
    console.print(
        f"[green]Total importado ({source_id}):[/green] {downloaded} novos, {skipped} ignorados\n"
        f"Markdown em: {KNOWLEDGE_DIR / product / source_id}"
    )
    return 0


def cmd_sync_tdn_cdp(config_path: Path, force: bool) -> int:
    config = load_config(config_path)
    data_dir = resolve_data_dir(config_path, config)
    tdn_cfg = config.get("sources", {}).get("tdn-fluig", {})
    crawler = ConfluenceCdpCrawler(
        CrawlerConfig(
            source_id="tdn-fluig",
            config=tdn_cfg,
            data_dir=str(data_dir),
            force=force,
        )
    )
    import logging
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    try:
        stats = crawler.run()
    except Exception as exc:
        console.print(f"[red]{exc}[/red]")
        return 1
    console.print(
        f"[green]TDN:[/green] {stats.downloaded} baixados, "
        f"{stats.skipped} ignorados, {stats.errors} erros"
    )
    return 0 if not stats.errors else 1


def cmd_receive_tdn(config_path: Path, port: int, source_id: str) -> int:
    from mirror.receive_tdn import run_receiver

    config = load_config(config_path)
    data_dir = resolve_data_dir(config_path, config)
    _, _, chunks_dir = resolve_tdn_source(config, source_id)
    out = data_dir / chunks_dir
    run_receiver(out, port=port, source_id=source_id)
    return 0


def cmd_setup_tdn() -> int:
    import subprocess

    script = TOOLS_DIR / "scripts" / "tdn" / "setup-tdn.sh"
    if not script.exists():
        console.print("[red]Script setup-tdn.sh não encontrado.[/red]")
        return 1
    result = subprocess.run(["bash", str(script)], cwd=ROOT)
    return result.returncode


def cmd_build_index(config_path: Path, products: list[str] | None) -> int:
    from mirror.catalog import build_indexes

    config = load_config(config_path)
    knowledge_dir = resolve_knowledge_dir(config_path, config)
    written = build_indexes(knowledge_dir, products)
    console.print(f"[green]Roteador:[/green] {written[0]}")
    console.print(f"[green]Busca full-text:[/green] {SEARCH_DB}")
    return 0


def cmd_export_tdn_handoff(
    config_path: Path,
    source_id: str,
    dest: Path | None,
) -> int:
    import shutil

    config = load_config(config_path)
    data_dir = resolve_data_dir(config_path, config)
    source_id, product, chunks_dir = resolve_tdn_source(config, source_id)

    knowledge_src = KNOWLEDGE_DIR / product / source_id
    chunks_src = data_dir / chunks_dir
    project_dir = ROOT

    if dest is None:
        dest = Path.home() / "Desktop" / f"{source_id}-export"
    dest = dest.expanduser().resolve()
    dest.mkdir(parents=True, exist_ok=True)

    copied_md = 0
    if knowledge_src.is_dir():
        knowledge_dest = dest / "knowledge" / product / source_id
        if knowledge_dest.exists():
            shutil.rmtree(knowledge_dest)
        shutil.copytree(knowledge_src, knowledge_dest)
        copied_md = sum(1 for _ in knowledge_dest.rglob("*.md"))
    else:
        console.print(f"[yellow]Ainda sem Markdown em {knowledge_src}[/yellow]")

    copied_chunks = 0
    if chunks_src.is_dir():
        chunks_dest = dest / "chunks"
        if chunks_dest.exists():
            shutil.rmtree(chunks_dest)
        shutil.copytree(chunks_src, chunks_dest)
        copied_chunks = len(list(chunks_dest.glob("*.json")))

    script_src = TOOLS_DIR / "scripts" / "console" / _console_script_name(source_id)
    if script_src.exists():
        shutil.copy2(script_src, dest / script_src.name)

    readme = dest / "LEIA-ME.md"
    readme.write_text(
        _handoff_readme(source_id, product, project_dir),
        encoding="utf-8",
    )

    console.print(f"[green]Handoff exportado em:[/green] {dest}")
    console.print(f"  Markdown: {copied_md} arquivos")
    console.print(f"  Chunks JSON: {copied_chunks} arquivos")
    console.print(f"  Guia: {readme}")
    return 0


def _console_script_name(source_id: str) -> str:
    return {
        "tdn-tec": "tdn-export-tec-console.js",
        "tdn-rm": "tdn-export-rm-console.js",
        "tdn-fluig": "tdn-export-console.js",
    }.get(source_id, "tdn-export-console.js")


def _handoff_readme(source_id: str, product: str, project_dir: Path) -> str:
    chunks_name = {
        "tdn-fluig": "chunks/tdn-fluig",
        "tdn-rm": "chunks/tdn-rm",
        "tdn-tec": "chunks/tdn-tec",
    }.get(source_id, f"chunks/{source_id}")
    script_name = _console_script_name(source_id)
    export_obj = {
        "tdn-tec": "tdnTecExport",
        "tdn-rm": "tdnRmExport",
        "tdn-fluig": "tdnExport",
    }.get(source_id, "tdnExport")

    return f"""# Export TDN — {source_id}

Pacote gerado pela base de conhecimento TOTVS.

## Conteúdo desta pasta

| Pasta/arquivo | Descrição |
|---------------|-----------|
| `knowledge/{product}/{source_id}/` | Markdown pronto para IA/RAG |
| `chunks/` | JSON bruto do Confluence (chunks do browser) |
| `{script_name}` | Script para colar no console do Chrome |
| `LEIA-ME.md` | Este guia |

## Quem baixa no browser (dev com acesso ao TDN)

1. Abra o Chrome **normal** (não automatizado)
2. Acesse a home do espaço no TDN e passe o Cloudflare
3. **F12 → Console** → cole o conteúdo de `{script_name}`
4. Rode `{export_obj}.run()` e aguarde terminar
5. Envie os dados de uma destas formas:
   - **Opção A (mesma máquina):** no projeto, `sync.py receive-tdn --source {source_id}` e depois `{export_obj}.sendToLocal()`
   - **Opção B (outra máquina):** `{export_obj}.downloadChunks()` e envie os `tdn-*-chunk-*.json` para a pasta `chunks/` aqui

## Quem importa na base de conhecimento

No repositório `{project_dir.name}`:

```bash
cd "{project_dir}"

# Se recebeu JSON na pasta chunks/ deste pacote:
cp -R chunks/* .cache/{chunks_name}/

# Importar e gerar Markdown
.venv/bin/python tools/sync.py import-tdn-dir .cache/{chunks_name} --source {source_id}
.venv/bin/python tools/sync.py build-index --product {product}

# Atualizar este pacote na Área de Trabalho
.venv/bin/python tools/sync.py export-tdn-handoff --source {source_id}
```

Markdown final: `knowledge/{product}/{source_id}/`

## Busca após importar

```bash
.venv/bin/python tools/sync.py search "SmartClient" --product {product} --source {source_id}
```
"""


def cmd_search(
    config_path: Path,
    query: str,
    product: str | None,
    source: str | None,
    limit: int,
) -> int:
    # Saída em texto puro e compacta (sem tabela/cores): é lida por agentes de IA
    from mirror.search import search, snippet_for

    hits, tokens = search(query, product=product, source=source, limit=limit)
    if not hits:
        print("Nenhum resultado. Tente sinônimos, menos termos ou outra --source.")
        return 0
    for n, hit in enumerate(hits, 1):
        heading, line = snippet_for(hit.path, tokens)
        print(f"[{n}] {hit.title}  ({hit.source}, {max(hit.size // 1024, 1)} KB)")
        print(f"    knowledge/{hit.path}")
        if hit.url:
            # Zendesk abre o artigo só pelo id — corta o slug percent-encoded (~60 tokens)
            print("    " + re.sub(r"(/articles/\d+)-[^?#]*", r"\1", hit.url))
        if heading:
            print(f"    § {heading}")
        if line:
            print(f"    > {line}")
    return 0


def cmd_show(path: str, secao: str | None, max_chars: int) -> int:
    from mirror.search import body_of, doc_path, outline, section

    if not doc_path(path).exists():
        print(f"Arquivo não encontrado: {path}")
        return 1
    if secao:
        meta, text, available = section(path, secao)
        if text is None:
            print(f"Seção \"{secao}\" não encontrada. Seções: " + " | ".join(available[:60]))
            return 1
    else:
        meta, items, size = outline(path)
        if size > max_chars and items:
            print(f"# {meta.get('title', path)}  ({size // 1024} KB) — {meta.get('url', '')}")
            print("Documento grande. Use --secao \"<nome>\" com uma destas seções:")
            print("\n".join(items[:200]))
            return 0
        _, text = body_of(path)  # sem frontmatter: a URL já vai em "Fonte:"
    if meta.get("url"):
        print(f"Fonte: {meta['url']}")
    if len(text) > max_chars:
        text = text[:max_chars] + f"\n… [cortado em {max_chars} caracteres — use --secao ou --max-chars]"
    print(text)
    return 0


def cmd_prune(
    config_path: Path,
    product: str | None,
    dry_run: bool,
    skip_obsolete: bool,
    skip_duplicates: bool,
    aggressive: bool,
    scan_body: bool,
) -> int:
    from mirror.catalog import prune_knowledge

    config = load_config(config_path)
    knowledge_dir = resolve_knowledge_dir(config_path, config)
    removable, count = prune_knowledge(
        knowledge_dir,
        product=product,
        dry_run=dry_run,
        include_obsolete=not skip_obsolete,
        include_duplicates=not skip_duplicates,
        aggressive=aggressive,
        scan_body=scan_body,
    )

    mode = "[dry-run]" if dry_run else "[removido]"
    console.print(f"{mode} {count} arquivos candidatos")

    by_reason: dict[str, int] = {}
    for item in removable:
        reason = item.get("removal_reason", "?")
        by_reason[reason] = by_reason.get(reason, 0) + 1
    for reason, n in sorted(by_reason.items()):
        console.print(f"  {reason}: {n}")

    for item in removable[:20]:
        console.print(f"  - [{item.get('removal_reason')}] {item.get('title', '')[:70]}")
    if len(removable) > 20:
        console.print(f"  ... e mais {len(removable) - 20}")

    if dry_run and count:
        console.print(
            "\n[cyan]Execute com --apply para remover de fato.[/cyan]"
        )
    return 0


def cmd_status(config_path: Path) -> int:
    config = load_config(config_path)
    data_dir = resolve_data_dir(config_path, config)
    db_path = data_dir / "manifest.db"

    if not db_path.exists():
        console.print("[yellow]Nenhum sync executado ainda.[/yellow]")
        return 0

    manifest = Manifest(db_path)
    table = Table(title="Status do espelho local")
    table.add_column("Fonte")
    table.add_column("Recursos", justify="right")

    for source_id in config.get("sources", {}):
        count = manifest.stats(source_id)["total_resources"]
        table.add_row(source_id, str(count))

    table.add_row("[bold]TOTAL[/bold]", str(manifest.stats()["total_resources"]))
    manifest.close()
    console.print(table)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Espelha documentação Fluig com sync incremental."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=CONFIG_PATH,
        help="Arquivo de configuração YAML",
    )
    sub = parser.add_subparsers(dest="command")

    sync_parser = sub.add_parser("sync", help="Sincronizar fontes")
    sync_parser.add_argument(
        "--source",
        action="append",
        dest="sources",
        help="Sincronizar apenas esta fonte (pode repetir)",
    )
    sync_parser.add_argument(
        "--force",
        action="store_true",
        help="Re-baixar tudo ignorando cache",
    )

    sub.add_parser("status", help="Mostrar estatísticas do espelho local")

    sub.add_parser(
        "setup-tdn",
        help="Instalar dependências e Chromium para tdn.totvs.com",
    )

    sub.add_parser(
        "auth-tdn",
        help="Autenticar no TDN (Playwright — pode falhar no Cloudflare)",
    )

    import_parser = sub.add_parser(
        "import-tdn",
        help="Importar JSON exportado pelo console do browser (recomendado)",
    )
    import_parser.add_argument(
        "export_file",
        type=Path,
        help="Arquivo tdn-fluig-export.json baixado pelo script do console",
    )
    import_parser.add_argument("--force", action="store_true")
    import_parser.add_argument(
        "--source",
        default="tdn-fluig",
        help="Fonte TDN (tdn-fluig, tdn-rm, ...)",
    )

    dir_parser = sub.add_parser(
        "import-tdn-dir",
        help="Importar pasta com tdn-chunk-*.json do console",
    )
    dir_parser.add_argument(
        "dir_path",
        type=Path,
        help="Pasta com os chunks baixados",
    )
    dir_parser.add_argument("--force", action="store_true")
    dir_parser.add_argument(
        "--source",
        default="tdn-fluig",
        help="Fonte TDN (tdn-fluig, tdn-rm, ...)",
    )

    cdp_parser = sub.add_parser(
        "sync-tdn-cdp",
        help="Sync TDN via Chrome aberto por você (porta 9222)",
    )
    cdp_parser.add_argument("--force", action="store_true")

    recv_parser = sub.add_parser(
        "receive-tdn",
        help="Servidor local para receber chunks do console do browser",
    )
    recv_parser.add_argument("--port", type=int, default=8765)
    recv_parser.add_argument(
        "--source",
        default="tdn-fluig",
        help="Fonte TDN (tdn-fluig, tdn-rm, ...)",
    )

    sub.add_parser(
        "export",
        help="Regenerar knowledge/ a partir do espelho raw existente",
    )

    sub.add_parser(
        "export-api",
        help="Exportar specs OpenAPI da API Fluig para Markdown",
    )

    index_parser = sub.add_parser(
        "build-index",
        help="Gerar roteador (tools/catalog/_INDEX.md) e índice de busca full-text",
    )
    index_parser.add_argument(
        "--product",
        action="append",
        dest="products",
        choices=["fluig", "rm", "protheus"],
        help="Gerar só este produto (pode repetir)",
    )

    handoff_parser = sub.add_parser(
        "export-tdn-handoff",
        help="Copiar Markdown + chunks TDN para a Área de Trabalho (repasse a outro dev)",
    )
    handoff_parser.add_argument(
        "--source",
        default="tdn-tec",
        help="Fonte TDN (tdn-tec, tdn-rm, tdn-fluig)",
    )
    handoff_parser.add_argument(
        "--dest",
        type=Path,
        default=None,
        help="Pasta destino (padrão: ~/Desktop/<source>-export)",
    )

    search_parser = sub.add_parser(
        "search",
        help="Busca full-text (título, seções e conteúdo) — saída compacta para IA",
    )
    search_parser.add_argument("query", help="Termos de busca")
    search_parser.add_argument(
        "--product",
        choices=["fluig", "rm", "protheus", "totvs"],
        help="Filtrar por produto",
    )
    search_parser.add_argument(
        "--source",
        help="Filtrar por fonte (tdn-fluig, central-rm, tdn-rm, ...)",
    )
    search_parser.add_argument("--limit", type=int, default=5)

    show_parser = sub.add_parser(
        "show",
        help="Ler um documento: pequeno inteiro, grande só o sumário ou uma --secao",
    )
    show_parser.add_argument("path", help="Caminho mostrado pelo search (knowledge/...md)")
    show_parser.add_argument("--secao", "--section", dest="secao", help="Trecho do título da seção")
    show_parser.add_argument("--max-chars", type=int, default=8000)

    prune_parser = sub.add_parser(
        "prune",
        help="Remover duplicatas e documentos explicitamente descontinuados",
    )
    prune_parser.add_argument(
        "--product",
        choices=["fluig", "rm", "protheus", "totvs"],
        help="Limitar limpeza a um produto",
    )
    prune_parser.add_argument(
        "--apply",
        action="store_true",
        help="Executar remoção (padrão: dry-run)",
    )
    prune_parser.add_argument(
        "--keep-obsolete",
        action="store_true",
        help="Não remover títulos obsoletos/descontinuados",
    )
    prune_parser.add_argument(
        "--keep-duplicates",
        action="store_true",
        help="Não remover duplicatas por URL",
    )
    prune_parser.add_argument(
        "--aggressive",
        action="store_true",
        help="Remover todo título com descontinuado/obsoleto/revogado",
    )
    prune_parser.add_argument(
        "--scan-body",
        action="store_true",
        help="Também detectar avisos de descontinuação no corpo do documento",
    )

    args = parser.parse_args()
    command = args.command or "sync"

    if command == "status":
        return cmd_status(args.config)

    if command == "setup-tdn":
        return cmd_setup_tdn()

    if command == "auth-tdn":
        return cmd_auth_tdn(args.config)

    if command == "import-tdn":
        return cmd_import_tdn(
            args.config, args.export_file, args.force, args.source
        )

    if command == "import-tdn-dir":
        return cmd_import_tdn_dir(
            args.config, args.dir_path, args.force, args.source
        )

    if command == "sync-tdn-cdp":
        return cmd_sync_tdn_cdp(args.config, getattr(args, "force", False))

    if command == "receive-tdn":
        return cmd_receive_tdn(args.config, args.port, args.source)

    if command == "export":
        return cmd_export(args.config)

    if command == "export-api":
        return cmd_export_api(args.config)

    if command == "build-index":
        return cmd_build_index(args.config, getattr(args, "products", None))

    if command == "export-tdn-handoff":
        return cmd_export_tdn_handoff(
            args.config,
            getattr(args, "source", "tdn-tec"),
            getattr(args, "dest", None),
        )

    if command == "search":
        return cmd_search(
            args.config,
            args.query,
            getattr(args, "product", None),
            getattr(args, "source", None),
            args.limit,
        )

    if command == "show":
        return cmd_show(args.path, args.secao, args.max_chars)

    if command == "prune":
        return cmd_prune(
            args.config,
            getattr(args, "product", None),
            dry_run=not getattr(args, "apply", False),
            skip_obsolete=getattr(args, "keep_obsolete", False),
            skip_duplicates=getattr(args, "keep_duplicates", False),
            aggressive=getattr(args, "aggressive", False),
            scan_body=getattr(args, "scan_body", False),
        )

    return run_sync(args.config, getattr(args, "sources", None), getattr(args, "force", False))


if __name__ == "__main__":
    sys.exit(main())
