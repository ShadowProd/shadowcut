import abc
from typing import Generic, TypeVar

T = TypeVar('T')


class BaseCase(abc.ABC, Generic[T]):
    @abc.abstractmethod
    async def __call__(self) -> T:
        raise NotImplementedError
