import tweepy
import sys
import jsonpickle

def process_or_store(data, topic_name):
    flag = False
    try:
        #data = json.loads(data)
        # This loop is used to identify the retweeted tweets and the next loop checks whether text does not contain @RT term
        if 'retweeted_status' not in data:
            print(data['text'])
            if 'RT @' not in data['text']:
                print(data['lang'])
                # This if loop identifies the language of the tweet and writes the tweet data into a separate file according to the language specified..
                if data['lang'] == 'en':
                    with open(topic_name + '-en.json', 'a') as f:
                        f.write(jsonpickle.encode(data, unpicklable=False) + '\n')
                        flag = True
                if data['lang'] == 'ko':
                    with open(topic_name+'-ko.json', 'a') as f:
                        f.write(jsonpickle.encode(data, unpicklable=False) + '\n')
                        flag = True
                if data['lang'] == 'es':
                    with open(topic_name+'-es.json', 'a') as f:
                        f.write(jsonpickle.encode(data, unpicklable=False) + '\n')
                        flag = True
                if data['lang'] == 'tr':
                    with open(topic_name+'-tr.json', 'a') as f:
                        f.write(jsonpickle.encode(data, unpicklable=False) + '\n')
                        flag = True
    except BaseException as e:
        print("Error on_data: %s" % str(e))
    return flag


def fetch_twitter_data():
    # Replace the API_KEY and API_SECRET with your application's key and secret.
    API_KEY = "9ZxyM3MhFBcvIDTJcMAUucZLW"
    API_SECRET = "FfIqwxe18ZQy6IJeyawFmlYhuSr9Uf3DTTa2xEQImcb9ujqyut"

    searchQuery = 'iPhone 7' # this is what we're searching for
    maxTweets = 100000 # Some arbitrary large number
    tweetsPerQry = 100  # this is the max the API permits
    topic_name = 'iPhone' # We'll store the tweets in a text file.

    sinceId = None
    max_id = -1
    tweetCount = 0

    auth = tweepy.AppAuthHandler(API_KEY, API_SECRET)
 
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
 
    if (not api):
        print ("Can't Authenticate")
        sys.exit(-1)


    print("Downloading max {0} tweets".format(maxTweets))
    while tweetCount < maxTweets:
        try:
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry)
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry, since_id=sinceId)
            else:
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry, max_id=str(max_id - 1))
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry, max_id=str(max_id - 1), since_id=sinceId)
            if not new_tweets:
                print("No more tweets found")
                break
            for tweet in new_tweets:
                is_original = process_or_store(tweet._json, topic_name)
                if(is_original):
                    tweetCount += 1
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            # Just exit if any error
            print("some error : " + str(e))
            break
        print("Downloaded {0} tweets".format(tweetCount))

    print ("Downloaded {0} tweets, Saved to {1}".format(tweetCount, fName))

if __name__ == '__main__':
    fetch_twitter_data()
