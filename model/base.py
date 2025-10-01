from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, UUID, DateTime

Base = declarative_base()

class BaseEntity(Base):
    __abstract__ = True 
    id = Column(UUID, primary_key=True)
    requestedAt = Column(DateTime)
    requestedIp = Column(String(100))