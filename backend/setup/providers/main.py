from domain.cases.create_shortcut import CreateShortcutCase
from domain.cases.get_all_shortcuts import GetAllShortcutsCase
from domain.cases.get_shortcut_by_pk import GetShortcutByPkCase
from settings import Settings

from dishka import Provider, Scope, from_context, provide


class MainProvider(Provider):
    scope = Scope.REQUEST

    settings = from_context(Settings, scope=Scope.APP)
    create_shortcut_case = provide(CreateShortcutCase)
    get_shortcut_by_pk_case = provide(GetShortcutByPkCase)
    get_all_shortcuts_case = provide(GetAllShortcutsCase)
