import json
from flask import jsonify
import datetime
import ConfigParser
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as features
import time

config = ConfigParser.ConfigParser()
config.readfp(open(r'./configurations.txt'))

watson_url = config.get('WATSON API Keys', 'url')
watson_username = config.get('WATSON API Keys', 'username')
watson_password = config.get('WATSON API Keys', 'password')

nlu_analyzer = NaturalLanguageUnderstandingV1(
    version=datetime.date.today(),
    username=watson_username,
    password=watson_password)

def get_sentiment(input_text):

    response = nlu_analyzer.analyze(text=input_text,
                                    features=[features.Emotion()], 
                                    language='en')
    return response['emotion']['document']['emotion']

def get_tweet_sentiments(tweets):
    start = time.time()

    sentiment_list = {'angry': [], 'joy': [], 'sadness': [], 'fear': [], 'disgust': []}

    for tweet in tweets:
        message = tweet['message']
        timestamp = tweet['timestamp']

        sentiment = get_sentiment(message)
        sentiment_list['angry'].append(
            [message, timestamp, sentiment['anger']]
        )
        sentiment_list['joy'].append(
            [message, timestamp, sentiment['joy']]
        )
        sentiment_list['sadness'].append(
            [message, timestamp, sentiment['sadness']]
        )
        sentiment_list['fear'].append(
            [message, timestamp, sentiment['fear']]
        )
        sentiment_list['disgust'].append(
            [message, timestamp, sentiment['disgust']]
        )

    end = time.time()
    print(end - start)
    return json.dumps(sentiment_list)


