import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, DefaultMarkdownGenerator
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
from crawl4ai.deep_crawling import DFSDeepCrawlStrategy

browser_config = BrowserConfig(verbose=True) # verbose for logging
strategy = DFSDeepCrawlStrategy(
    max_depth=2,               # Crawl initial page + 2 levels deep
    include_external=False,    # Stay within the same domain
    max_pages=2,              # Maximum number of pages to crawl (optional)
    score_threshold=0.5,       # Minimum score for URLs to be crawled (optional)
)

markDownConfig = DefaultMarkdownGenerator(
    options={

    }
)

config = CrawlerRunConfig(
    markdown_generator=markDownConfig,
    max_depth=1
)

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
