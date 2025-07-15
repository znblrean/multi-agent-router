import requests
from app.config.proxy_config import PROXY_CONFIG

def test_proxy_connection():
    try:
        response = requests.get(
            "http://ipinfo.io/json",
            proxies=PROXY_CONFIG,
            timeout=10
        )
        assert response.status_code == 200
        print("پروکسی کار می‌کند. IP شما:", response.json()["ip"])
    except Exception as e:
        assert False, f"خطا در اتصال پروکسی: {str(e)}"