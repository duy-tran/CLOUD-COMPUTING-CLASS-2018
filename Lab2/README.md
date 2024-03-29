# Lab session #2: Doors in the cloud

Course link: [ccbda-upc.github.io](https://ccbda-upc.github.io/).

Group 1207

-   Quang Duy Tran - duy9968\@gmail.com

-   Marc Garnica Caparros - marcgarnicacaparros\@gmail.com

Assignment link: [Lab 2 Assignment](https://github.com/CCBDA-UPC/Assignments-2018/blob/master/Lab02.md)

## Objectives

The following README summarizes the tasks done during the second lab session
of the Cloud Computing for Big Data Analytics course in Universitat Politècnica
de Catalunya. For project delivery and recovery of information during the course evolution.



### Pre-lab homeworks

-   Registering our app on twitter for accessing the API (Application Programming Interface)
in http://apps.twitter.com

### Lab tasks

#### NLTK

- [x] NLTK package setup. Python package for Natural Language Processing. It does not only include algorithms but also linguistic data.
- [x] **Task 2.1.1** [First script](WordCountTensorFlow_1.py) using NLTK: Tokenizing the whole .txt file, counting the tokens and printing the 10 most common, also printing the total number of words in the file (with and without repetitions)

![Task 2.1.1](img/t211.png)

- [x] **Task 2.1.2** [Second script](WordCountTensorFlow_2.py) modifying the first one. In this case removing the punctuation from the tokens set.

![Task 2.1.2](img/t212.png)


- [x] **Task 2.1.3** For a better analysis of the words used in the file, it is also possible to remove the Stop Words, words language-dependent that are highly used without adding semantic meaning to the context. [Third Script](WordCountTensorFlow_3.py).

![Task 2.1.3](img/t213.png)

#### TWEEPY

- [x] Tweepy setup on the python environment. Package to access Twitter data.
- [x] Getting the Twitter credentials from the twitter app created previously.
- [x] Protecting our credentials for being public with environment variables through Pycharm >> Edit configurations. And adding this into the code:

```python
import os

#Credential setup
auth = OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_SECRET'])
```

**os.environ[key]** returns the value of that certain key in the Environment Variables configuration.

- [x] Accessing profile data with tweepy with [Twitter_1.py](Twitter_1.py) script.

![Task 2.2.1](img/t221.png)

- [x] [Twitter_2.py](Twitter_2.py) script shows that tweets data can be accessed in multiple ways.
   -   Accessing one tweet text:

   ![One tweet text](img/t2221.png)

   -   Printing the json format of a tweet status: [tweet_status.json](tweet_status.json).
   -   Printing the json format of 10 friend in the twiteer profile: [tw_friends.json](tw_friends.json).
   -   Analysing the json format of our own tweets: [tweet.json](tweet.json).

- [x] Analyzing tweets information by Natural Language processing.
   -   Printing the tokens of the tweet.

   ![Task 2.3.1](img/t231.png)
   The complete text can also be accessed in [tweet_tokens.txt](tweet_tokens.txt)

   -   We also tried a more detailed analysis to get the most common topic in the newsfeed. We tried to achieve this by analysing (as we did in the first NLTK part) the words in the text. For a better understanding of the results we deleted the stopwords and punctuation. We needed to add some new code to filter the text.

   ```python
   import nltk
   from nltk.corpus import stopwords
   from collections import Counter
   import string

   nltk.download('stopwords')

   #creating the final list of discarded words or punctuation
   punctuation = list(string.punctuation)
   stop = punctuation + stopwords.words('spanish') + stopwords.words('english') + ['rt', 'via', '…', 'RT', '‘'] + ['ón', 'és', 'i', 'ó', '', 'els']
   ```
   This last snippet is creating the stop list with stopwords for spanish and english adding some specials chars and custom catalan stopwords.

   ```python
   #New process to get the tweet text, preprocess them and count them (without the stopwords)
   #'''
   #Analyze the 10 most common words used in the newsfeed
   totalCount = Counter()
   for status in tweepy.Cursor(api.home_timeline).items(40):
      print("Tokens: ", preprocess(status._json["text"], True))
      words_all = [word for word in preprocess(status._json['text'], True) if word not in stop]
      totalCount.update(words_all)
   print(totalCount.most_common(10))
   #'''
   ```

   Note that we used the second optional parameter of the function **preprocess** to lower all the tokens so that we can compared with the stopwords list.
   As an example of output we obtained this:

   ```
   [('#barçachelsea', 4), ('🔵', 4), ('🔴', 4), ('3', 3), ('santos', 2), ('sec', 2), ('charged', 2), ('theranos', 2), ('founder', 2), ('elizabeth', 2)]
   ```   
   Looks like [@marcgarnica](https://twitter.com/marc_garnica) is really following FCs Barcelona news!
