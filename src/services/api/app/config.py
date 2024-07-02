from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pendulum import Timezone

from os import environ
from dataclasses import dataclass
from pendulum import timezone
from pydantic import SecretStr


@dataclass
class Config:
    @property
    def FASTAPI_USERS_SECRET(self) -> SecretStr:
        return SecretStr(environ["FASTAPI_USERS_SECRET"])

    @property
    def TSDB_URL(self) -> str:
        return environ["TSDB_URL"]

    @property
    def TSDB_TOKEN(self) -> str:
        return environ["TSDB_TOKEN"]

    @property
    def TSDB_ORG(self) -> str:
        return environ["TSDB_ORG"]

    @property
    def TSDB_BUCKET(self) -> str:
        return environ["TSDB_BUCKET"]

    @property
    def TIMEZONE(self) -> "Timezone":
        return timezone(environ["TIMEZONE"])


CONFIG = Config()
