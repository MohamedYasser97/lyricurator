import tweepy
from datetime import datetime
from tweet_util import *


# Authenticate Twitter account
auth = tweepy.OAuthHandler('ddnsdyRVRFLjPFsfbIV7kCgo0',
                           'UCv62xY76M0AMFULs9BFRGrhZuj4RM2wvkT9PwRpToqEOGkSYJ')

auth.set_access_token('1223203700040175616-rmVFV5k7P13QMwxwRlArta6agtmD2I',
                      'D25aILraVldNYeij3tQNk6Tyfgeh19a45ogq4COXHKKZD')

api = tweepy.API(auth)

artist, song_name, lyrics = prepare_tweet_content()

tweet = get_tweet_string(artist, song_name, lyrics)

# Send the tweet
api.update_status(tweet)

now = datetime.now()
print('Tweet Sent | ' + now.strftime("%d/%m/%Y %H:%M:%S"))
print('-' * 35)

