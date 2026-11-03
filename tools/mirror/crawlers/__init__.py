from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

from mirror.http_client import SyncStats


@dataclass
class CrawlerConfig:
    source_id: str
    config: dict
    data_dir: str
    force: bool = False


class BaseCrawler(ABC):
    def __init__(self, crawler_config: CrawlerConfig) -> None:
        self.cfg = crawler_config

    @abstractmethod
    def run(self) -> SyncStats:
        ...
