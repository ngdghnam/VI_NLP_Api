from fastapi import APIRouter
from dto.requestCrawlDto import RequestCrawlDto, MultipleKeywordsDto, UrlDto
from service.crawl_service import crawlService

router = APIRouter(
    prefix="/crawling-data",
    tags=["Crawling Data"]
)

@router.post("/crawl-url")
async def crawlFromSpecificURL(data: UrlDto):
    return await crawlService.crawlFromSpecificURL(data)

@router.post("/crawl")
async def crawlData(request: RequestCrawlDto):
    return await crawlService.crawlData(request)

@router.post("/crawl-multiple")
async def crawlMultipleData(request: MultipleKeywordsDto):
    return await crawlService.crawlMultipleData(request)