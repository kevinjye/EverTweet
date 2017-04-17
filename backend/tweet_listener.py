import tweepy
import json
import time
import ConfigParser
import tweepy
# from tweepy import Stream
from tweepy.streaming import StreamListener

config = ConfigParser.ConfigParser()
config.readfp(open(r'./configurations.txt'))

consumerKey=config.get('API Keys', 'consumerKey')
consumerSecret=config.get('API Keys', 'consumerSecret')
accessToken=config.get('API Keys', 'accessToken')
accessSecret=config.get('API Keys', 'accessSecret')

REQUEST_LIMIT = 420

def sentiment(tweet):

    return tweet
    pass

def get_tweets(twitter_handle):

    auth = tweepy.AppAuthHandler(consumerKey, consumerSecret)
    # auth.set_access_token(accessToken, accessSecret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    timeline = api.user_timeline(screen_name=twitter_handle, count=3200)
    user_tweets = []

    for current_tweet in timeline:
        if not current_tweet.retweeted:
            tweet = {}
            tweet['tweetId'] = current_tweet.id
            tweet['message'] = current_tweet.text
            tweet['author'] = current_tweet.user.name
            tweet['timestamp'] = current_tweet.created_at
            user_tweets.append(tweet)

    return user_tweets

# For testing purposes only
if __name__ == '__main__':
    twitter_handle = 'tomandmartys'
    all_tweets = get_tweets(twitter_handle)
    print len(all_tweets)
