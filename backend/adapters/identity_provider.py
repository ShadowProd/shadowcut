from domain.enums.role import RoleEnum
from domain.ports.identity_provider import IdentityProvider

from fastapi import Request


class CookieKeyIdentityProvider(IdentityProvider):
    def __init__(self, request: Request, admin_key: str):
        self._request = request
        self._admin_key = admin_key

    async def get_role(self) -> RoleEnum:
        is_admin = self._request.headers.get('Authorization') == self._admin_key

        return RoleEnum.ADMIN if is_admin else RoleEnum.USER
