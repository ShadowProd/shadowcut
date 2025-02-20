from domain.cases.get_all_shortcuts import GetAllShortcutsCase
from domain.enums.role import RoleEnum
from tests.mocks.identity_provider import DummyIdentityProvider
from tests.mocks.repositories.shortcut import DummyShortcutRepository

import pytest


async def test_get_all_shortcuts_as_user():
    shortcut_repository = DummyShortcutRepository()
    identity_provider = DummyIdentityProvider(RoleEnum.USER)
    get_all_shortcuts_case = GetAllShortcutsCase(
        shortcut_repository=shortcut_repository, identity_provider=identity_provider
    )

    # Make sure user is not allowed to retrieve shortcuts.
    with pytest.raises(PermissionError):
        await get_all_shortcuts_case()


async def test_get_all_shortcuts():
    shortcut_repository = DummyShortcutRepository()
    identity_provider = DummyIdentityProvider(RoleEnum.ADMIN)
    get_all_shortcuts_case = GetAllShortcutsCase(
        shortcut_repository=shortcut_repository, identity_provider=identity_provider
    )

    # Check if shortcuts are retrieved successfully.
    assert await shortcut_repository.get_all() == await get_all_shortcuts_case()
