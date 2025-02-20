import uuid
from dataclasses import dataclass
from typing import Self

from .base import BaseEntity


@dataclass(kw_only=True)
class ShortcutEntity(BaseEntity):
    pk: str
    url: str

    @staticmethod
    def generate_pk() -> str:
        return str(uuid.uuid4())[:8]

    @classmethod
    def create(cls, url: str) -> Self:
        return cls(pk=cls.generate_pk(), url=url)
