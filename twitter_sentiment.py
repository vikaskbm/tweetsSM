from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import json
import matplotlib.pyplot as plt
from collections import Counter
import GetOldTweets3 as got


# getting tweets from twitter user using getoldtweets3
def get_tweets(username, max_tweets):
    import GetOldTweets3 as got
    tweetCriteria = got.manager.TweetCriteria().setUsername(username) \
        .setSince("2020-01-01") \
        .setUntil("2020-04-01") \
        .setMaxTweets(max_tweets)
    # Creation of list that contains all tweets
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    # Creating list of chosen tweet data
    tweets = [[tweet.text] for tweet in tweets]
    return tweets


username = input("Enter twitter username(multiple userneame separated by space)")
max_tweets = int(input("Enter maximum number of tweets to get"))

text_tweets = get_tweets(username, max_tweets)

text = ""
for i in range(0, len(text_tweets)):
    text = text_tweets[i][0] + " " + text

# lowercasing and cleaning the input text
text = text.lower()
cleaned_text = text.translate(str.maketrans('', '', string.punctuation))

# tokenizing the text using word_tokenize function
text_tokenize = word_tokenize(text)

# Removing stop words from our text
final_text = [word for word in text_tokenize if word not in stopwords.words('english')]

# NLP emotion algorithm.
with open('emotion.json', encoding='UTF-8') as file:
    emotions = json.load(file)

emotion_list = []
for word in final_text:
    if word in emotions:
        if isinstance(emotions[word], (list)):
            emotion_list.extend(emotions[word])
        else:
            emotion_list.append(emotions[word])

# count occurance of all the emotions in the input
emotion_count = Counter(emotion_list)


# plotting data on a graph
fig, ax1 = plt.subplots()
ax1.bar(emotion_count.keys(), emotion_count.values())
fig.autofmt_xdate()
plt.show()