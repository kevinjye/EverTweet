import tweepy
import json
import time
import datetime
import ConfigParser
import tweepy
from tweepy.streaming import StreamListener


'''
Get API keys from Configurations document
'''
config = ConfigParser.ConfigParser()
config.readfp(open(r'./configurations.txt'))

consumerKey=config.get('API Keys', 'consumerKey')
consumerSecret=config.get('API Keys', 'consumerSecret')
accessToken=config.get('API Keys', 'accessToken')
accessSecret=config.get('API Keys', 'accessSecret')


'''
Returns given number of tweets for given Twitter handle
'''
def get_tweets(twitter_handle, num_tweets):

    auth = tweepy.AppAuthHandler(consumerKey, consumerSecret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    timeline = api.user_timeline(screen_name=twitter_handle, count=num_tweets)

    user_tweets = []

    for current_tweet in timeline:
        if not current_tweet.retweeted:
            tweet = {}
            tweet['tweetId'] = current_tweet.id
            tweet['message'] = current_tweet.text
            tweet['author'] = current_tweet.user.name
            s = str(current_tweet.created_at)
            new_s = time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S").timetuple()) * 1000
            tweet['timestamp'] = new_s
            user_tweets.append(tweet)

    return user_tweets

