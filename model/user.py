from .base import BaseEntity
from sqlalchemy import Column, Integer, String, UUID, DateTime, Boolean
from sqlalchemy.orm import Mapped, mapped_column

class User(BaseEntity):
    __tablename__ = "users"
    data_search: Mapped[str] = mapped_column(String(1000))  # lịch sử tìm kiếm