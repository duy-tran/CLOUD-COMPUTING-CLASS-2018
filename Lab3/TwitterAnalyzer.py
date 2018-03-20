import json
from collections import Counter
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords") # download the stopword corpus on our computer
import string
from Lab2.Twitter_2 import preprocess

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via', 'RT', '…']

fname = 'ArtificialIntelligenceTweets.json'
with open(fname, 'r') as f:
    count_all = Counter()
    count_hashtag = Counter()
    count_term = Counter()
    for line in f:
        tweet = json.loads(line)
        # Create a list with all the terms
        terms_stop = [term for term in preprocess(tweet['text'])
                      if term not in stop]
        hashtag_only = [term for term in preprocess(tweet['text'])
                        if term.startswith('#')]
        terms_only = [term for term in preprocess(tweet['text'])
                      if term not in stop and
                      not term.startswith(('#', '@'))]
        count_all.update(terms_stop)
        count_hashtag.update(hashtag_only)
        count_term.update(terms_only)
    print('Top 10 tokens: ', end=" ")
    for word, index in count_all.most_common(10):
        print (word, end="\t")
    print('\nTop 10 hashtags: ', end=" ")
    for word, index in count_hashtag.most_common(10):
        print (word, end="\t")
    print('\nTop 10 terms: ', end=" ")
    for word, index in count_term.most_common(10):
        print (word, end="\t")