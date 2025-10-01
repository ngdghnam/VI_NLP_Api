from pydantic import BaseModel

class User(BaseModel): 
    ip_address: str