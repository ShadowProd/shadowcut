from adapters.models.shortcut import ShortcutModel
from domain.entities.shortcut import ShortcutEntity


def shortcut_entity_to_model(entity: ShortcutEntity) -> ShortcutModel:
    return ShortcutModel(pk=entity.pk, url=entity.url)


def shortcut_model_to_entity(model: ShortcutModel) -> ShortcutEntity:
    return ShortcutEntity(pk=model.pk, url=model.url)
