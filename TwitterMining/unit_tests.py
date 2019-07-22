import unittest

from ddt import ddt, data, unpack

from tweet_analyzer import TweetClassifier


@ddt
class TestClasses(unittest.TestCase):

    @data("hey", "Fifi", "Accident", "Event")
    def test_tweet_count(self, search_key):
        """Test number of retrieved tweets
           It is not possible to test the expected tweets exactly but
            we can test the expected number of tweets which this test does
        """
        tweet_classifier = TweetClassifier(search_key, 10, "tweets")
        self.assertTrue(len(tweet_classifier.classify_tweets()) <= 10)

    @data("hey", "Fifi", "Accident", "Event")
    def test_tweet_validity(self, search_key):
        """Test if tweet contains the word
        """
        tweet_classifier = TweetClassifier(search_key, 10, "tweets")
        tweets_list = tweet_classifier.retrieve_tweets()
        for tweet in tweets_list:
            self.assertTrue(search_key in tweet)
