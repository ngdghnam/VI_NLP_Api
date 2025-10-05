from pydantic import BaseModel
class RequestCrawlDto(BaseModel): 
    query: str
    number: int
