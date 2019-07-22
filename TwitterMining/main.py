import argparse

from tweet_analyzer import TweetClassifier


def main():
    """How main works

       We use argparse to get search key and number of requested tweets
       and return classified tweets that match that number
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--string", help="Any keyword")
    parser.add_argument("-n", "--number", type=int,
                        help="number of tweets")
    args = parser.parse_args()
    tweet_classifier = TweetClassifier(args.string, args.number, "tweets")
    tweet_list = tweet_classifier.classify_tweets()

    tweet_index = 0
    while tweet_index < len(tweet_list):
        print(tweet_list[tweet_index][0] + "  ||  classification: " +
              tweet_list[tweet_index][1] + "  || tweet number: " +
              str(tweet_index+1)+" ||")
        tweet_index = tweet_index + 1


if __name__ == "__main__":
    main()
