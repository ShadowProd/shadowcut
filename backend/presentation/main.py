from domain.cases.create_shortcut import CreateShortcutCase
from domain.cases.get_all_shortcuts import GetAllShortcutsCase
from domain.cases.get_shortcut_by_pk import GetShortcutByPkCase
from domain.exceptions.shortcut_not_found import ShortcutNotFound

from .depends_token import DependsToken
from .schemas import CreateShortcutSchema, ExceptionSchema, ShortcutSchema

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import RedirectResponse

main_router = APIRouter(prefix='/shortcuts', tags=['Shortcut your link here'])


@main_router.post('', responses={status.HTTP_201_CREATED: {'model': ShortcutSchema}})
@inject
async def create_shortcut(
    body: CreateShortcutSchema, generate_shortcut: FromDishka[CreateShortcutCase]
) -> ShortcutSchema:
    shortcut_entity = await generate_shortcut(url=str(body.url))
    return ShortcutSchema.from_entity(shortcut_entity)


@main_router.get('', responses={status.HTTP_403_FORBIDDEN: {'model': ExceptionSchema}}, dependencies=[DependsToken])
@inject
async def get_all_shortcuts(get_all_shortcuts: FromDishka[GetAllShortcutsCase]) -> list[ShortcutSchema]:
    try:
        shortcut_entities = await get_all_shortcuts()
    except PermissionError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

    return [ShortcutSchema.from_entity(entity) for entity in shortcut_entities]


@main_router.get('/{pk}', responses={status.HTTP_404_NOT_FOUND: {'model': ExceptionSchema}})
@inject
async def use_shortcut(pk: str, get_shortcut_by_pk: FromDishka[GetShortcutByPkCase]):
    try:
        link_entity = await get_shortcut_by_pk(pk=pk)
    except ShortcutNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return RedirectResponse(url=link_entity.url)
