import json
import datetime
import ConfigParser
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as features

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
                                    features=[features.Emotion()])
    return response['emotion']['document']['emotion']

def get_tweet_sentiments(tweets):

    sentiment_list = {'angry': [], 'joy': [], 'sadness': [], 'fear': [], 'disgust': []}

    for tweet in tweets:
        message = tweet['message']
        timestamp = tweet['timestamp']

        sentiment = get_sentiment(message)
        sentiment_list['angry'].append(
            [timestamp, message, sentiment['anger']]
        )
        sentiment_list['joy'].append(
            [timestamp, message, sentiment['joy']]
        )
        sentiment_list['sadness'].append(
            [timestamp, message, sentiment['sadness']]
        )
        sentiment_list['fear'].append(
            [timestamp, message, sentiment['fear']]
        )
        sentiment_list['disgust'].append(
            [timestamp, message, sentiment['disgust']]
        )

    return sentiment_list


