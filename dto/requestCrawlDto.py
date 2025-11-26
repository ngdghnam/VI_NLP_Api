from pydantic import BaseModel
from typing import Optional
class RequestCrawlDto(BaseModel): 
    query: str
    number: Optional[int] = None

class MultipleKeywordsDto(BaseModel):
    keywords: list[str]