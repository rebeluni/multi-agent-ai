import requests
from bs4 import BeautifulSoup

def get_market_data(keyword):
    url = f"https://news.google.com/search?q={keyword}&hl=en-IN&gl=IN&ceid=IN:en"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    articles = soup.select('article h3 a')
    headlines = []

    for a in articles[:5]:  # Top 5 headlines
        text = a.get_text()
        link = "https://news.google.com" + a['href'][1:]  # remove "./"
        headlines.append(f"- {text}\n  {link}")

    return "\n".join(headlines)
