from adapters.identity_provider import CookieKeyIdentityProvider
from domain.ports.identity_provider import IdentityProvider
from settings import Settings

from dishka import Scope, provide
from dishka.integrations.fastapi import FastapiProvider
from fastapi import Request


class AuthProvider(FastapiProvider):
    scope = Scope.REQUEST

    @provide
    def get_identity_provider(self, request: Request, settings: Settings) -> IdentityProvider:
        return CookieKeyIdentityProvider(request=request, admin_key=settings.admin_key)
