from dataclasses import dataclass
from typing import Self

from domain.entities.shortcut import ShortcutEntity

from pydantic import BaseModel, HttpUrl


class CreateShortcutSchema(BaseModel):
    url: HttpUrl


class ShortcutSchema(BaseModel):
    pk: str
    url: HttpUrl

    @classmethod
    def from_entity(cls, entity: ShortcutEntity) -> Self:
        return cls(pk=entity.pk, url=HttpUrl(entity.url))


@dataclass(frozen=True, slots=True)
class ExceptionSchema:
    description: str
