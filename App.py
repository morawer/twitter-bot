import tweepy, os

def dogeCoinFunction():

    twitter_Api = os.environ.get('Twitter_API')
    twitter_Secret_Api = os.environ.get('Twitter_Secret_API')
    acces_Twitter = os.environ.get('Twitter_Access')
    access_Twitter_Secret = os.environ.get('Twitter_Access_Secret')

    auth = tweepy.OAuthHandler(twitter_Api, twitter_Secret_Api)
    auth.set_access_token(acces_Twitter, access_Twitter_Secret)

    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name='elonmusk', tweet_mode="extended", exclude_replies=True)

    if tweets:
        lastTweet = tweets[0].full_text
        lastTweet = lastTweet.lower()
        print(lastTweet)
    
        words = ['dogecoin', 'doge', 'dog']

        for i in range(len(words)):
            if words[i] in lastTweet:
                return True

    return False