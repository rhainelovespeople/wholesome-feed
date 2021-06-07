import tweepy
import json

# Authenticate to Twitter
with open("api_keys.json", "r") as read_file:
    keys = json.load(read_file)

auth = tweepy.OAuthHandler(keys['API_key'], keys['API_secret_key'])
auth.set_access_token(keys['access_token'], keys['access_token_secret'])

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

try:
    for tweet in tweepy.Cursor(api.home_timeline).items(10):
        tweet_json = {tweet.id: tweet.text}
        with open("scraped_tweets_file.json", "a") as append_file:
            json.dump(tweet_json, append_file, indent=4)
except tweepy.TweepError as e:
    print(str(e))

