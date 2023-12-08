"""
Database Query Script

This script provides functions to query a music database and retrieve song and 
artist information based on the specified mood.
"""

import sqlite3

def query_song(m=None):
    """
    Query the music database and retrieve a random song and artist based on the specified mood.
    
    Args:
    mood (str, optional): The mood for which to retrieve a song. Defaults to None.

    Returns:
    tuple or None: A tuple containing the song name and artist name if a match is found, otherwise None.
    """
    conn = sqlite3.connect("music.db")
    cursor = conn.cursor()
    if m != None:
        cursor.execute(
            "SELECT * \
                    FROM songs \
                    WHERE mood = '{}' \
                    ORDER BY RANDOM() \
                    LIMIT 1".format(
                m
            )
        )
    else:
        cursor.execute(
            "SELECT * \
                       FROM songs \
                       ORDER BY RANDOM() \
                       LIMIT 1"
        )
    query = cursor.fetchall()
    conn.close()
    song_name = query[0][1]
    artist_name = query[0][2]
    return song_name, artist_name
