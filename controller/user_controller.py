from fastapi import APIRouter
from dto.requestCrawlDto import RequestCrawlDto
from service.user_service import userService
from dto.createUserDto import CreateUserDto
from uuid import uuid4

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.post('/create')
async def createData(data: CreateUserDto):
    return await userService.create(data)


@router.get('/get_users')
async def getUsers():
    pass