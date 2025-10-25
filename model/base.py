from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, DateTime, Boolean
from uuid import uuid4
import uuid

class Base(DeclarativeBase):
    pass

class BaseEntity(Base):
    __abstract__ = True

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid4)
    requestedAt: Mapped[datetime | None] = mapped_column(DateTime, default=datetime.utcnow, nullable=True)
    requestedIp: Mapped[str | None] = mapped_column(String(100),  nullable=True)
    createdAt: Mapped[datetime | None] = mapped_column(DateTime, default=datetime.utcnow)
    isDeleted: Mapped[bool] = mapped_column(Boolean, default=False)
    updatedAt: Mapped[datetime | None] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    updatedBy: Mapped[str | None] = mapped_column(String(100),  nullable=True)
