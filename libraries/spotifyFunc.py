import base64
from dotenv import load_dotenv
import json
import os
from requests import get, post, exceptions

#load variables stored in .env file
load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    '''
    This function outputs token for spotify access
    '''
    auth_string = client_id + ":" + client_secret
    auth_bytes  = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    try:
        result = post(url, headers = headers, data = data, timeout=10)
        json_result = json.loads(result.content)
        token = json_result["access_token"]
        return token
    except exceptions.Timeout:
        print("Timed out. Server did not respond.")
        return None

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def search_for_track(token, artist_name=None, song_name=None):
    '''
    This function searches for a track on spotify
    input: artist name and song name, defalut None
    output: url to the track on spotify
    '''
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name, song_name}&type=track&limit=1"
    
    query_url = url + query

    try:
        result = get(query_url, headers = headers, timeout=10)
    except exceptions.Timeout:
        print("Timed out. Server did not respond.")
        
    json_result = json.loads(result.content)
    output_url = json_result['tracks']['items'][0]['external_urls']['spotify']
    
    if len(output_url) == 0:
        print("No soundtrack found...")
        return None
    else:
        return output_url
    
