from dataclasses import dataclass

from domain.entities.shortcut import ShortcutEntity
from domain.ports.committer import Committer
from domain.ports.shortcut_repository import ShortcutRepository

from .base import BaseCase


@dataclass(kw_only=True)
class CreateShortcutCase(BaseCase[ShortcutEntity]):
    shortcut_repository: ShortcutRepository
    committer: Committer

    async def __call__(self, url: str):
        """
        Create Shortcut
        """

        shortcut_entity = ShortcutEntity.create(url)
        await self.shortcut_repository.create(shortcut_entity)
        await self.committer.commit()

        return shortcut_entity
