import asyncio
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, DefaultMarkdownGenerator

# config = CrawlerRunConfig(
#     markdown_generator=DefaultMarkdownGenerator(

#     )
# )

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
