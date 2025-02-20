from .base import BaseModel

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy_utils import URLType


class ShortcutModel(BaseModel):
    pk: Mapped[str] = mapped_column(String(64), primary_key=True)
    url: Mapped[str] = mapped_column(URLType())

    __tablename__ = 'shortcuts'
