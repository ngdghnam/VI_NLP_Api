from .base import BaseEntity
from sqlalchemy import Column, Integer, String, UUID, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .search_history import SearchHistoryEntity

class User(BaseEntity):
    __tablename__ = "users"
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100))
    phone_number: Mapped[str] = mapped_column(String(10))
    message: Mapped[str] = mapped_column(String(255), nullable=True)
    search_histories: Mapped[List["SearchHistoryEntity"]] = relationship(back_populates="user")
    