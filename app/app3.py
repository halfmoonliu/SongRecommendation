import streamlit as st
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from my_parser import parse_song, query_song
from spotifyFunc import get_token, search_for_track
from speech2text import recordingVoice, transcribe_audio
from GPT_prompt import get_resp_gpt
import os

# Load Spotify API credentials from environment variables
SPOTIPY_CLIENT_ID = "YOUR_CLIENT_ID"
SPOTIPY_CLIENT_SECRET = "YOUR_CLIENT_SECRET"
SPOTIPY_REDIRECT_URI = "YOUR_REDIRECT_URI"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

# Authenticate with Spotify API
sp = Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope="user-library-read",
    )
)

# Streamlit App
st.title("Spotify Song Player")

# Get Spotify access token
token = get_token()

# User Option: Speech Input
st.subheader("Option 1: Enter Song Details through Voice")
if st.button("Record Voice"):
    recordingVoice()
    st.success("Voice recording complete!")

    # Transcribe the voice recording
    transcription = transcribe_audio("output.wav")

    # Use GPT for song recommendation
    song_recommendation = get_resp_gpt(transcription, OPENAI_API_KEY)
    st.write(f"Song Recommendation: {song_recommendation}")

    # Extract song and artist from GPT response
    song_artist_gpt = parse_song(song_recommendation)
    if song_artist_gpt[0] and song_artist_gpt[1]:
        artist_name_gpt, song_name_gpt = song_artist_gpt
        st.write(f"Searching for: {song_name_gpt} by {artist_name_gpt}")
        spotify_url_gpt = search_for_track(token, artist_name_gpt, song_name_gpt)
        st.write(f"Spotify URL: {spotify_url_gpt}")

        if spotify_url_gpt:
            st.success("Song Found! Play it below:")
            st.markdown(
                f'<iframe src="https://open.spotify.com/embed/track/{spotify_url_gpt.split("/")[-1]}" width="300" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>',
                unsafe_allow_html=True,
            )
        else:
            st.warning("Song not found on Spotify.")

# User Option: Mood Dropdown
st.subheader("Option 2: Select Mood from Dropdown")
mood_options = ["Happy", "Sad", "Energetic", "Calm", "Anxious", "Chill"]
selected_mood = st.selectbox("Select Mood:", mood_options)
if st.button("Get Song Preview (By Mood)"):
    song_name_mood, artist_name_mood = query_song(selected_mood)
    st.write(f"Song for Mood '{selected_mood}': {song_name_mood} by {artist_name_mood}")
    spotify_url_mood = search_for_track(token, artist_name_mood, song_name_mood)
    st.write(f"Spotify URL: {spotify_url_mood}")

    if spotify_url_mood:
        st.success("Song Found! Play it below:")
        st.markdown(
            f'<iframe src="https://open.spotify.com/embed/track/{spotify_url_mood.split("/")[-1]}" width="300" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>',
            unsafe_allow_html=True,
        )
    else:
        st.warning("Song not found on Spotify.")
