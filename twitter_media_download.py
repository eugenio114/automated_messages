import tweepy
import os
import wget

# Authenticate with Twitter API
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Get tweets from the user's timeline
tweets = api.user_timeline(screen_name="TWITTER_ACCOUNT_NAME", count=200, include_rts=False, exclude_replies=True)

# Create a folder to store the media files
if not os.path.exists('media'):
    os.makedirs('media')

# Loop through the tweets and download media files
for tweet in tweets:
    media = tweet.entities.get("media", [])
    if len(media) > 0:
        for i, item in enumerate(media):
            wget.download(media[i]["media_url"], 'media/')
