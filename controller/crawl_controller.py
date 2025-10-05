from fastapi import APIRouter
from dto.requestCrawlDto import RequestCrawlDto
from service.crawl_service import crawlService

router = APIRouter(
    prefix="/crawling-data",
    tags=["Crawling Data"]
)

@router.post("/crawl")
async def crawlData(request: RequestCrawlDto):
    return await crawlService.crawlData(request)
