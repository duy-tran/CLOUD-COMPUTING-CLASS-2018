import os
import tweepy
import matplotlib as mpl
import matplotlib.pyplot as plt
import googleapiclient.discovery


from tweepy import OAuthHandler
from collections import Counter
from wordcloud import WordCloud

auth = OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_SECRET'])

api = tweepy.API(auth)

def generate_histogram(count_label, name):
    print(str(count_label.most_common()))

    mpl.rcParams['figure.figsize'] = (6, 6)
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
    wordcloud = WordCloud().generate_from_frequencies(count_label)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(name + '_wordcloud.png')

    plt.show()

    print(" -- Wordcloud saved in " + name + "wordcloud.png file.")

def main(twitter_profile, numberOfImages):
    print(' -- Receiving a new request')
    print(' -- Twitter URL: ' + twitter_profile)
    # The only parameter is the twitter profile url
    profile_name = twitter_profile.rsplit('/', 1)[1]
    print(' -- Twitter user: ' + profile_name)
    print(' -- Getting the last ' + str(numberOfImages) + ' photos posted')

    image_count = 0
    tweet_count = 0

    t_images = []

    while (image_count < numberOfImages):
        tweets = api.user_timeline(profile_name, count=100)
        for t in tweets:
            if (image_count < numberOfImages):
                tweet_count += 1
                try:
                    for m in t.entities['media']:
                        if m['type'] == 'photo':
                            t_images.append(m['media_url_https'])
                            image_count += 1
                except:
                    pass

    print(' -- ' + str(image_count) + ' pictures were contained in his/her/its last ' + str(tweet_count) + ' tweets')

    print(' -- Analysing the pictures with Google Cloud Vision API')
    image_count = 0
    service = googleapiclient.discovery.build('vision', 'v1')
    count_label = Counter()
    for url in t_images:
        image_count += 1
        service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'source': {
                        "imageUri": url
                    }
                },
                'features': [{
                    'type': 'LABEL_DETECTION',
                    'maxResults': 10
                }]
            }]
        })

        # [END construct_request]
        # [START parse_response]
        response = service_request.execute()
        print("Results for image " + url + " " + image_count + " out of " + numberOfImages)
        for result in response['responses'][0]['labelAnnotations']:
            #print("%s - %.3f" % (result['description'], result['score']))
            count_label[result['description']] += result['score']
        # [END parse_response]

    generate_histogram(count_label, profile_name)
    generate_wordcloud(count_label, profile_name)




twitter_url = str(input("Introduce the twitter url: "))
numberOfImages = int(input("Introduce the number of images for the analysis: "))
main(twitter_url, numberOfImages)
