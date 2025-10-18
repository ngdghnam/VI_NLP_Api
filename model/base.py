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
    requestedAt: Mapped[datetime | None] = mapped_column(DateTime, default=datetime.utcnow)
    requestedIp: Mapped[str | None] = mapped_column(String(100))
    isDeleted: Mapped[bool] = mapped_column(Boolean, default=False)
    updatedAt: Mapped[datetime | None] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    updatedBy: Mapped[str | None] = mapped_column(String(100))
