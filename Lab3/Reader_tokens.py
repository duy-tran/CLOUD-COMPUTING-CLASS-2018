import json
import os

from Lab2 import Twitter_2

with open(os.environ['FILENAME'], 'r') as json_file:
    for line in json_file:
        tweet = json.loads(line)
        tokens = Twitter_2.preprocess(tweet['text'])
        print(tokens)