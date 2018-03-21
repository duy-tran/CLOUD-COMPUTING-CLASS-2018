import json

from Lab2 import Twitter_2

with open('AnalyticsTweets.json', 'r') as json_file:
    for line in json_file:
        tweet = json.loads(line)
        tokens = Twitter_2.preprocess(tweet['text'])
        print(tokens)