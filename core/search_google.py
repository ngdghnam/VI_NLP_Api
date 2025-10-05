import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from googleapiclient.discovery import build
from config.env import settings

class SearchingGoogle: 
    def __init__(self):
        self.apiKey = settings.GOOGLE_CUSTOM_SEARCH_API_KEY
        self.cseId = settings.CUSTOM_SEARCH_ENGINE_ID
        self.service = build("customsearch", "v1", developerKey=self.apiKey)


    def google_search(self, query, num_results=10):
        result = self.service.cse().list(q=query, cx=self.cseId, num=num_results).execute()
        items = result.get('items', [])
        return [{'title': item.get('title', ''), 'link': item.get('link', '')} for item in items]

if __name__ == "__main__":
    searchingGoogle = SearchingGoogle()
    search_results = searchingGoogle.google_search("Son Tung MTP")
    for item in search_results:
        # print(f"Title: {item['title']}")
        # print(f"Link: {item['link']}")
        # print("-" * 20)
        print(item)