from __future__ import annotations

import re
import time
from dataclasses import dataclass, field
from typing import Optional
from urllib.parse import urljoin, urlparse

import httpx

from mirror.manifest import Manifest, ResourceRecord, content_hash, utc_now


SKIP_EXTENSIONS = {
    ".jpg", ".jpeg", ".png", ".gif", ".webp", ".ico", ".svg",
    ".woff", ".woff2", ".ttf", ".eot", ".mp4", ".webm",
}


@dataclass
class SyncStats:
    downloaded: int = 0
    skipped: int = 0
    errors: int = 0


@dataclass
class FetchResult:
    action: str  # downloaded | skipped | error
    url: str
    message: str = ""


class HttpFetcher:
    def __init__(
        self,
        manifest: Manifest,
        source_id: str,
        output_dir: str,
        rate_limit: float = 0.5,
        timeout: float = 30.0,
        user_agent: str = "FluigDocsMirror/1.0 (+local backup)",
    ) -> None:
        self.manifest = manifest
        self.source_id = source_id
        self.output_dir = output_dir
        self.rate_limit = rate_limit
        self.client = httpx.Client(
            timeout=timeout,
            follow_redirects=True,
            headers={"User-Agent": user_agent},
        )

    def close(self) -> None:
        self.client.close()

    def _local_path(self, url: str) -> str:
        parsed = urlparse(url)
        path = parsed.path.lstrip("/")
        if not path or path.endswith("/"):
            path = f"{path}index.html"
        if parsed.query:
            safe_query = re.sub(r"[^\w.-]", "_", parsed.query)[:80]
            path = f"{path}__{safe_query}"
        return f"{self.output_dir}/{parsed.netloc}/{path}"

    def _headers_unchanged(
        self,
        record: ResourceRecord,
        etag: Optional[str],
        last_modified: Optional[str],
    ) -> bool:
        if etag and record.etag and etag == record.etag:
            return True
        if (
            last_modified
            and record.last_modified
            and last_modified == record.last_modified
        ):
            return True
        return False

    def fetch(self, url: str, force: bool = False) -> FetchResult:
        time.sleep(self.rate_limit)
        existing = self.manifest.get(url)

        try:
            head = self.client.head(url)
            etag = head.headers.get("etag")
            last_modified = head.headers.get("last-modified")
            content_length = head.headers.get("content-length")
            cl_int = int(content_length) if content_length else None

            if (
                not force
                and existing
                and head.status_code == 200
                and self._headers_unchanged(existing, etag, last_modified)
            ):
                self.manifest.upsert(
                    ResourceRecord(
                        url=url,
                        source_id=self.source_id,
                        file_path=existing.file_path,
                        content_hash=existing.content_hash,
                        etag=etag or existing.etag,
                        last_modified=last_modified or existing.last_modified,
                        content_length=cl_int or existing.content_length,
                        status_code=head.status_code,
                        fetched_at=utc_now(),
                    )
                )
                return FetchResult("skipped", url)

            response = self.client.get(url)
            response.raise_for_status()
            data = response.content
            digest = content_hash(data)

            if not force and existing and existing.content_hash == digest:
                self.manifest.upsert(
                    ResourceRecord(
                        url=url,
                        source_id=self.source_id,
                        file_path=existing.file_path,
                        content_hash=digest,
                        etag=response.headers.get("etag") or existing.etag,
                        last_modified=response.headers.get("last-modified")
                        or existing.last_modified,
                        content_length=len(data),
                        status_code=response.status_code,
                        fetched_at=utc_now(),
                    )
                )
                return FetchResult("skipped", url)

            file_path = self._local_path(url)
            from pathlib import Path

            dest = Path(file_path)
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)

            self.manifest.upsert(
                ResourceRecord(
                    url=url,
                    source_id=self.source_id,
                    file_path=file_path,
                    content_hash=digest,
                    etag=response.headers.get("etag"),
                    last_modified=response.headers.get("last-modified"),
                    content_length=len(data),
                    status_code=response.status_code,
                    fetched_at=utc_now(),
                )
            )
            return FetchResult("downloaded", url)

        except httpx.HTTPError as exc:
            return FetchResult("error", url, str(exc))
