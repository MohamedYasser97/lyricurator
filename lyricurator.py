from lyrics_util import *

artists = get_artists_links()

selected_artist = random.choice(artists)

artist_name, selected_song = get_artist_name_and_song(selected_artist)

print(artist_name, selected_song[0], sep=' - ')

song_lyrics = get_lyrics(selected_song[1])

print(song_lyrics)
