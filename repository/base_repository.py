from typing import TypeVar, Generic, List, Optional, Type
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime

# Generic type cho Entity
T = TypeVar('T')

class BaseRepository(Generic[T]): 
    def __init__(self, session: Session, model: Type[T]):
        """
        Args:
            session: SQLAlchemy Session
            model: Model class (ví dụ: User)
        """
        self.session = session
        self.model = model

    def save(self, entity: T) -> T:
        """
        Lưu entity mới hoặc cập nhật entity hiện tại
        Tự động phát hiện insert hoặc update
        """
        try:
            self.session.add(entity)
            self.session.commit()
            self.session.refresh(entity)
            return entity
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
    
    def insert(self, entity: T) -> T:
        """
        Thêm mới một entity vào database
        """
        try:
            self.session.add(entity)
            self.session.commit()
            self.session.refresh(entity)
            return entity
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def update(self, entity: T) -> T:
        """
        Cập nhật một entity
        """
        try:
            self.session.merge(entity)
            self.session.commit()
            return entity
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
    
    def delete_by_id(self, entity_id) -> bool:
        """
        Xóa mềm entity theo ID (soft delete)
        """
        try:
            entity = self.find_by_id(entity_id)
            if entity:
                if hasattr(entity, 'isDeleted'):
                    entity.isDeleted = True
                    if hasattr(entity, 'deletedAt'):
                        entity.deletedAt = datetime.now()
                    self.session.commit()
                    return True
                else:
                    # Nếu không có trường isDeleted thì xóa cứng
                    self.session.delete(entity)
                    self.session.commit()
                    return True
            return False
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
    
    def find_by_id(self, entity_id) -> Optional[T]:
        """
        Tìm entity theo ID
        author: Hoài Nam
        """
        return self.session.query(self.model).filter(
            self.model.id == entity_id
        ).first() 