from collections import Counter
import json
import string
from Lab2.Twitter_2 import preprocess

import nltk
from nltk.corpus import stopwords
nltk.download("stopwords") # download the stopword corpus on our computer

punctuation = list(string.punctuation)
stop = stopwords.words('english') + stopwords.words('spanish') + punctuation + ['rt', 'via', 'RT', '…', '#', 'ี', '️', '¿', '¡', '’']

fname = 'Madrid.json'
with open(fname, 'r') as json_file:
        count_all = Counter()
        count_stop = Counter()
        count_hash = Counter()
        count_mentions = Counter()
        numberOfTweets = 0

        for line in json_file:
            numberOfTweets += 1
            tweet = json.loads(line)

            # List of all the terms
            t_all = [term for term in preprocess(tweet['text'])]

            # List of all the terms without sw and it is not a hashtag
            t_stop = [word for word in preprocess(tweet['text'], True) if
                      word not in stop and not word.startswith(('#', '@'))]

            # List of all hashtags
            t_hash = [hash for hash in preprocess(tweet['text']) if hash.startswith('#') and hash not in stop]

            # Lis of all mentions
            t_mention = [mention for mention in preprocess(tweet['text']) if mention.startswith('@')]

            # Update the counter
            count_all.update(t_all)
            count_stop.update(t_stop)
            count_hash.update(t_hash)
            count_mentions.update(t_mention)

        print("-------RESULT-------")
        print("Number of tweets analyzed: " + str(numberOfTweets))
        print("Top 10 token appearences -> " + str(count_all.most_common(10)))
        print("Top 20 word appearences (without stopwords) -> " + str(count_stop.most_common(20)))
        print("Top 20 hashtag appearences -> " + str(count_hash.most_common(20)))
        print("Top 20 mention appearences -> " + str(count_mentions.most_common(20)))

import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (6,6)
import matplotlib.pyplot as plt

sorted_x, sorted_y = zip(*count_hash.most_common(20))
print(sorted_x, sorted_y)

plt.bar(range(len(sorted_x)), sorted_y, width=0.75, align='center')
plt.xticks(range(len(sorted_x)), sorted_x, rotation=60)
plt.axis('tight')


# plt.savefig('Madrid.png')     # save it on a file

##Show needs to come after savefig, if not the image on the local drive was blank.
plt.show()                  # show it on IDE
