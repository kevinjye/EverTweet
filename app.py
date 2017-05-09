import json
from flask import Flask, render_template
from tweet_listener import get_tweets
from sentiment_analyzer import get_tweet_sentiments
import time

app = Flask(__name__)
app.config.update(
	DEBUG=True,
	SECRET_KEY='EVERTWEET'
)

'''
Loads webpage
'''
@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')


'''
Returns given number of sentiment values for given user
'''
@app.route('/getSentimentList/<username>/<numTweets>', methods=['GET', 'POST'])
def get_sentiment_list(username, numTweets):

	tweets = get_tweets(username, numTweets)
	return get_tweet_sentiments(tweets)

if __name__ == '__main__':
	app.run()
