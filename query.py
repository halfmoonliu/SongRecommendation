"""
ETL-Query script
"""

from libraries.query import query_song
from libraries.parser import parse_song

print("Querying database...")
print(query_song('Chill'))

example1 = "shall I compare thee to a summer's day?"
print(parse_song(example1))


example2 = """
1. "One of Us" - Joan Osborne
2. "Someone Like You" - Adele
3. "It's Gonna be Alright" - Marvin Gaye
4. "Ain't No Sunshine" - Bill Withers
5. "Hallelujah" - Jeff Buckley
6. "What a Wonderful World" - Louis Armstrong
7. "I Will Survive" - Gloria Gaynor
8. "Daughters" - John Mayer
9. "Lean on Me" - Bill Withers
10. "I'm Not the Only One" - Sam Smith
"""

print(parse_song(example2))
