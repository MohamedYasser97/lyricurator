import random
import string
import http_utils
import parser_requests

base_url = 'https://www.azlyrics.com/'

def get_artists_links():
    available_letters = list(string.ascii_lowercase)
    available_letters.append('19')  # To get artists that start with a number
    selected_letter = random.choice(available_letters)

    url = base_url + selected_letter + '.html'
    
    req = http_utils.request_uri(url)
    
    return parser_requests.extract_artist(req)


def get_artist_name_and_song(artist_link):
    url = base_url + artist_link
    
    req = http_utils.request_uri(url)

    artist_name = parser_requests.extract_artist_name(req)
    songs = parser_requests.extract_songs(req)
    
    try:
        selected_song = random.choice(songs)
    except IndexError:
        selected_song = ''

    if not selected_song:
        return '', ''

    return artist_name, selected_song


def get_lyrics(song_link):
    url = base_url + song_link
    
    req = http_utils.request_uri(url)
    
    return parser_requests.extract_lyrics(req)

def get_lyrics_portion(lyrics):
    selected_block = random.choice(lyrics)

    # The block is already small to begin with
    if len(selected_block) < 3:
        return selected_block

    # Give a minimum choice space of 3 lyric lines. '-2' because exclusive range
    start_index = random.randrange(0, len(selected_block) - 2)

    # Select from 2 to 3 lines (inclusive) from the selected block
    end_index = start_index + random.randrange(1, 3) + 1

    return selected_block[start_index:end_index]

def get_full_lyrics(lyrics):
    full_lyrics=['\n'.join(block) for block in lyrics]
    return full_lyrics

def get_random_artist():
    available_letters = list(string.ascii_lowercase)
    available_letters.append('19')  # To get artists that start with a number
    selected_letter = random.choice(available_letters)

    url = base_url + selected_letter + '.html'
    
    req = http_utils.request_uri(url)
    
    artists = parser_requests.extract_all_artists(req)
    
    selected_artist = random.choice(artists)

    return selected_artist

def get_songs_from_artist(artist):
    artist = artist.lower().replace(" ", "")
    first_char = artist[0]
    url = base_url + first_char + "/" + artist + ".html"
    
    req = http_utils.request_uri(url)

    all_songs = parser_requests.extract_all_songs(req)
    
    songs = []

    for song in all_songs:
        if song.string is not None:
            songs.append(song.string)

    return songs

def get_artist_names():
    artist_links = get_artists_links()
    artist_names = [(x.rsplit('/',1)[1]).rsplit('.',1)[0] for x in artist_links]
    return artist_names

def get_hot_songs():
    req = http_utils.request_uri(base_url)
    
    return parser_requests.extract_hot_songs(req)
    
def get_hot_albums():
    req = http_utils.request_uri(base_url)
    
    return parser_requests.extract_hot_albums(req)
