from adapters.datamappers.shortcut import shortcut_entity_to_model, shortcut_model_to_entity
from adapters.models.shortcut import ShortcutModel
from domain.entities.shortcut import ShortcutEntity
from domain.ports.shortcut_repository import ShortcutRepository

from .base import SqlaBaseRepository

from sqlalchemy.future import select


class SqlaShortcutRepository(SqlaBaseRepository, ShortcutRepository):
    async def create(self, entity: ShortcutEntity):
        model = shortcut_entity_to_model(entity)
        self.session.add(model)

    async def get_by_pk(self, pk: str) -> ShortcutEntity | None:
        shortcut_model = await self.session.scalar(select(ShortcutModel).where(ShortcutModel.pk == pk))

        if shortcut_model is None:
            return None

        shortcut_entity = shortcut_model_to_entity(shortcut_model)

        return shortcut_entity

    async def get_all(self) -> list[ShortcutEntity]:
        shortcut_models = await self.session.scalars(select(ShortcutModel))
        shortcut_entities = [shortcut_model_to_entity(model) for model in shortcut_models]

        return shortcut_entities
