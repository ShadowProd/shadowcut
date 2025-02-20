from dataclasses import dataclass

from .base import ApplicationException


@dataclass(frozen=True)
class ShortcutNotFound(ApplicationException):
    pk: str

    @property
    def message(self):
        return f'Shortcut {self.pk} is not found'
