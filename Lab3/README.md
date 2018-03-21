# Lab session #3: Extracting and Analyzing data from the Cloud

Course link: [ccbda-upc.github.io](https://ccbda-upc.github.io/).

Group 1207

-   Quang Duy Tran - duy9968\@gmail.com

-   Marc Garnica Caparros - marcgarnicacaparros\@gmail.com

Assignment link: [Lab 2 Assignment](https://github.com/CCBDA-UPC/Assignments-2018/blob/master/Lab03.md)

## Objectives

The following README summarizes the tasks done during the third lab session
of the Cloud Computing for Big Data Analytics course in Universitat Politècnica
de Catalunya. For project delivery and recovery of information during the course evolution.
This session introduces the basics for extracting appealing terms from a dataset of tweets while keeping an open connection gathering the streaming and upcoming tweets about a particular track or filter.

### Pre-lab homeworks

-   This lab assignment had no pre-tasks because it is build on the previous one ([see here](https://github.com/duy-tran/CLOUD-COMPUTING-CLASS-2018/tree/master/Lab2)).

### Lab tasks

-  [x] Set up and open connection with Twitter API, using the Real-time Tweets API. The Real-time tweets API of twitter is preferred over the common REST API if we want to perform singular searches. With the open real-time connection we are able to get massive amount of data without exceeding the rate limits. In this case we are storing the tweets from a single filter in a file. The keyword for the filter and the name of the file are stored as environment parameters and can be accessed in the code by:

```python
import os

filterKW = os.environ['FILTER_KW']
fileName = os.environ['FILENAME']
```
[[PASTE HERE SOME SCREENSHOTS ON THE FILES GENERATED AND RESULTS]]

Each line of the file contains a tweet containing the filter keyword on its text.

- [x] Analyzing the tweets: Counting the terms present on the tweets stored by the process explained in the previous point. We assume all the tweets we want to analyze have been previoulsy saved in a file. The program [TwitterAnalyzer.py](TwitterAnalyzer.py) is opening the file containing the tweets and preprocessing their text to finally count the appearance of each word. As it was studied on the previous lab session, we deleted the common English and Catalan stopwords and also the punctuation.
