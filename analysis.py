import json
from PyDictionary import PyDictionary
def get_tweets(file):
    with open(fil) as f:
        for line in f.readlines():
            yield(json.loads(line))

if __name__ == '__main__':
        pos_words=[]
        with open('positive_words.txt') as f:
            for line in f.readlines():
                pos_words.append(line.replace('\n',''))
        print(pos_words)
        with open('words.py','wb') as f:
            f.write(pos_words)
        '''fil = 'homecoming.json'
        dict = PyDictionary()
        tweets = get_tweets(fil)
        for tweet in tweets:
            tweetText = tweet['text'].lower()
            for word in tweetText.split(' '):
                if word.startswith('#'):
                    print('hashtags:'+wor
                if word in pos_dict:
                    print('positive:'+word)
                if word in neg_dict:
                    print('negative:'+word)
            print(tweetText)
            #for key in dict.meaning('love').keys():
                #print(key)'''
