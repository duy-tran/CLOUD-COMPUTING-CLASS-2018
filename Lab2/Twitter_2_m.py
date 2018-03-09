import tweepy
import os
import json

from tweepy import OAuthHandler

#Credential setup
auth = OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_SECRET'])

#API initialisation
api = tweepy.API(auth)

#api variable is now the entry point for most of the Twitter REST methods
user = api.me()
print ('Name: ' + user.name)
print ('Location: ' + user.location)
print ('Friends: ' + str(user.followers_count))
print ('Created: ' + str(user.created_at))
print('Description: ' + str(user.description))

"""
We use 1 to limit the number of tweets we are reading
and we only access the text of the tweet
"""
for status in tweepy.Cursor(api.home_timeline).items(1):
    print(status.text)

"""
# Print for each tweet its status with json format
for status in tweepy.Cursor(api.home_timeline).items(1):
    print(json.dumps(status._json, indent=2)
"""

"""
# Print a list of 10 of our friends
for friend in tweepy.Cursor(api.friends).items(10):
    print(json.dumps(friend._json, indent=2))
"""

"""
# Print some of our tweets
for tweet in tweepy.Cursor(api.user_timeline).items(1):
    print(json.dumps(tweet._json, indent=2))
"""