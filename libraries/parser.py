import random
from libraries.query import query_song

def parse_song(response):
    '''
    This function parses a text response from chatGPT and 
    returns a song name and aartist name 
    input: a string of chatGPT response
    output: a tuple of (song name, artist name), both are strings
    '''
    sentences = [x.split(" ") for x in response.split("\n")]
    song_artist_l = list()
    for sent in sentences:
        song_artist = tuple()
        split_ind = None
        song_name, artist_name = None, None
        if len(sent) <= 1:
            pass
        else:
            for i in range(len(sent)):
                if sent[i] == "by":
                    split_ind = i
                elif sent[i] == "-":
                    split_ind = i
        if split_ind != None:
            song_name = " ".join(sent[1:split_ind])
            if song_name[0] == '"':
                song_name = song_name[1:]
            if song_name[-1] == '"':
                song_name = song_name[:-1]
            artist_name = " ".join(sent[split_ind+1:])
        if song_name != None or artist_name != None:
            song_artist = (song_name, artist_name)
            song_artist_l.append(song_artist)
    if len(song_artist_l) == 0:
        return query_song()
    else:
        return random.choice(song_artist_l)
    