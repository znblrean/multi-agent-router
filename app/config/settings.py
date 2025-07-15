import os
from dotenv import load_dotenv

load_dotenv()  # بارگذاری متغیرهای .env

class Settings:
    # API Keys
    WOLFRAM_ALPHA_KEY = os.getenv("WOLFRAM_ALPHA_API_KEY")
    SERPAPI_KEY = os.getenv("SERPAPI_KEY")
    
    # تنظیمات پروکسی
    PROXIES = {
        "http": os.getenv("HTTP_PROXY"),
        "https": os.getenv("HTTPS_PROXY")
    }

settings = Settings()