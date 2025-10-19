from pydantic import BaseModel
from typing import Optional

class UserDto(BaseModel):
    id: str 
    ip: str
    