import tweepy
import os

# GitHubのSecretsから鍵を読み込む
API_KEY = os.environ["API_KEY"]
API_SECRET = os.environ["API_SECRET"]
ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
ACCESS_SECRET = os.environ["ACCESS_SECRET"]

def post_to_x():
    # X APIに接続
    client = tweepy.Client(
        consumer_key=API_KEY, consumer_secret=API_SECRET,
        access_token=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET
    )
    
    # 投稿するメッセージ
    status_text = "テスト投稿です！botが正常に動作しています。\n\n詳しくはこのリンクをクリック→ https://example.com"
    
    try:
        # 投稿実行
        client.create_tweet(text=status_text)
        print("Successfully posted!")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    post_to_x()
