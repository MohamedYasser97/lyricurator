from lyrics_util import *

artists = get_artists_links()

selected_artist = random.choice(artists)

print(selected_artist)
print(get_artist_name_and_song(selected_artist))
