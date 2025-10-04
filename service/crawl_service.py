from dto.requestCrawlDto import RequestCrawlDto
from repository.user_repository import UserRepository
from core.search_google import searchingGoogle
from constant.index import NULL_QUERY
from utils.crawlUtils import CrawlUtils

class CrawlService: 
    def __init__(self, userRepo: UserRepository, search: searchingGoogle, crawlUtils: CrawlUtils):
        self.userRepo = userRepo
        self.search = search
        self.crawlUtils = crawlUtils

    def crawlData(self, request: RequestCrawlDto):
        if request.query == "":
            return {"message": NULL_QUERY}
        
