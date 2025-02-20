from domain.enums.role import RoleEnum
from domain.ports.identity_provider import IdentityProvider


class DummyIdentityProvider(IdentityProvider):
    def __init__(self, role: RoleEnum):
        self.role = role

    async def get_role(self) -> RoleEnum:
        return self.role
