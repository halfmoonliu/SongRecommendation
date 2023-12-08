"""
App Script

This script defines our Streamlit app, 'JAMB-O', a mood-based music recommendation app. 
It allows users to either record their voice to generate a song recommendation using 
GPT-3 or choose a mood from a dropdown to get a song recommendation based on their 
mood. The script integrates with the Spotify API for music playback and uses various 
modules for speech-to-text, natural language processing, and database queries.

Authors: Bob Zhang, Jiwon Shin, Yun-Chung Liu (Murphy), Afraa Noureen 
"""
import os
import streamlit as st
from dotenv import load_dotenv
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from loguru import logger
from libraries._01_speech_to_text import recordingVoice, transcribe_audio
from libraries._02_gpt_prompt import get_resp_gpt
from libraries._03_spotify_functionality import get_token, search_for_track
from libraries._04_query import query_song
from libraries._05_parser import parse_song

# Configure Loguru logger
log_format = (
    "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
    "<level>{level: <8}</level> | "
    "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
    "<level>{message}</level>"
)
logger.add("logging.md", format=log_format, level="INFO")

# Load environment variables from .env file
load_dotenv()

# Load Spotify API credentials from environment variables
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

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
logger.info("Streamlit app started.")

st.markdown(
    """
    <style>
        body {
            background-color: #000000;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #d2b48c;
        }
        .stApp {
            max-width: 800px;
            margin: 0 auto;
        }
        .btn-primary:hover {
            background-color: #d2b48c !important;
        }
        .heading {
            background-color: #8b735b;
            border-radius: 20px;
            padding: 2em;
            margin-bottom: 2em;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="heading">
        <h1 style="font-size: 3em;">✨ Welcome to JAMB-O ✨</h1>
        <h3 style="font-size: 2em;">Your Mood-based Music Recommendation App!</h3>
    </div>
    """,
    unsafe_allow_html=True,
)

# Get Spotify access token
token = get_token()
logger.info("Spotify access token retrieved.")

# User Option: Choose between Option 1 and Option 2
option_choice = st.radio(
    "Take your pick:", ["Tell us how you feel!", "Choose your mood!"]
)

if option_choice == "Tell us how you feel!":
    logger.info("Option chosen: Tell us how you feel.")
    st.subheader("Tell us how you feel today, and we'll give you a song! 🎵")
    if st.button(
        "🎙️ Record Voice", key="record-voice", help="Click to record your voice"
    ):
        logger.info("Recording voice.")
        with st.spinner("Recording..."):
            audio_data = recordingVoice()

        with st.spinner("Awesome! Finding your mood song 😉"):
            transcription = transcribe_audio(audio_data)
            song_recommendation = get_resp_gpt(transcription, OPENAI_API_KEY)
            song_artist_gpt = parse_song(song_recommendation)

        if song_artist_gpt[0] and song_artist_gpt[1]:
            logger.info("Song recommendation successfully parsed.")
            song_name_gpt, artist_name_gpt = song_artist_gpt
            st.write(f"Now Playing: {song_name_gpt} by {artist_name_gpt}")
            spotify_url_gpt = search_for_track(token, artist_name_gpt, song_name_gpt)

            if spotify_url_gpt:
                logger.info("Spotify track found for GPT recommendation.")
                st.markdown(
                    f'<iframe src="https://open.spotify.com/embed/track/{spotify_url_gpt.split("/")[-1]}" width="300" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>',
                    unsafe_allow_html=True,
                )
            else:
                logger.warning("Song not found on Spotify. Fallback to DB for Option 1.")
                song_name_db, artist_name_db = query_song(song_recommendation)
                spotify_url_db = search_for_track(token, artist_name_db, song_name_db)

                if spotify_url_db:
                    logger.info("Spotify track found in the database for Option 1.")
                    st.markdown(
                        f'<iframe src="https://open.spotify.com/embed/track/{spotify_url_db.split("/")[-1]}" width="300" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>',
                        unsafe_allow_html=True,
                    )
                else:
                    logger.warning("Song not found in the database for Option 1.")
                    st.warning("Song not found in the database for Option 1.")

elif option_choice == "Choose your mood!":
    logger.info("Option chosen: Choose your mood.")
    st.subheader("Choose your mood from the dropdown, and we'll give you a song! 🎶")
    mood_options = ["Happy", "Sad", "Energetic", "Calm", "Anxious", "Chill"]
    selected_mood = st.selectbox("Select Mood:", mood_options)

    if st.button(
        "🎧 Get Song (By Mood)",
        key="get-song-preview",
        help="Click to get song preview",
    ):
        logger.info(f"Getting song preview for selected mood: {selected_mood}.")
        with st.spinner("Finding your mood's song!"):
            song_name_mood, artist_name_mood = query_song(selected_mood)
            spotify_url_mood = search_for_track(token, artist_name_mood, song_name_mood)

        if spotify_url_mood:
            logger.info("Spotify track found for mood.")
            st.markdown(
                f'<iframe src="https://open.spotify.com/embed/track/{spotify_url_mood.split("/")[-1]}" width="300" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>',
                unsafe_allow_html=True,
            )
        else:
            logger.warning("Song not found on Spotify.")
            st.warning("Song not found on Spotify.")
