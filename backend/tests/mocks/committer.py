import logging

from domain.ports.committer import Committer

logger = logging.getLogger(__name__)


class DummyCommitter(Committer):
    async def commit(self, *args, **kwargs) -> None:
        logger.info('Committing changes...')
