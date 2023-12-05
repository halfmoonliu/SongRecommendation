import sqlite3
import csv


def create_songs_db(database_file, csv_file):
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY,
            'Song Title' TEXT,
            'Artist Name' TEXT, 
            'Mood' TEXT
        )
        """
    )

    with open(csv_file, "r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            cursor.execute(
                "INSERT INTO songs ('Song Title', 'Artist Name', 'Mood') VALUES (?, ?, ?)",
                (row[0], row[1], row[2]),
            )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    database_file = "songs.db"
    csv_file = "music_data.csv"
    create_songs_db(database_file, csv_file)
