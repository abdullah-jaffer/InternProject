class TweetExtractor:

    def __init__(self, file_name):
        self.file_name = file_name

    def file_opener(self):
        global input_file, input_file_list
        try:
            input_file = open(self.file_name, "r")
        except IOError:
            print("Could not open file")
        else:
            input_file_list = input_file.readlines()
        finally:
            input_file.close()

        return input_file_list

    def get_tweets(self):
        tweet_list = self.file_opener()
        return tweet_list
