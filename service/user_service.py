from model.user import User
from repository.user_repository import UserRepository
from database.database import database
from constant.index import CREATE_SUCCESS
from uuid import uuid4
from dto.createUserDto import CreateUserDto
from datetime import date

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def create(self, user, data: CreateUserDto):
        entity = User()
        entity.id = uuid4()
        entity.email = data.email
        entity.name = data.name
        entity.message = data.message
        entity.phone_number = data.phone_number
        entity.createdAt = date.today()

        await self.repo.insert(entity)

        return {"message": CREATE_SUCCESS}
    
    async def getUsers(self):
        return await self.repo.find
        
session = next(database.get_db())  # Lấy session từ Database class
userRepo = UserRepository(session, User)
userService = UserService()