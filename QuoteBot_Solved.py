# Dependencies
import tweepy
import time
import os


# Twitter API Keys
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")


# Twitter credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    
# Create quotes to tweet
quote_list = ["Quote1","Quote2","Quote3","Quote4"]


# Create function for tweeting
def QuoteItUp(quote_num):

    # Tweet the next quote
    api.update_status(quote_num)
    # Print success message
    print(f"Quote is successful. {quote_num}")

# Create a loop that tweets one quote per minute until
# all of the quotes have been tweeted
interval = 15
for quote in quote_list:
	QuoteItUp(quote)
	time.sleep(interval)
