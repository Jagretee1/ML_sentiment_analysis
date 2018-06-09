import tweepy
from textblob import TextBlob

consumer_key = 'UOxyq6CRLOrZyLtOrfmnQPWJj'
consumer_secret = 'ovqZnQP2SlY4phDm0MxZCU5jsiBfzffgSUtVnQdAmTZEqTghMS'

access_token = '358621146-6XxALl8QhMZZs082lJKzFKPOg4rHLOiKV4UOxicK'
access_token_secret = 'cqRV6ccdwDPgc7VZJTHw0LhrZkAZgEqaiVFHERaz42xGj'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token (access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Alone')

for tweet in public_tweets:
     print(tweet.text)

     analysis = TextBlob(tweet.text)
     print(analysis.sentiment)
     print("")
