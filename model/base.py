from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, UUID, DateTime, Boolean

Base = declarative_base()

class BaseEntity(Base):
    __abstract__ = True 
    id = Column(UUID, primary_key=True)
    requestedAt = Column(DateTime)
    requestedIp = Column(String(100))
    isDeleted = Column(Boolean, default=False)
    updatedAt = Column(DateTime)
    updatedBy = Column(String(100))