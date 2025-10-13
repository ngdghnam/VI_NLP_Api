from dto.requestCrawlDto import RequestCrawlDto
from repository.user_repository import UserRepository
from core.search_google import SearchingGoogle
from constant.index import NULL_QUERY
from utils.crawlUtils import CrawlUtils
from config.logger import logger
from database.database import database
from model.user import User
import asyncio
from core.crawl import main, crawl_sync

class CrawlService: 
    def __init__(self, userRepo: UserRepository, search: SearchingGoogle, crawlUtils: CrawlUtils):
        self.userRepo = userRepo
        self.search = search
        self.crawlUtils = crawlUtils 

    async def crawlData(self, request: RequestCrawlDto):
        if request.query == "":
            logger.error("Không thể tìm kiếm khi không có từ khóa")
            return {"message": NULL_QUERY}
        
        links = self.search.google_search(request.query, request.number)
        print("Links:", links)
        # Lấy danh sách URL từ dict
        urls = [item["link"] for item in links if item.get("link")]

        # Lọc URL hợp lệ
        valid_links = [
            url for url in urls
            if isinstance(url, str) and url.startswith(("http://", "https://")) and url.strip() != ""
        ]


        if not valid_links:
            logger.error("Không có URL hợp lệ để crawl")
            return {"message": "Không có URL hợp lệ để crawl"}

        # Chạy crawl trong thread
        results = await asyncio.to_thread(crawl_sync, valid_links)

        return {"data": self.crawlUtils.combineResult(results)}
    
    def extractToFind(number: int):
        pass



session = next(database.get_db())  # Lấy session từ Database class
userRepo = UserRepository(session, User)
search = SearchingGoogle()
crawlUtils = CrawlUtils()    
crawlService = CrawlService(userRepo, search, crawlUtils)
