import json
import tweepy
import sys
from datetime import datetime
from lyrics_util import get_artists_links
from tweet_util import *
from console_args import CONSOLE_ARGS, PARSER

def main():
    """ Main program. """
    if CONSOLE_ARGS.listartists:
        artist_links = get_artists_links()
        artist_names = [(x.rsplit('/',1)[1]).rsplit('.',1)[0] for x in artist_links]
        print(*artist_names, sep='\n')
        sys.exit()

    try:
        if CONSOLE_ARGS.notwitter and CONSOLE_ARGS.fullsong:
            artist, song_name, lyrics = prepare_tweet_content(full_song=True)
            tweet = get_tweet_string(artist, song_name, lyrics)
            print(tweet)
        elif CONSOLE_ARGS.fullsong:
            CONSOLE_ARGS.notwitter=True
            artist, song_name, lyrics = prepare_tweet_content(full_song=True)
            tweet = get_tweet_string(artist, song_name, lyrics)
            print(tweet)
            print("\nFull song lyrics can't be tweeted")
        elif CONSOLE_ARGS.notwitter:
            artist, song_name, lyrics = prepare_tweet_content()
            tweet = get_tweet_string(artist, song_name, lyrics)
            print(tweet)
        elif CONSOLE_ARGS.listsongs and CONSOLE_ARGS.artist:
            songs = get_songs_from_artist(CONSOLE_ARGS.artist)
            print("Artist: " + CONSOLE_ARGS.artist)
            print(*songs, sep = "\n")
        elif CONSOLE_ARGS.listsongs:
            random_artist = get_random_artist()
            songs = get_songs_from_artist(random_artist)
            print("Artist: " + random_artist)
            print(*songs, sep = "\n")
        elif CONSOLE_ARGS.twitter:
            artist, song_name, lyrics = prepare_tweet_content()
            tweet = get_tweet_string(artist, song_name, lyrics)
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
        else:
            PARSER.print_help()
    except requests.ConnectionError:
        now = datetime.now()
        print('Connection Error | ' + now.strftime("%d/%m/%Y %H:%M:%S"))
    except tweepy.error.TweepError:
        now = datetime.now()
        print('Tweet Error | ' + now.strftime("%d/%m/%Y %H:%M:%S"))
        

if __name__ == "__main__":
    if CONSOLE_ARGS.interval:
        minutes = CONSOLE_ARGS.interval
        try:
            while True:
                print(f"\n---Delivering lyrics every {minutes} minute(s), Ctrl+C to quit---\n")
                main()
                time.sleep(minutes * 60)
        except KeyboardInterrupt:
            pass
    else:
        main()
