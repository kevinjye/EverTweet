import json
from flask import Flask
from tweet_listener import get_tweets
from sentiment_analyzer import get_tweet_sentiments

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='EVERTWEET'
)

@app.route('/getTwitterData/<username>', methods=['GET', 'POST'])
def getTwitterData(username):

    sentimentData = getSentiments(username);
    return reformatForUI(sentimentData)

@app.route('/getSentimentList/<username>', methods=['GET', 'POST'])
def get_sentiment_list(username):

    tweets = get_tweets(username)
    return get_tweet_sentiments(tweets)

if __name__ == '__main__':
    app.run()
