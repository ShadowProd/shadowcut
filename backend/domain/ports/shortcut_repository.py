import abc

from domain.entities.shortcut import ShortcutEntity


class ShortcutRepository(abc.ABC):
    @abc.abstractmethod
    async def create(self, entity: ShortcutEntity):
        raise NotImplementedError

    @abc.abstractmethod
    async def get_by_pk(self, pk: str) -> ShortcutEntity | None:
        raise NotImplementedError

    @abc.abstractmethod
    async def get_all(self) -> list[ShortcutEntity]:
        raise NotImplementedError
