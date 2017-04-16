import tweepy
import json
import time
import ConfigParser
from tweepy import Stream
from tweepy.streaming import StreamListener

config = ConfigParser.ConfigParser()
config.readfp(open(r'./configurations.txt'))

consumerKey=config.get('API Keys', 'consumerKey')
consumerSecret=config.get('API Keys', 'consumerSecret')
accessToken=config.get('API Keys', 'accessToken')
accessSecret=config.get('API Keys', 'accessSecret')

REQUEST_LIMIT = 420

class TweetListener(StreamListener):

    def on_data(self, data):
        try:
            parse_data(data)
        except:
            print("No data found")


    def on_error(self, status):
        errorMessage = "Error - Status code " + str(status)
        print(errorMessage)
        if status == REQUEST_LIMIT:
            print("Request limit reached. Trying again...")
            exit()

def parse_data(data):

    tweet = {}
    current_tweet = json.loads(data)
    
    tweet['location'] = current_tweet["place"]
    tweet['coordinates'] = current_tweet["coordinates"]
    tweet['language'] = current_tweet["lang"]
    tweet['tweetId'] = current_tweet['id_str']
    tweet['message'] = current_tweet["text"]
    tweet['author'] = current_tweet["user"]["name"]
    tweet['timestamp'] = current_tweet["created_at"]

    print tweet


def startStream():

    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(accessToken, accessSecret)
    while True:
        try:
            twitterStream = Stream(auth, TweetListener())
            twitterStream.filter(languages=['en'], track='Chelsea')
        except:
            print("Restarting Stream")
            continue

# For testing purposes only

if __name__ == '__main__':
    startStream()
