"""Servidor local para receber chunks do TDN exportados pelo console do browser."""

from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path


def run_receiver(output_dir: Path, port: int = 8765, source_id: str = "tdn-fluig") -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    received: list[str] = []

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, fmt, *args):
            print(f"  {args[0]}")

        def _cors(self):
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")

        def do_OPTIONS(self):
            self.send_response(204)
            self._cors()
            self.end_headers()

        def do_POST(self):
            if self.path not in ("/chunk", "/"):
                self.send_response(404)
                self.end_headers()
                return

            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            data = json.loads(body.decode("utf-8"))

            chunk_id = data.get("chunk", str(len(received) + 1).zfill(3))
            filename = f"tdn-chunk-{chunk_id}.json"
            dest = output_dir / filename
            dest.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

            pages = len(data.get("pages", []))
            received.append(filename)
            print(f"✓ {filename} — {pages} páginas (total: {len(received)} arquivos)")

            self.send_response(200)
            self._cors()
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"ok": True, "file": filename}).encode())

        def do_GET(self):
            if self.path == "/status":
                self.send_response(200)
                self._cors()
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                payload = json.dumps({"received": len(received), "files": received})
                self.wfile.write(payload.encode())
            else:
                self.send_response(200)
                self._cors()
                self.end_headers()
                self.wfile.write(b"TDN receiver OK. POST /chunk")

    print(f"\nServidor TDN ({source_id}) em http://localhost:{port}")
    print(f"Salvando em: {output_dir}")
    print("\nNo console do TDN (mesma máquina), rode sendToLocal() do script export.\n")
    print("Ctrl+C para parar.\n")

    server = HTTPServer(("127.0.0.1", port), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print(f"\nEncerrado. {len(received)} arquivos em {output_dir}")
        server.server_close()
