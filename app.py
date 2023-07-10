import time
import requests


# Hacker News APIのエンドポイント
url = "https://hacker-news.firebaseio.com/v0/topstories.json"

# トップストーリーのIDを取得
response = requests.get(url)
story_ids = response.json()

# 10件のトップストーリーのタイトルとリンクURLを取得
for story_id in story_ids[:10]:
    story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    story_response = requests.get(story_url)
    story_data = story_response.json()

    title = story_data["title"]
    url = story_data["url"]

    print(f"{{'title': ' {title}', 'link': '{url}'}}")
    print("---")
    time.sleep(1)  # ここで1秒止まる
