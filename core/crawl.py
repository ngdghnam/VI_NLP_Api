import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, DefaultMarkdownGenerator
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
from crawl4ai.deep_crawling import DFSDeepCrawlStrategy

# --- Cấu hình trình duyệt ---
browser_config = BrowserConfig(verbose=True)

# --- Cấu hình chiến lược cào ---
strategy = DFSDeepCrawlStrategy(
    max_depth=2,
    include_external=False,
    max_pages=2,
    score_threshold=0.5,
)

# --- Cấu hình Markdown ---
markDownConfig = DefaultMarkdownGenerator(
    options={
        "include_links": False,   # Không lấy link
        "include_images": False,  # Không lấy ảnh
        "include_tables": True,   # Giữ lại bảng nếu có
        "strip_metadata": True,   # Loại bỏ meta
        "text_only": True,        # Chỉ lấy text
    }
)

config = CrawlerRunConfig(
    markdown_generator=markDownConfig,
)

# --- Crawl 1 URL ---
async def crawl_one(url: str):
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url, config=config)
        return result.markdown or ""
    
# --- Cào nhiều URL ---
async def crawl_all(urls: list[str]):
    """
    Cào nhiều URL (chạy async tuần tự)
    Trả về danh sách dict: [{"url": ..., "content": ...}, ...]
    """
    results = []
    for url in urls:
        markdown = await crawl_one(url)
        results.append({
            "url": url,
            "content": markdown
        })

    return results

# --- Hàm sync để gọi trong FastAPI ---
def crawl_sync(urls: list[str]):
    """
    Wrapper sync để dùng trong môi trường FastAPI hoặc code đồng bộ.
    """
    return asyncio.run(crawl_all(urls))

async def main(url):
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun(url)
        print(result.markdown) 

if __name__ == "__main__":
    lstUrls = [
        "https://ibighit.com/bts/eng/", 
        "https://www.instagram.com/bts.bighitofficial/?hl=en",
        "https://www.bts.gov/",
        "https://bts.com/"
    ]
    for url in lstUrls:
        res = asyncio.run(main(url))
        print(f">>> crawling {url}")
        print(res)
        print(">>> Success. Next Turn")
