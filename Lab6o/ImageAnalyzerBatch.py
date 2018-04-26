import os
import tweepy
import time
import matplotlib as mpl
import matplotlib.pyplot as plt
import googleapiclient.discovery

from tweepy import OAuthHandler
from collections import Counter
from wordcloud import WordCloud

auth = OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_SECRET'])

api = tweepy.API(auth)

# Maximum number of images per batch request
MAX_IMAGES_PER_BATCH = 16

def generate_histogram(count_label, name):
    print(str(count_label.most_common()))

    mpl.rcParams['figure.figsize'] = (10, 10)
    sorted_x, sorted_y = zip(*count_label.most_common(10))
    print(sorted_x, sorted_y)

    plt.bar(range(len(sorted_x)), sorted_y, width=0.75, align='center')
    plt.xticks(range(len(sorted_x)), sorted_x, rotation=60)
    plt.axis('tight')
    plt.savefig(name + '_histogram.png')

    plt.show()

    print(" -- Histogram saved in " + name + "_histogram.png file.")

def generate_wordcloud(count_label, name):
    count_label = dict(count_label)
    wordcloud = WordCloud(background_color="white").generate_from_frequencies(count_label)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(name + '_wordcloud.png')

    plt.show()

    print(" -- Wordcloud saved in " + name + "_wordcloud.png file.")

def main(twitter_profile, numberOfImages):
    start_time = time.time()
    print(' -- Receiving a new request')
    print(' -- Twitter URL: ' + twitter_profile)
    # The only parameter is the twitter profile url
    profile_name = twitter_profile.rsplit('com/', 1)[1]
    print(' -- Twitter user: ' + profile_name)
    print(' -- Getting the last ' + str(numberOfImages) + ' photos posted')
    image_count = 0
    tweet_count = 0
    array_index = 0
    t_images = []
    t_images.append([])

    while image_count < numberOfImages:
        tweets = api.user_timeline(profile_name, count=100)
        for t in tweets:
            if image_count < numberOfImages:
                tweet_count += 1
                try:
                    for m in t.entities['media']:
                        if m['type'] == 'photo':
                            t_images[array_index].append(m['media_url_https'])
                            image_count += 1
                            if image_count % MAX_IMAGES_PER_BATCH == 0 and image_count < numberOfImages:
                                t_images.append([])
                                array_index += 1
                except:
                    pass

    print(' -- ' + str(image_count) + ' pictures were contained in his/her/its last ' + str(tweet_count) + ' tweets')

    print(' -- Analysing the pictures with Google Cloud Vision API')
    image_count = 0
    service = googleapiclient.discovery.build('vision', 'v1')
    count_label = Counter()
    # Images are sending in batches, since the number of images per batch in a request is limited
    for batch in t_images:
        requests = []
        for url in batch:
            image_count += 1
            requests.append({
                    'image': {
                        'source': {
                            "imageUri": url
                        }
                    },
                    'features': [{
                        'type': 'LABEL_DETECTION',
                        'maxResults': 10
                    }]
                })
        service_request = service.images().annotate(body={
            'requests': requests
        })
        responses = service_request.execute()
        for response in responses['responses']:
            for result in response['labelAnnotations']:
                count_label[result['description']] += result['score']

    generate_histogram(count_label, profile_name)
    generate_wordcloud(count_label, profile_name)
    end_time = time.time()
    print(' -- Total running time: ' + str(round(end_time - start_time,2)) + ' s')

twitter_url = str(input("Introduce the twitter url: "))
numberOfImages = int(input("Introduce the number of images for the analysis: "))
main(twitter_url, numberOfImages)
