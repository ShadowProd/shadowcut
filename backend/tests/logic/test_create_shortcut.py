from domain.cases.create_shortcut import CreateShortcutCase
from tests.mocks.committer import DummyCommitter
from tests.mocks.repositories.shortcut import DummyShortcutRepository

from faker import Faker


async def test_create_shortcut(faker: Faker):
    shortcut_repository = DummyShortcutRepository()
    create_shortcut_case = CreateShortcutCase(shortcut_repository=shortcut_repository, committer=DummyCommitter())

    url = faker.url()
    user_entity = await create_shortcut_case(url=url)

    # Check if shortcut URL is correct.
    assert user_entity.url == url
    # Check if shortcut was created and retrieved successfully.
    assert await shortcut_repository.get_by_pk(user_entity.pk) is not None
