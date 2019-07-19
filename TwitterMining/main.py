import argparse

from tweet_analyzer import TweetClassifier


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--string", help="Any keyword")
    parser.add_argument("-n", "--number", type=int,
                        help="number of tweets")
    args = parser.parse_args()
    tweet_classifier = TweetClassifier(args.string, args.number, "tweets")
    tweet_classifier.classify_tweets()


if __name__ == "__main__":
    main()
