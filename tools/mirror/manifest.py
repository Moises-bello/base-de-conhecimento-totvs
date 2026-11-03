from __future__ import annotations

import hashlib
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


@dataclass
class ResourceRecord:
    url: str
    source_id: str
    file_path: str
    content_hash: str
    etag: Optional[str]
    last_modified: Optional[str]
    content_length: Optional[int]
    status_code: int
    fetched_at: str


class Manifest:
    def __init__(self, db_path: Path) -> None:
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(self.db_path)
        self._conn.row_factory = sqlite3.Row
        self._init_schema()

    def _init_schema(self) -> None:
        self._conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS resources (
                url TEXT PRIMARY KEY,
                source_id TEXT NOT NULL,
                file_path TEXT NOT NULL,
                content_hash TEXT NOT NULL,
                etag TEXT,
                last_modified TEXT,
                content_length INTEGER,
                status_code INTEGER,
                fetched_at TEXT NOT NULL
            );
            CREATE INDEX IF NOT EXISTS idx_resources_source ON resources(source_id);
            CREATE TABLE IF NOT EXISTS sync_runs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source_id TEXT NOT NULL,
                started_at TEXT NOT NULL,
                finished_at TEXT,
                downloaded INTEGER DEFAULT 0,
                skipped INTEGER DEFAULT 0,
                errors INTEGER DEFAULT 0
            );
            """
        )
        self._conn.commit()

    def get(self, url: str) -> Optional[ResourceRecord]:
        row = self._conn.execute(
            "SELECT * FROM resources WHERE url = ?", (url,)
        ).fetchone()
        if not row:
            return None
        return ResourceRecord(**dict(row))

    def upsert(self, record: ResourceRecord) -> None:
        self._conn.execute(
            """
            INSERT INTO resources (
                url, source_id, file_path, content_hash, etag,
                last_modified, content_length, status_code, fetched_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(url) DO UPDATE SET
                source_id = excluded.source_id,
                file_path = excluded.file_path,
                content_hash = excluded.content_hash,
                etag = excluded.etag,
                last_modified = excluded.last_modified,
                content_length = excluded.content_length,
                status_code = excluded.status_code,
                fetched_at = excluded.fetched_at
            """,
            (
                record.url,
                record.source_id,
                record.file_path,
                record.content_hash,
                record.etag,
                record.last_modified,
                record.content_length,
                record.status_code,
                record.fetched_at,
            ),
        )
        self._conn.commit()

    def start_run(self, source_id: str) -> int:
        cur = self._conn.execute(
            "INSERT INTO sync_runs (source_id, started_at) VALUES (?, ?)",
            (source_id, utc_now()),
        )
        self._conn.commit()
        return int(cur.lastrowid)

    def finish_run(
        self, run_id: int, downloaded: int, skipped: int, errors: int
    ) -> None:
        self._conn.execute(
            """
            UPDATE sync_runs
            SET finished_at = ?, downloaded = ?, skipped = ?, errors = ?
            WHERE id = ?
            """,
            (utc_now(), downloaded, skipped, errors, run_id),
        )
        self._conn.commit()

    def iter_all(self) -> list[ResourceRecord]:
        rows = self._conn.execute(
            "SELECT * FROM resources ORDER BY source_id, url"
        ).fetchall()
        return [ResourceRecord(**dict(row)) for row in rows]

    def stats(self, source_id: str | None = None) -> dict:
        if source_id:
            row = self._conn.execute(
                "SELECT COUNT(*) as total FROM resources WHERE source_id = ?",
                (source_id,),
            ).fetchone()
        else:
            row = self._conn.execute(
                "SELECT COUNT(*) as total FROM resources"
            ).fetchone()
        return {"total_resources": row["total"]}

    def close(self) -> None:
        self._conn.close()


def content_hash(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()
