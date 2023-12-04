"""Query the database"""

import sqlite3


# Now you can run queries like this:

def query_song(m=None):    
    '''
    This function takes in a "mood" as input and
    query the music database and
    returns a song name and artist name 
    input: a string of mood (e.g. "Chill")
    output: a tuple of (song name, artist name), both are strings
    '''
    conn = sqlite3.connect("music.db")
    cursor = conn.cursor()   
    if m != None:
        cursor.execute("SELECT * \
                    FROM songs \
                    WHERE mood = '{}' \
                    ORDER BY RANDOM() \
                    LIMIT 1".format(m))
    else:
        cursor.execute("SELECT * \
                       FROM songs \
                       ORDER BY RANDOM() \
                       LIMIT 1")
    query = cursor.fetchall()
    conn.close()
    song_name = query[0][1]
    artist_name = query[0][2]
    return song_name, artist_name