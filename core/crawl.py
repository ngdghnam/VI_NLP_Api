import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, DefaultMarkdownGenerator

config = CrawlerRunConfig(
    markdown_generator=DefaultMarkdownGenerator(

    )
)

async def main():
    async with AsyncWebCrawler() as crawler:
        result = await crawler.arun("https://www.ieee.org/")
        print(result.markdown) 

if __name__ == "__main__":
    asyncio.run(main())
