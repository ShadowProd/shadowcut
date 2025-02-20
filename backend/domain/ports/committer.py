from typing import Protocol


class Committer(Protocol):
    async def commit(self, *args, **kwargs) -> None:
        raise NotImplementedError
