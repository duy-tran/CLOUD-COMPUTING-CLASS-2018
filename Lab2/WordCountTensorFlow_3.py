import nltk
import re

from collections import Counter
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def get_tokens():
   with open('FirstContactWithTensorFlow.txt', 'r') as tf:
    text = tf.read()
    lowers = text.lower()
    no_punctuation = re.sub(r'[^\w\s]','',lowers)
    tokens = nltk.word_tokenize(no_punctuation)
    return tokens

tokens = get_tokens()

#the lambda expression below this comment
#stores stopwords in a variable for eficiency:
#it avoids retrieving them from ntlk for each iteration
sw = stopwords.words('english');
#select the words (w) form tokens set that are not in sw
filtered = [w for w in tokens if not w in sw]

count = Counter(filtered)
#If you do not want to delete the sw -> count = Counter(tokens)

print (count.most_common(10))
print("Total number of words (with repetitions) = " + str(filtered.__len__()))
print ("Total number of words (without repetitions) = " + str(count.__len__()))

#The total number of words can also we obtained from the count
#print ("Total number of words: "+str(sum(count.values())))