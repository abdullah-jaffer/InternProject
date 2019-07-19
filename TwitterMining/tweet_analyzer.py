import re

from load_tweets import TweetExtractor


class TweetClassifier:

    def __init__(self, search_query, tweet_count, data_source):
        self.search_query = search_query
        self.tweet_count = tweet_count
        self.data_source = data_source

    def retrieve_tweets(self):
        tweet_extractor = TweetExtractor(self.data_source)
        tweets = tweet_extractor.get_tweets()
        required_tweets = []
        tweet_index = 0

        for tweet in tweets:
            if self.search_query in tweet and \
                    tweet_index <= self.tweet_count:

                required_tweets.append(tweet)
                tweet_index = tweet_index + 1

        return required_tweets

    def classify_tweets(self):
        tweets = self.retrieve_tweets()
        classification = ""
        for tweet in tweets:
            if re.search("#+", str(tweet)):
                classification += "HashTag "
            if re.search("(https?:\/\/)?([\da-z-]+)\."
                         "([a-z]{2,6})([\/\w-]*)*\/?\S", tweet):
                classification += " Link "
            if re.search("@+", tweet):
                classification += " Mention"

            classification = "Simple Tweet" if classification == "" \
                else classification

            print(str(tweet) + " " + classification + "\n")
            classification = ""
