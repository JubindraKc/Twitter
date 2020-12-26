import tweepy
import time
import random

consumer_key = 'U5ZmE14nlYLLQWAKKVTfRhQ08'
consumer_secret = 'ZutqNtcj3Q8eHFxlApDmnZWicFNdSYcxlrU55jtEnReOC80Fhj'
key = '1264137430937952258-cPObmxCajvlYgmtrLNVny2hMBHMnqT'
secret = 'IAfmf9wJhFBBMRfTQMHzqdSbhedbBMocE7NGe7vbslXAX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


# tag_collection = ['Xiaomi', 'Redmi', 'POCOF2Pro', 'MIUI12', '#MiTrueWirelessEarphones2', 'NoMiWithoutYou', 'XiaomiNepal']
# tag = random.choice(tag_collection)

reply_collection = ['This is a great post!', 'Great Post!', 'Well Said!', 'Great Insight', 'Honestly, this is an excellent tweet!']
reply_this = random.choice(reply_collection)

add_tag = '#BudgetKingXiaomi #XiaomiForever'



def searchbot(number,reply,tag):
    print(number)
    print(tag)
    print(reply)

    tweets = tweepy.Cursor(api.search, str(tag)).items(number)
   
    
    for tweet in tweets:
        try:
            tweet.retweet()
            api.create_favorite(tweet.id)
            print(reply)

            api.update_status("@" + tweet.user.screen_name + " " + reply+ " " +add_tag, tweet.id)
            print('Retweeted!')
            time.sleep(number)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(number)


# searchbot(filename)