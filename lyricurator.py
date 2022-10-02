import argparse
import json
import tweepy
from datetime import datetime
from tweet_util import *

try:
    parser = argparse.ArgumentParser()
    parser.add_argument('-nt', '--notwitter', action= 'store_true', help='Prints lyrics to console instead of tweeting them')
    args = parser.parse_args()

    artist, song_name, lyrics = prepare_tweet_content()

    tweet = get_tweet_string(artist, song_name, lyrics)

    if args.notwitter:
        print(tweet)
    else:
        with open("auth.json", "r") as f:
            auth_creds = json.load(f)

        # Authenticate Twitter account
        auth = tweepy.OAuthHandler(auth_creds['api_key'], auth_creds['api_key_secret'])

        auth.set_access_token(auth_creds['access_token'], auth_creds['access_token_secret'])

        api = tweepy.API(auth)

        # Send the tweet
        api.update_status(tweet)

        now = datetime.now()
        print('Tweet Sent | ' + now.strftime("%d/%m/%Y %H:%M:%S"))
        print('-' * 40)
except requests.ConnectionError:
    now = datetime.now()
    print('Connection Error | ' + now.strftime("%d/%m/%Y %H:%M:%S"))
except tweepy.error.TweepError:
    now = datetime.now()
    print('Tweet Error | ' + now.strftime("%d/%m/%Y %H:%M:%S"))
