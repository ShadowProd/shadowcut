from dataclasses import dataclass

from domain.entities.shortcut import ShortcutEntity
from domain.exceptions.shortcut_not_found import ShortcutNotFound
from domain.ports.committer import Committer
from domain.ports.shortcut_repository import ShortcutRepository

from .base import BaseCase


@dataclass(kw_only=True)
class GetShortcutByPkCase(BaseCase[ShortcutEntity]):
    shortcut_repository: ShortcutRepository
    committer: Committer

    async def __call__(self, pk: str):
        """
        Get Shortcut By Primary Key

        Raises:
            ShortcutNotFound: Shortcut is not found
        """

        entity = await self.shortcut_repository.get_by_pk(pk)

        if not entity:
            raise ShortcutNotFound(pk)

        return entity
