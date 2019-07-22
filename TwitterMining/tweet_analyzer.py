import re

from load_tweets import TweetExtractor


class TweetClassifier:

    def __init__(self, search_query, tweet_count, data_source):
        self.search_query = search_query
        self.tweet_count = tweet_count
        self.data_source = data_source

    def retrieve_tweets(self):
        """Tweet Filtering

           This function filters the tweets according to the number and
           keyword specified by the user and wraps them up in a list
        """
        tweet_extractor = TweetExtractor(self.data_source)
        tweets = tweet_extractor.get_tweets()
        required_tweets = []
        tweet_index = 0

        for tweet in tweets:
            if self.search_query in tweet and \
                    tweet_index < self.tweet_count:
                required_tweets.append(tweet)
                tweet_index = tweet_index + 1

        return required_tweets

    def classify_tweets(self):
        """Tweet classification

           This is the key function that classifies the tweets and puts
           them in a list along with their assigned classification
        """
        tweets = self.retrieve_tweets()
        tweet_list = []
        for tweet in tweets:
            if re.search("#+", str(tweet)):
                tweet_list.append([tweet, "HashTag"])

            elif re.search("(https?:\/\/)?([\da-z-]+)\."
                         "([a-z]{2,6})([\/\w-]*)*\/?\S", tweet):
                tweet_list.append([tweet, "Link"])

            elif re.search("@+", tweet):
                tweet_list.append([tweet, " Mention"])

            else:
                tweet_list.append([tweet, "Simple Tweet"])

        return tweet_list
