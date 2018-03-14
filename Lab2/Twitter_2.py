import tweepy
import json
import os
import re
from tweepy import OAuthHandler
from nltk.tokenize import word_tokenize

emoticons_str = r"""
    (?:
        [:=;] 
        [oO\-]?
        [D\)\]\(\]/\\OpP] 
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)',  # other words
    r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

auth = OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_SECRET'])

api = tweepy.API(auth)

user = api.me()

#'''
#Tweet newsfeed
for status in tweepy.Cursor(api.home_timeline).items(1):
    print(json.dumps(status._json, indent=2))
#'''

'''
#User's friends
for friend in tweepy.Cursor(api.friends).items(1):
    print(json.dumps(friend._json, indent=2))
#'''

'''
#User's tweets
for tweet in tweepy.Cursor(api.user_timeline).items(1):
    print(json.dumps(tweet._json, indent=2))
#'''

'''
#Preprocess 10 tweets in newsfeed
for status in tweepy.Cursor(api.home_timeline).items(10):
    print(preprocess(json.dumps(status._json["text"], indent=2)))
#'''