#!/usr/bin/env python3
"""Exporta a documentação de api.fluig.com/old/ para JSON compatível com `sync.py import-tdn`.

Dois conjuntos (nenhum passa por Cloudflare, então roda direto do terminal):

    rest  → https://api.fluig.com/old/            API REST pública (Enunciate):
            recursos (resource_*.html) + tipos de dados JSON (json_*.html, os VOs com campos)
    sdk   → https://api.fluig.com/old/sdk/        Javadoc do fluig-sdk-api.jar (com.fluig.sdk.*)

Uso (na raiz da base):
    .venv/bin/python tools/scripts/fluig-api/export-fluig-old-docs.py rest
    .venv/bin/python tools/sync.py import-tdn .cache/chunks/rest-fluig/rest-fluig-export.json --source rest-fluig

    .venv/bin/python tools/scripts/fluig-api/export-fluig-old-docs.py sdk
    .venv/bin/python tools/sync.py import-tdn .cache/chunks/sdk-fluig/sdk-fluig-export.json --source sdk-fluig

    .venv/bin/python tools/sync.py build-index --product fluig
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin

import httpx
from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from mirror.paths import CHUNKS_DIR  # noqa: E402

REST_BASE = "https://api.fluig.com/old/"
SDK_BASE = "https://api.fluig.com/old/sdk/"
WORKERS = 6
RETRIES = 3

REST_NOTE = (
    "<p><em>Paths relativos à base da API pública do Fluig "
    "(normalmente <code>https://[servidor]/api/public</code>). "
    "Autenticação OAuth — ver TDN \"Fluig API\".</em></p>"
)


def fetch(client: httpx.Client, url: str) -> str:
    for attempt in range(1, RETRIES + 1):
        try:
            response = client.get(url)
            response.raise_for_status()
            return response.text
        except httpx.HTTPError:
            if attempt == RETRIES:
                raise
            time.sleep(attempt)
    raise AssertionError("unreachable")


def links(html: str, base: str, prefixes: tuple[str, ...]) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    found: list[str] = []
    # Enunciate lista recursos/tipos em <tr class="clickable-row" data-href="...">, não em <a>
    for el in soup.select("a[href], [data-href]"):
        href = (el.get("href") or el.get("data-href")).split("#")[0]
        name = href.rsplit("/", 1)[-1]
        if not href.endswith(".html") or "class-use/" in href:
            continue
        if prefixes and not name.startswith(prefixes):
            continue
        url = urljoin(base, href)
        if url.startswith(base) and url not in found:
            found.append(url)
    return found


def rest_targets(client: httpx.Client) -> list[str]:
    index = fetch(client, REST_BASE + "index.html")
    data = fetch(client, REST_BASE + "data.html")
    # xml_*.html são a mesma estrutura dos json_*.html em XML — ignorados
    return (
        [REST_BASE + "index.html"]
        + links(index, REST_BASE, ("resource_",))
        + links(data, REST_BASE, ("json_",))
    )


def sdk_targets(client: httpx.Client) -> list[str]:
    targets = links(fetch(client, SDK_BASE + "allclasses.html"), SDK_BASE, ())
    packages = sorted({u.rsplit("/", 1)[0] + "/" for u in targets})
    return targets + [p + "package-summary.html" for p in packages]


def absolutize(soup: BeautifulSoup, url: str) -> None:
    for tag in soup(["script", "noscript", "nav"]):
        tag.decompose()
    for a in soup.select("a[href]"):
        a["href"] = urljoin(url, a["href"])


def rest_page(url: str, html: str) -> tuple[str, str]:
    soup = BeautifulSoup(html, "html.parser")  # lxml trunca o HTML malformado do Enunciate
    absolutize(soup, url)
    main = soup.select_one(".content__main") or soup.body
    h1 = main.select_one("h1")
    heading = " ".join(h1.get_text(" ").split()) if h1 else url.rsplit("/", 1)[-1]
    name = url.rsplit("/", 1)[-1]
    if name == "index.html":
        title = "Fluig REST — índice de recursos (paths e métodos)"
    else:
        title = f"Fluig REST — {heading}"  # ex.: "AlertServiceRest Resource", "CancelInstanceVO Data Type"
    body = str(main)
    if name.startswith("resource_") or name == "index.html":
        body = REST_NOTE + body
    return title, body


def sdk_page(url: str, html: str) -> tuple[str, str]:
    soup = BeautifulSoup(html, "html.parser")  # lxml trunca o HTML malformado do Enunciate
    for sel in (".topNav", ".bottomNav", ".subNav", ".legalCopy", ".skipNav"):
        for tag in soup.select(sel):
            tag.decompose()
    absolutize(soup, url)
    rel = url[len(SDK_BASE):].removesuffix(".html")
    if rel.endswith("/package-summary"):
        title = "Fluig SDK — pacote " + rel.removesuffix("/package-summary").replace("/", ".")
    else:
        kind_el = soup.select_one(".header .title")
        kind = kind_el.get_text(" ").split()[0] if kind_el else ""
        title = f"Fluig SDK — {rel.replace('/', '.')}" + (f" ({kind})" if kind else "")
    parts = [str(el) for el in (soup.select_one(".header"), soup.select_one(".contentContainer")) if el]
    return title, "\n".join(parts) or str(soup.body)


KINDS = {
    "rest": ("rest-fluig", REST_BASE, rest_targets, rest_page),
    "sdk": ("sdk-fluig", SDK_BASE, sdk_targets, sdk_page),
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("kind", choices=KINDS)
    parser.add_argument("--out", type=Path, help="Arquivo JSON de saída")
    args = parser.parse_args()

    source_id, base, list_targets, to_page = KINDS[args.kind]
    out = args.out or CHUNKS_DIR / source_id / f"{source_id}-export.json"

    pages: list[dict] = []
    skipped: list[dict] = []
    with httpx.Client(timeout=60, follow_redirects=True) as client:
        targets = list_targets(client)
        print(f"{source_id}: {len(targets)} páginas")

        def export(url: str) -> None:
            try:
                title, body = to_page(url, fetch(client, url))
            except Exception as exc:  # noqa: BLE001 — registra e segue
                skipped.append({"url": url, "error": str(exc)})
                return
            # Formato Confluence esperado por mirror/import_tdn.py
            pages.append({
                "id": url[len(base):].removesuffix(".html") or "index",
                "title": title,
                "_links": {"base": "https://api.fluig.com", "webui": url},
                "body": {"storage": {"value": body}},
                "version": {"number": 1},
            })
            done = len(pages) + len(skipped)
            if done % 50 == 0 or done == len(targets):
                print(f"  {done}/{len(targets)} (erros: {len(skipped)})")

        with ThreadPoolExecutor(WORKERS) as pool:
            list(pool.map(export, targets))

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({
        "exported_at": datetime.now(timezone.utc).isoformat(),
        "origin": base,
        "pages": sorted(pages, key=lambda p: p["id"]),
        "skipped": skipped,
    }, ensure_ascii=False), encoding="utf-8")
    print(f"✓ {out} — {len(pages)} páginas, {len(skipped)} erros")
    print(f"  Importar: .venv/bin/python tools/sync.py import-tdn \"{out}\" --source {source_id}")
    return 1 if skipped and not pages else 0


if __name__ == "__main__":
    raise SystemExit(main())
