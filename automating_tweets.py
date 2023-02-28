import tweepy

class TwitterAPI:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    def post_tweet(self, tweet):
        self.api.update_status(tweet)

    def get_tweets(self, username, count=10):
        tweets = []
        for tweet in tweepy.Cursor(self.api.user_timeline, screen_name=username, tweet_mode='extended').items(count):
            tweets.append(tweet.full_text)
        return tweets

      
api = TwitterAPI('consumer_key', 'consumer_secret', 'access_token', 'access_token_secret')

# post a tweet
api.post_tweet('Hello, Twitter!')

# get a user's tweets
tweets = api.get_tweets('BarackObama', count=5)
print(tweets)
