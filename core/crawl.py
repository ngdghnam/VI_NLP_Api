import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, DefaultMarkdownGenerator
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
from crawl4ai.deep_crawling import DFSDeepCrawlStrategy
import re

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
        "include_links": False,
        "include_images": False,
        "include_tables": True,
        "strip_metadata": True,
        "text_only": True,
    }
)


config = CrawlerRunConfig(
    markdown_generator=markDownConfig,
    # Chỉ lấy nội dung từ thẻ article hoặc main
    css_selector="article, main, .content, .post-content, .article-content",
    # Loại bỏ các phần không cần thiết
    excluded_tags=['nav', 'footer', 'header', 'aside', 'script', 'style'],
    remove_overlay_elements=True,
)


def clean_content(markdown: str) -> str:
    """
    Làm sạch markdown, loại bỏ links và content không cần thiết
    """
    # Loại bỏ markdown links [text](url)
    cleaned = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', markdown)
    
    # Loại bỏ URLs đơn thuần
    cleaned = re.sub(r'https?://[^\s]+', '', cleaned)
    
    # Loại bỏ email
    cleaned = re.sub(r'\S+@\S+', '', cleaned)
    
    # Loại bỏ nhiều dòng trống liên tiếp
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
    
    # Loại bỏ các dòng chỉ chứa ký tự đặc biệt
    lines = [line for line in cleaned.split('\n') 
             if line.strip() and not re.match(r'^[\s\-_*#]+$', line)]
    
    return '\n'.join(lines).strip()

async def crawl_one(url: str):
    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(url, config=config)
        raw_markdown = result.markdown or ""
        # Làm sạch content
        return clean_content(raw_markdown)
    
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
        # print(result.markdown)
        return result 

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
