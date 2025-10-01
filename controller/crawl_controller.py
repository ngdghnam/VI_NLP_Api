from fastapi import APIRouter
from dto.requestCrawlDto import RequestCrawlDto

router = APIRouter(
    prefix="/crawling-data",
    tags=["Crawling Data"]
)

@router.post("/crawl")
def crawlData(request: RequestCrawlDto):
    pass