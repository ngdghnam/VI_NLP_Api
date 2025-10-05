from dto.requestCrawlDto import RequestCrawlDto
from repository.user_repository import UserRepository
from core.search_google import SearchingGoogle
from constant.index import NULL_QUERY
from utils.crawlUtils import CrawlUtils
from config.logger import logger
from database.database import database
from model.user import User

class CrawlService: 
    def __init__(self, userRepo: UserRepository, search: SearchingGoogle, crawlUtils: CrawlUtils):
        self.userRepo = userRepo
        self.search = search
        self.crawlUtils = crawlUtils 

    async def crawlData(self, request: RequestCrawlDto):
        if request.query == "":
            logger.error()
            return {"message": NULL_QUERY}
        
        # keywords = await self.crawlUtils.splitKeywords(request.query)

        return self.search.google_search(request.query, request.number)

session = next(database.get_db())  # Lấy session từ Database class
userRepo = UserRepository(session, User)
search = SearchingGoogle()
crawlUtils = CrawlUtils()    
crawlService = CrawlService(userRepo, search, crawlUtils)
