import abc

from domain.enums.role import RoleEnum


class IdentityProvider(abc.ABC):
    @abc.abstractmethod
    async def get_role(self) -> RoleEnum:
        raise NotImplementedError
