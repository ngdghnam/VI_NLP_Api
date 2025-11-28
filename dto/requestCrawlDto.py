from pydantic import BaseModel
from typing import Optional
class RequestCrawlDto(BaseModel): 
    query: str
    number: Optional[int] = 5

class MultipleKeywordsDto(BaseModel):
    keywords: list[str]

class UrlDto(BaseModel):
    url: str