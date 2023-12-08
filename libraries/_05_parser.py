"""
Song Parser Script

This script provides a function to parse a text response from chatGPT and retrieve song and artist information. 
It utilizes the 'query_song' function from '_04_query.py' to obtain a random song and artist in case the parsing 
is unsuccessful.
"""
import random
from libraries._04_query import query_song


def parse_song(response):
    """
    Parse a text response from chatGPT and retrieve a song and artist.

    Args:
    response (str): A string of chatGPT response.

    Returns:
    tuple: A tuple containing the parsed song name and artist name. 
    If parsing is unsuccessful, a random song and artist are returned.
    """
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
            artist_name = " ".join(sent[split_ind + 1 :])
        if song_name != None or artist_name != None:
            song_artist = (song_name, artist_name)
            song_artist_l.append(song_artist)
    if len(song_artist_l) == 0:
        return query_song()
    else:
        return random.choice(song_artist_l)
