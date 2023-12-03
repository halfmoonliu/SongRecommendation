"""Query the database"""

import sqlite3


# Now you can run queries like this:

def query_song(m=None):    
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