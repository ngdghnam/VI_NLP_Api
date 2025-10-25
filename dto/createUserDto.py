from pydantic import BaseModel
from typing import Optional

class CreateUserDto(BaseModel):
    name: str
    email: str 
    phone_number: str
    message: Optional[str] = None