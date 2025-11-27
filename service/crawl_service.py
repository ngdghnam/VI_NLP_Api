from dto.requestCrawlDto import RequestCrawlDto, MultipleKeywordsDto, UrlDto
from repository.user_repository import UserRepository
from core.search_google import SearchingGoogle
from constant.index import NULL_QUERY
from utils.crawlUtils import CrawlUtils
from config.logger import logger
from database.database import database
from model.user import User
import asyncio
from core.crawl import crawl_sync, crawl_one

class CrawlService: 
    def __init__(self, userRepo: UserRepository, search: SearchingGoogle, crawlUtils: CrawlUtils):
        self.userRepo = userRepo
        self.search = search
        self.crawlUtils = crawlUtils 
        self.crawled_urls = set()

    async def crawlFromSpecificURL(self, data: UrlDto):
        if data.url == "":
            return {"message": NULL_QUERY}

        res = await crawl_one(data.url)
        return res

    async def crawlData(self, request: RequestCrawlDto, skip_duplicates: bool = True):
        if request.query == "":
            return {"message": NULL_QUERY}
        
        links = self.search.google_search(request.query, request.number)
        # Lấy danh sách URL từ dict
        urls = [item["link"] for item in links if item.get("link")]

        # Lọc URL hợp lệ
        valid_links = [
            url for url in urls
            if isinstance(url, str) and url.startswith(("http://", "https://")) and url.strip() != ""
        ]

        # Lọc bỏ URLs đã crawl (nếu bật skip_duplicates)
        if skip_duplicates:
            new_links = [url for url in valid_links if url not in self.crawled_urls]
            logger.info(f"Tìm thấy {len(valid_links)} URLs, {len(new_links)} URLs mới")
            valid_links = new_links

        if not valid_links:
            logger.warning("Không có URL mới để crawl")
            return {"message": "Không có URL mới để crawl", "data": []}
        
        # Chạy crawl trong thread
        results = await asyncio.to_thread(crawl_sync, valid_links)

        # Lưu URLs đã crawl
        if skip_duplicates:
            self.crawled_urls.update(valid_links)

        # Trả về mảng các object thay vì string
        return {"data": self.crawlUtils.combineResultBase(results)}
    
    def extractToFind(number: int):
        return
    
    async def crawlMultipleData(self, data: MultipleKeywordsDto):
        """
        Crawl dữ liệu cho nhiều keywords và gộp tất cả kết quả lại
        """
        if not data.keywords or len(data.keywords) == 0:
            logger.error("Danh sách keywords trống")
            return {"message": "Danh sách keywords không được để trống", "data": []}
        
        all_results = []
        
        # Crawl từng keyword
        for keyword in data.keywords:
            logger.info(f"Đang crawl keyword: {keyword}")
            
            # Tạo RequestCrawlDto cho từng keyword
            request = RequestCrawlDto(
                query=keyword,
                number=10
            )
            
            # Gọi hàm crawlData cho từng keyword
            result = await self.crawlData(request, skip_duplicates=True)
            
            # result["data"] là string từ combineResultBase
            if result.get("data"):
                # Thêm header keyword vào đầu markdown
                keyword_section = f"\n\n{'='*10}\n## KEYWORD: {keyword}\n{'='*10}\n\n"
                all_results.append(keyword_section + result["data"])
        
        if not all_results:
            logger.warning("Không có dữ liệu nào được crawl")
            return {"message": "Không tìm thấy dữ liệu cho các keywords", "data": ""}
        
        # Gộp tất cả kết quả thành một chuỗi markdown
        combined_markdown = "\n".join(all_results)
        self.crawled_urls.clear()

        return {
            "message": f"Đã crawl thành công từ {len(data.keywords)} keywords",
            "keywords": data.keywords,
            "data": combined_markdown
        }

session = next(database.get_db())  # Lấy session từ Database class
userRepo = UserRepository(session, User)
search = SearchingGoogle()
crawlUtils = CrawlUtils()    
crawlService = CrawlService(userRepo, search, crawlUtils)
