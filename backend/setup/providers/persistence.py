from typing import AsyncIterable

from adapters.repositories.shortcut import SqlaShortcutRepository
from domain.ports.committer import Committer
from domain.ports.shortcut_repository import ShortcutRepository
from settings import Settings

from dishka import Provider, Scope, alias, provide
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine


class PersistenceProvider(Provider):
    scope = Scope.REQUEST

    @provide(scope=Scope.APP)
    def get_engine(self, settings: Settings) -> AsyncEngine:
        return create_async_engine(str(settings.database_dsn), echo=False, pool_recycle=180)

    @provide(scope=Scope.APP)
    def get_session_maker(self, engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
        return async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    @provide
    async def get_session(self, factory: async_sessionmaker[AsyncSession]) -> AsyncIterable[AsyncSession]:
        session = factory()

        yield session

        await session.close()

    committer = alias(AsyncSession, provides=Committer)

    @provide
    def get_shortcut_repository(self, session: AsyncSession) -> ShortcutRepository:
        return SqlaShortcutRepository(session)
