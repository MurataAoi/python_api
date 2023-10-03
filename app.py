import requests
import time

# Hacker News API
Hacker_News_API = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"

# 各ニュースを取得する
news_url = "https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty"

response = requests.get(Hacker_News_API)

top_news_ids = response.json()

for news_id in top_news_ids[:30]:
    get_news_url = news_url.format(news_id)
    news_response = requests.get(get_news_url)

    news_data = news_response.json()

    title = news_data.get("title", "")
    link = news_data.get("url", "")

    print(f"Title: {title}, Link: {link}")

    time.sleep(1)