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