# Aidan Henry
# Class representing tweet-like messages
import time


class Tweet:
    def __init__(self, author, text):
        self.__author = author
        self.__text = text
        self.__age = time.time()

    def get_author(self):
        return self.__author

    def get_text(self):
        return self.__text

    def get_age(self):
        current_time = time.time()
        tweet_age = int(current_time - self.__age)
        if tweet_age > 59:
            if tweet_age > 3600:
                age_string = str(int(tweet_age / 3600)) + "h"
                return age_string
            age_string = str(int(tweet_age / 60)) + "m"
            return age_string
        age_string = str(tweet_age) + "s"
        return age_string
