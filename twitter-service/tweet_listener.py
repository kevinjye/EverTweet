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

def parse_data(data):

    current_tweet = json.loads(data)

    tweet = {}

    tweet['location'] = current_tweet["place"]
    tweet['tweetId'] = current_tweet['id_str']
    tweet['message'] = current_tweet["text"]
    tweet['author'] = current_tweet["user"]["name"]
    tweet['timestamp'] = current_tweet["created_at"]

    print tweet

def sentiment(tweet):

    return tweet
    pass

def get_tweets():

    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessSecret)
    api = tweepy.API(auth)

    timeline = api.user_timeline(screen_name='bryanyu12345')
    user_tweets = []

    for current_tweet in timeline:
        tweet = {}    
        tweet['tweetId'] = current_tweet.id_str
        tweet['message'] = current_tweet.text
        tweet['author'] = current_tweet.user.name
        tweet['timestamp'] = current_tweet.created_at
        user_tweets.append(tweet)

    print user_tweets

# For testing purposes only

if __name__ == '__main__':
    get_tweets()
