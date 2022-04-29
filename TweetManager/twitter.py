# Aidan Henry
# This program manages the tweets created using the Tweet class
import Tweet
import pickle
import os

MAX_TWEET_LENGTH = 140


def load_tweets(tweets):
    tweet_history = []
    try:
        tweet_file = open("tweets.txt", "rb")
        tweet_file_size = os.path.getsize("tweets.txt")
        if tweet_file_size == 0:
            return
    except FileNotFoundError:
        tweet_file = open("tweets.txt", "x")
        exit()
    while True:
        try:
            tweet_history.append(pickle.load(tweet_file))
        except EOFError:
            break
    # for tweet in tweet_history:
    # print(tweet.get_text())
    tweets.extend(tweet_history)
    # for tweet in tweets:
    # print(tweet.get_text())
    tweet_file.close()


def make_tweet(tweets):
    name = input("What is your name? ")
    while True:
        text = input("What would you like to tweet? ")
        if len(text) > MAX_TWEET_LENGTH:
            print("Tweets can only be 140 characters!")
            continue
        else:
            break
    # print(len(text))
    tweet = Tweet.Tweet(name, text)
    tweets.append(tweet)
    tweet_file = open("tweets.txt", "ab")
    pickle.dump(tweet, tweet_file)
    tweet_file.close()
    print(name + ", your tweet has been saved.")


def view_recent_tweets(tweets):
    if len(tweets) < 5:
        for tweet in reversed(tweets):
            print(tweet.get_author() + " - " + tweet.get_age())
            print(tweet.get_text())
    else:
        tweets.reverse()
        for i in range(5):
            print(tweets[i].get_author() + " - " + tweets[i].get_age())
            print(tweets[i].get_text())
        tweets.reverse()


def search_tweets(tweets):
    if not tweets:
        print("Empty")
    else:
        search_results = []
        search = input("What would you like to search for? ")
        for tweet in tweets:
            if search in tweet.get_text():
                search_results.append(tweet)
        print("Search Results")
        print("------")
        if not search_results:
            print("No results found")
        else:
            for result in search_results:
                print(result.get_author() + " - " + result.get_age())
                print(result.get_text())


def main():
    twitter = True
    tweets = []
    load_tweets(tweets)
    while twitter:
        print("Tweet Menu")
        print("______")
        print("1. Make Tweet")
        print("2. View Recent Tweets")
        print("3. Search Tweets")
        print("4. Quit\n")
        while True:
            try:
                tweet_manager_choice = int(input("What would you like to do? "))
                if tweet_manager_choice < 1 or tweet_manager_choice > 4:
                    print("Please select a valid option")
                    continue
            except ValueError:
                print("Please enter a numeric value\n")
                continue
            else:
                break

        if tweet_manager_choice == 1:
            make_tweet(tweets)
        if tweet_manager_choice == 2:
            view_recent_tweets(tweets)
        if tweet_manager_choice == 3:
            search_tweets(tweets)
        if tweet_manager_choice == 4:
            twitter = False


main()
