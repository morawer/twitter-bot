import time
import requests
import tweepy, os, json

def dogeCoinFunction():

    twitter_Api = os.environ.get('Twitter_API')
    twitter_Secret_Api = os.environ.get('Twitter_Secret_API')
    acces_Twitter = os.environ.get('Twitter_Access')
    access_Twitter_Secret = os.environ.get('Twitter_Access_Secret')

    auth = tweepy.OAuthHandler(twitter_Api, twitter_Secret_Api)
    auth.set_access_token(acces_Twitter, access_Twitter_Secret)

    api = tweepy.API(auth)

    tweetL = api.user_timeline(screen_name='elonmusk', tweet_mode="extended", exclude_replies=True)
    time.sleep(1)
    lastTweet = tweetL[0].full_text
    
    words = ['dogecoin', 'Dogecoin', 'DOGECOIN', 'DOGE', 'doge', 'DOG', 'dog']

    for i in range(len(words)):
        if words[i] in lastTweet:
            return True
    
    return False    

print(dogeCoinFunction())
    