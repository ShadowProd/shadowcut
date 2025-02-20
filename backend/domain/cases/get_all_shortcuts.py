from dataclasses import dataclass

from domain.entities.shortcut import ShortcutEntity
from domain.enums.role import RoleEnum
from domain.ports.identity_provider import IdentityProvider
from domain.ports.shortcut_repository import ShortcutRepository

from .base import BaseCase


@dataclass(kw_only=True)
class GetAllShortcutsCase(BaseCase[list[ShortcutEntity]]):
    shortcut_repository: ShortcutRepository
    identity_provider: IdentityProvider

    async def __call__(self):
        """
        Get All Shortcuts

        Raises:
            PermissionError: Admin is required
        """

        role = await self.identity_provider.get_role()

        if role != RoleEnum.ADMIN:
            raise PermissionError('Admin is required')

        shortcut_entities = await self.shortcut_repository.get_all()
        return shortcut_entities
