from .base import BaseEntity

class User(BaseEntity): 
    __tablename__ = "users"
    data_search: str # lịch sử tìm kiếm