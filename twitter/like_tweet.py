#Possibly doesn't work because of Elon Musk, will update it soon

# This bot likes tweet on behalf of you based upon the search list you enter inside the list on line 24
import tweepy
from time import sleep
from datetime import datetime, timedelta
import random

# Add your token keys from Twitter Developer Portal
# https://developer.twitter.com/en/apply-for-access
consumer_key = ''
consumer_secret = ''
key = ''
secret = ''

# Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

d = datetime.today() - timedelta(hours=0, minutes=30)

d = d.strftime("%Y/%m/%d %H:%M:%S")

# Add your searching preference over here
search_list = ['anime','#animetwt','#anime']

def like_tweet():
    global search_list

    try:
        # This will randomly select any one search query from the search_list
        tweets = tweepy.Cursor(api.search_tweets,q=random.choice(search_list), since_id=d, lang="en", result_type='recent').items(1)
        search_results = [tweet for tweet in tweets]

        for tweet in search_results:
            print('\n---------------')
            print('Username:',tweet.user.screen_name)
            print('Followers: ',tweet.user.followers_count)
            print('text: ',str(tweet.text)[0:40].replace("\n", "") + '...')

            # This will like the selected tweet
            api.create_favorite(tweet.id)

            print('tweet liked')
            print('---------------\n')

            # You can either use sleep and pass the seconds to stop the execution of the code or use any scheduler function
            print('sleeping for 300 seconds..')
            for countdown in range(0,300): 
                print(countdown, end='\r')
                sleep(1)
            
    except Exception as e:
        print(e)
        pass

while 1:
    like_tweet()
