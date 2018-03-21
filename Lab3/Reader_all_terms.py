import json
import nltk
import string

from Lab2.Twitter_2 import preprocess

from collections import Counter
from nltk.corpus import stopwords
nltk.download("stopwords")

punctuation = list(string.punctuation)
stop = punctuation + stopwords.words('spanish') + stopwords.words('english') + ['rt', 'via', '…', 'RT', '‘'] + ['ón', 'és', 'i', 'ó', '', 'els']


with open('AnalyticsTweets.json', 'r') as json_file:
    count_all = Counter()
    count_stop = Counter()
    count_hash = Counter()
    count_mentions = Counter()

    for line in json_file:
        tweet = json.loads(line)

        # List of all the terms
        t_all = [term for term in preprocess(tweet['text'])]

        # List of all the terms without sw and it is not a hashtag
        t_stop = [word for word in preprocess(tweet['text']) if word not in stop and not word.startswith(('#', '@'))]

        # List of all hashtags
        t_hash = [hash for hash in preprocess(tweet['text']) if hash.startswith('#')]

        # Lis of all mentions
        t_mention = [mention for mention in preprocess(tweet['text']) if mention.startswith('@')]

        # Update the counter
        count_all.update(t_all)
        count_stop.update(t_stop)
        count_hash.update(t_hash)
        count_mentions.update(t_mention)

    print("-------RESULT-------")
    print("Top 10 token appearences -> " + str(count_all.most_common(10)))
    print("Top 10 word appearences (without stopwords) -> " + str(count_stop.most_common(10)))
    print("Top 10 hashtag appearences -> " + str(count_hash.most_common(10)))
    print("Top 10 mention appearences -> " + str(count_mentions.most_common(10)))