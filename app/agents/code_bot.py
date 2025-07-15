import requests
from app.core.config import config
from urllib.parse import quote_plus

class CodeBot:
    def __init__(self):
        self.base_url = "https://api.stackexchange.com/2.3"
        self.timeout = config.TIMEOUT

    async def search_stackoverflow(self, query: str) -> list:
        """جستجوی سوالات در StackOverflow"""
        try:
            params = {
                "order": "desc",
                "sort": "relevance",
                "q": quote_plus(query),
                "site": "stackoverflow",
                "pagesize": config.MAX_RESULTS,
                "key": config.STACK_KEY
            }
            
            response = requests.get(
                f"{self.base_url}/search/advanced",
                params=params,
                timeout=self.timeout
            )
            response.raise_for_status()
            
            return [
                {
                    "title": item["title"],
                    "url": item["link"],
                    "score": item["score"]
                } for item in response.json().get("items", [])
            ]
            
        except Exception as e:
            raise Exception(f"StackOverflow API Error: {str(e)}")

    async def answer(self, input: dict) -> dict:
        """متد اصلی برای پاسخ به سوالات برنامه‌نویسی"""
        try:
            results = await self.search_stackoverflow(input["question"])
            
            if not results:
                return {
                    "topic": "code",
                    "answer": "هیچ نتیجه‌ای در StackOverflow یافت نشد",
                    "source": None
                }
                
            return {
                "topic": "code",
                "answer": results,
                "source": "StackExchange"
            }
            
        except Exception as e:
            return {
                "topic": "code",
                "answer": f"خطا در دریافت پاسخ: {str(e)}",
                "source": None
            }

from app.core.config import config
import requests

class CodeBot:
    async def search_stackoverflow(self, query):
        params = {
            "key": config.STACK_KEY,
            "q": query,
            "site": "stackoverflow"
        }
        response = requests.get(
            "https://api.stackexchange.com/2.3/search",
            params=params,
            timeout=config.TIMEOUT
        )
        return response.json()