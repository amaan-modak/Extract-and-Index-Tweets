from __future__ import absolute_import, print_function

import tweepy
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import Cursor

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="9ZxyM3MhFBcvIDTJcMAUucZLW"
consumer_secret="FfIqwxe18ZQy6IJeyawFmlYhuSr9Uf3DTTa2xEQImcb9ujqyut"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="46865394-wRX6n4xAcnQYZa68noSWE4wuScjFTsaJb3z6W6GTG"
access_token_secret="R89g3FVt28OrnWmWHUKClo9s7pZddmxYz6lZr6ET5mBVa"

class StdOutListener(StreamListener):
    
    def on_data(self, data):
        try:
            data = json.loads(data)
            # This loop is used to identify the retweeted tweets and the text does not contain @RT term
            if 'retweeted_status' not in data and 'RT @' not in data['text']:
                print(data['text'])
                # This if loop identifies the language of the tweet and writes the tweet data into a separate file according to the language specified..
                if data['lang'] == 'en':
                        with open('GOT-en.json', 'a') as file:
                            file.write(json.dumps(data) + '\n')
                        return True
                if data['lang'] == 'ko':
                        with open('GOT-ko.json', 'a') as file:
                            file.write(json.dumps(data) + '\n')
                        return True
                if data['lang'] == 'es':
                        with open('GOT-es.json', 'a') as file:
                            file.write(json.dumps(data) + '\n')
                        return True
                if data['lang'] == 'tr':
                        with open('GOT-tr.json', 'a') as file:
                            file.write(json.dumps(data) + '\n')
                        return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
			
    def on_error(self, status):
        print(status)
        return True

# This method displays the tweet in command print.
def process_or_store(tweet):
    print(json.dumps(tweet))

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # This is used to stream tweets based on the query defined the track specified below.
    twitter_stream = Stream(auth, l)
    twitter_stream.filter(track=['Game of Thrones, Jon Snow, Winds of Winter'])