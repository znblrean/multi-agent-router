import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

def google_search(query: str, max_results=3):
    try:
        url = f"https://www.google.com/search?q={quote_plus(query)}"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        return [
            {"title": a.text, "url": a['href']}
            for g in soup.find_all('div', class_='g') 
            if (a := g.find('a')) 
            and 'href' in a.attrs
            and not a['href'].startswith('/search?')
        ][:max_results]
    
    except Exception as e:
        raise Exception(f"خطای scraping: {str(e)}")