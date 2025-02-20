from domain.entities.shortcut import ShortcutEntity
from domain.ports.shortcut_repository import ShortcutRepository

from .base import DummyBaseRepository


class DummyShortcutRepository(DummyBaseRepository, ShortcutRepository):
    _entities = []

    async def create(self, entity: ShortcutEntity):
        self._entities.append(entity)

    async def get_by_pk(self, pk: str) -> ShortcutEntity | None:
        for entity in self._entities:
            if entity.pk == pk:
                return entity

    async def get_all(self) -> list[ShortcutEntity]:
        return self._entities
