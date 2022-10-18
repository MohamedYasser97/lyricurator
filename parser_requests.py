import bs4
import re

def extract_artist(req):
    scraped_objects = bs4.BeautifulSoup(req.content, "html.parser")
    
    artists_links = []

    for div in scraped_objects.find_all('div',
                                        {'class': 'container main-page'}):
        links = div.find_all('a')

        for a in links:
            artists_links.append(a['href'])
            
    return artists_links

def extract_artist_name(req):
    scraped_objects = bs4.BeautifulSoup(req.content, "html.parser")
    artist_name = ''

    for strong in scraped_objects.find_all('strong'):
        if strong.parent.name == 'h1':
            artist_name = strong.text.strip()
            break

    artist_name = artist_name.rsplit(' ', 1)[0]  # Delete the last word 'Lyrics'

def extract_songs(req):
    scraped_objects = bs4.BeautifulSoup(req.content, "html.parser")
    songs = []

    for div in scraped_objects.find_all('div', {'class': 'listalbum-item'}):
        links = div.find_all('a')

        for a in links:
            songs.append((a.text.strip(), a['href'].split('/', 1)[1]))
    
    return songs

def extract_lyrics(req):
    scraped_objects = bs4.BeautifulSoup(req.content, "html.parser")

    lyrics = scraped_objects.find_all('div', attrs={'class': None, 'id': None})

    lyrics = [line.getText() for line in lyrics]
    lyrics = ''.join(lyrics)  # Converting the list to a string
    lyrics = lyrics.split('\n\n')  # Splitting lyrics to individual blocks
    lyrics = [line.strip() for line in lyrics]  # Removing edge spaces

    temp_lyrics = []

    # Removing square brackets
    for line in lyrics:
        formatted_line = re.sub(r'\[.*?\]', '', line)
        formatted_line = formatted_line.strip()

        if formatted_line != '':
            temp_lyrics.append(formatted_line)

    lyrics = temp_lyrics
    temp_lyrics = []

    # Splitting each block into lines
    for block in lyrics:
        temp_lyrics.append(block.split('\n'))

    lyrics = []

    # Last check for special characters
    for block in temp_lyrics:
        temp_block = []
        for line in block:
            formatted_line = line.replace('\r', '')
            formatted_line = formatted_line.replace('\t', '')
            formatted_line = formatted_line.replace('\n', '')
            formatted_line = formatted_line.replace('\\', '')

            if formatted_line != '':
                temp_block.append(formatted_line)

        lyrics.append(temp_block)
    
    return lyrics

def extract_all_artists(req):
    
    scraped_objects = bs4.BeautifulSoup(req.content, "html.parser")
    artists = []

    for div in scraped_objects.find_all('div',
                                        {'class': 'container main-page'}):
        links = div.find_all('a')

        for a in links:
            artists.append(a.string)
            
    return artists

def extract_all_songs(req):
    soup = bs4.BeautifulSoup(req.content, 'html.parser')

    return soup.find_all('div', class_='listalbum-item') 

def extract_hot_songs(req):
    scraped_objects = bs4.BeautifulSoup(req.content, "html.parser")

    hot_songs_div = scraped_objects.find_all('div',class_="hotsongs")
    
    hot_songs = []
    
    for div in hot_songs_div:
        links = div.find_all('a')
        for a in links:
            hot_songs.append(a.string)
    
    return hot_songs

def extract_hot_albums(req):
    scraped_objects = bs4.BeautifulSoup(req.content, "html.parser")    
    
    hot_albums_div = scraped_objects.find_all('div',class_="hotalbums")
    hot_albums = []
    
    for div in hot_albums_div:
      album = div.text
      album = album.replace(" \"", " - \"")
      all_albums = album.split("\n")
      for a in all_albums:  
        if a != '':
            hot_albums.append(a)
            
    return hot_albums