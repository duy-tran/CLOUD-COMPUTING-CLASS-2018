import nltk
from nltk.corpus import stopwords
from collections import Counter
import re

nltk.download('punkt')
nltk.download('stopwords')
# from WordCountTensorFlow_2 import get_tokens

def get_tokens():
   with open('FirstContactWithTensorFlow.txt', 'r') as tf:
    text = tf.read()
    lowers = text.lower()
    no_punctuation = re.sub(r'[^\w\s]', '', lowers)
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens

tokens = get_tokens()
# lambda expression here
# store stopwords in a variable for eficiency
# avoid retrieving them from ntlk for each iteration
sw = stopwords.words('english')
filtered = [w for w in tokens if not w in sw]
count = Counter(filtered)
print (count.most_common(10))
print ("Total number of words: "+str(sum(count.values())))