from domain.cases.get_shortcut_by_pk import GetShortcutByPkCase
from domain.entities.shortcut import ShortcutEntity
from tests.mocks.committer import DummyCommitter
from tests.mocks.repositories.shortcut import DummyShortcutRepository


async def test_get_shortcut_by_pk():
    shortcut_repository = DummyShortcutRepository()
    get_shortcut_by_pk_case = GetShortcutByPkCase(shortcut_repository=shortcut_repository, committer=DummyCommitter())

    shortcut_entity = ShortcutEntity(pk='example', url='https://example.com')
    await shortcut_repository.create(shortcut_entity)

    # Test if the shortcut is retrieved correctly.
    assert await get_shortcut_by_pk_case(shortcut_entity.pk) == await shortcut_repository.get_by_pk(shortcut_entity.pk)
