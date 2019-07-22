class TweetExtractor:

    def __init__(self, file_name):
        self.file_name = file_name
        self.input_file = ""
        self.input_file_list = []

    def file_opener(self):
        """Tweet Loading

           Extracts all the tweets and puts them in a list
        """
        try:
            self.input_file = open(self.file_name, "r")
        except IOError:
            print("Could not open file")
        else:
            self.input_file_list = self.input_file.readlines()
        finally:
            self.input_file.close()

        return self.input_file_list

    def get_tweets(self):
        tweet_list = self.file_opener()
        return tweet_list
