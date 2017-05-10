import os, sys
sys.path.append("..")
import app as EverTweet
import unittest
import tempfile

class TweetTestCase(unittest.TestCase):

    def setUp(self):
        EverTweet.app.config['TESTING'] = True
        self.app = EverTweet.app.test_client()

    def test_homepage(self):
        rv = self.app.get('/')
        assert rv.status_code == 200

    def test_username1(self):
        rv = self.app.get('/getSentimentList/RealDonaldTrump/10')
        assert rv.status_code == 200

    def test_username2(self):
        rv = self.app.get('/getSentimentList/BarackObama/10')
        assert rv.status_code == 200

if __name__ == '__main__':
    unittest.main()
