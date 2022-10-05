import time
from lyrics_util import *
from console_args import CONSOLE_ARGS


def prepare_tweet_content(full_song=False):
    while True:
        time.sleep(3)
        artists = get_artists_links()

        if not artists:
            continue

        try:
            if CONSOLE_ARGS.artist:
                selected_artist = CONSOLE_ARGS.artist[0].lower() + '/' + CONSOLE_ARGS.artist.lower() + '.html'
                print(selected_artist)
            else:
                selected_artist = random.choice(artists)
        except IndexError:
            continue

        # 'selected_song' is a tuple where 1st is song name and 2nd is its link
        artist_name, selected_song = get_artist_name_and_song(selected_artist)

        if not artist_name or not selected_song:
            continue

        song_lyrics = get_lyrics(selected_song[1])

        if not song_lyrics:
            continue
        if full_song:
            full_lyrics=get_full_lyrics(song_lyrics)
            return artist_name,selected_song[0],full_lyrics

        lyrics_portion = get_lyrics_portion(song_lyrics)

        if lyrics_portion:
            return artist_name, selected_song[0], lyrics_portion


def get_tweet_string(artist_name, song_name, lyrics):
    tweet = '\n'.join(lyrics)
    tweet += '\n\n'
    tweet += artist_name + ' - ' + song_name

    return tweet
