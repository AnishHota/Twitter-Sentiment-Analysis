#Libraries
#Importing required consumer access and token keys for twitter API
from config import CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_SECRET
#Tweepy library for scraping twitter
import tweepy
#OAuthHandler for authorization with the API and Stream for streaming tweets.
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

#OAuthHandler object passing the required arguments
auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)

#Making an API object with the authorization
api = tweepy.API(auth)
#Output file where the tweets will be stored
output = 'homecoming.json'
#output = sys.argv[0]
#Class for the streamer
class MyStreamer(StreamListener):
    #To count the no. of tweets initalized to 0
    count = 0
    #on_data function which runs when the streamer returns any data, and it store it to the file.
    def on_data(self,data):
        print(self.count)
        #Opens the output file and writes the data in json format
        with open(output,'a') as f:
            f.write(data)
        #Increases the count of tweets after extracting a tweet
        self.count+=1
        #Checks if the tweet extracted is more than 10, stops the streaming.
        if self.count>=10:
            return False
        else:
            return True
    #on_error runs when there is any error and it prints the error.
    def on_error(self,status):
        print('Error:'+status)
        return True
#Main function
if __name__=='__main__':
    #Stream object which takes auth and the class object MyStreamer as args.
    streamer = Stream(auth,MyStreamer())
    #Streams with the keyword track.
    streamer.filter(languages=['en'],track=['SpiderManHomecoming'])
