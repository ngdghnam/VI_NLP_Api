from .base import BaseEntity
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User

class SearchHistoryEntity(BaseEntity):
    __tablename__ = "search_history"
    content: Mapped[str] = mapped_column(String(255))
    userId: Mapped[str] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="search_histories")