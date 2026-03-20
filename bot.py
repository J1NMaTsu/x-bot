import tweepy
from pytrends.request import TrendReq
import os

# GitHubのSecretsから鍵を読み込む
API_KEY = os.environ["API_KEY"]
API_SECRET = os.environ["API_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_SECRET = os.environ["ACCESS_SECRET"]

def get_google_trends():
    pytrends = TrendReq(hl='ja-JP', tz=540)
    df = pytrends.trending_searches(pn='japan')
    return df[0].head(5).tolist()

def post_to_x():
    # X APIに接続
    client = tweepy.Client(
        consumer_key=API_KEY, consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET
    )
    
    trends = get_google_trends()
    status_text = "【現在のトレンドワード】\n\n"
    for i, word in enumerate(trends, 1):
        status_text += f"{i}. {word}\n"
    status_text += "\n#トレンド #まとめ"
    
    # 投稿実行
    client.create_tweet(text=status_text)
    print("Successfully posted!")

if __name__ == "__main__":
    post_to_x()
