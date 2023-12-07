import base64
from dotenv import load_dotenv
import json
import os
from requests import get, post, exceptions

# load variables stored in .env file
load_dotenv()
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")


def get_token():
    """
    This function outputs token for spotify access
    """
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"grant_type": "client_credentials"}
    try:
        result = post(url, headers=headers, data=data, timeout=10)
        json_result = json.loads(result.content)
        token = json_result["access_token"]
        return token
    except exceptions.Timeout:
        print("Timed out. Server did not respond.")
        return None


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def search_for_track(token, artist_name=None, song_name=None):
    """
    This function searches for a track on Spotify.
    input: artist name and song name, default None
    output: URL to the track on Spotify
    """
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)

    # Check if both artist_name and song_name are provided
    if artist_name is not None and song_name is not None:
        query = f"?q=artist:{artist_name} track:{song_name}&type=track&limit=1"
    elif artist_name is not None:
        query = f"?q=artist:{artist_name}&type=track&limit=1"
    elif song_name is not None:
        query = f"?q=track:{song_name}&type=track&limit=1"
    else:
        print(
            "Both artist_name and song_name are None. Please provide at least one of them."
        )
        return None

    query_url = url + query

    try:
        result = get(query_url, headers=headers, timeout=10)
    except exceptions.Timeout:
        print("Timed out. Server did not respond.")
        return None

    json_result = json.loads(result.content)

    # Check if any tracks are found
    if (
        "tracks" in json_result
        and "items" in json_result["tracks"]
        and json_result["tracks"]["items"]
    ):
        output_url = json_result["tracks"]["items"][0]["external_urls"]["spotify"]
        return output_url
    else:
        print("No soundtrack found...")
        return None
