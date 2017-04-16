import json
from flask import Flask
from tweet_listener import get_tweets
from sentiment_analyzer import get_tweet_sentiments

#@app.route('/getTwitterData/<username>', method=['POST'])
def getTwitterData(username):

    sentimentData = getSentiments(username);
    return reformatForUI(sentimentData)

def get_sentiment_list(username):

    tweets = get_tweets(username)
    return get_tweet_sentiments(tweets)

print(get_sentiment_list('angel__yang'))


