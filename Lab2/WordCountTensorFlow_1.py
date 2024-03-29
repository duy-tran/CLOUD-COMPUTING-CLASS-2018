import nltk
nltk.download('punkt')
import re

from collections import Counter

def get_tokens():
   with open('FirstContactWithTensorFlow.txt', 'r') as tf:
    text = tf.read()
    tokens = nltk.word_tokenize(text)
    return tokens

tokens = get_tokens()
count = Counter(tokens)
print (count.most_common(10))
print("Total number of words (with repetitions) = " + str(tokens.__len__()))
print ("Total number of words (without repetitions) = " + str(count.__len__()))

#The total number of words can also we obtained from the count
#print ("Total number of words: "+str(sum(count.values())))