"""
ETL-Query script
"""

from libraries.query import query_song

print("Querying database...")
print(query_song('Chill'))