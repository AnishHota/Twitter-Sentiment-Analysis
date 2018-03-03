# To read the json file which contains the tweets from getting_tweepy.py
import json
# Textblob module is used for good and bad words. It classifies the tweets on basis of -1 to 1.
# -1 being negative and 1 being positive
from textblob import TextBlob
# defaultdict is used over collections.counter because:
# 1. Ignores duplicate tweets
# 2. Store the tweets for further use.
from collections import defaultdict

#Function to get tweets one by one from the json file.
def get_tweets(input_file):
    # Opens the json file as f
    with open(input_file) as f:
        # Reads the json file line by line
        for line in f.readlines():
            #Returns the read line[tweet]
            yield(json.loads(line))

#Function to convert the polarity.
#Polarity<0: negative
#Polartity=0: neutral
#Polartity>0: positive
#for uniformity
def get_sentiment(polarity):
    if polarity<0:
        return "negative"
    elif polarity==0:
        return "neutral"
    else:
        return "positive"

#Main function
if __name__ == '__main__':
    #Name of the json file which holds the tweets
    input_file = 'homecoming.json'
    #Retrieving tweets using the get_tweets Function
    tweets = get_tweets(input_file)
    #Making a defaultdict object for storing the sentiments with their tweets
    sentiments = defaultdict(set)
    #Looping for every tweet
    for tw in tweets:
        #Only taking the text part of the tweet and converting them to lowercase
        text = dict(tw)['text'].lower()
        #Making a textblob object with tweet's text as argument
        blob = TextBlob(text)
        #Calling the get_sentiment function which will return positive,negative or neutral
        sent = get_sentiment(blob.sentiment.polarity)
        #Adding the text of the tweet to the proper sentiment in sentiments dicitonary.
        sentiments[sent].add(text)
    #Finding the total no. of tweets
    total = sum(len(i) for i in sentiments.values())
    #Finding the percentage of each tweets by dividing them with total tweets and mutliplying it by 100
    perc_pos = (float(len(sentiments['positive']))/total)*100
    perc_neg = (float(len(sentiments['negative']))/total)*100
    perc_neu = (float(len(sentiments['neutral']))/total)*100
    #Displaying the percentages
    print("Positive sentiments:{0}".format(perc_pos))
    print("negative Sentiments:{0}".format(perc_neg))
    print("neutral sentiments:{0}".format(perc_neu))
