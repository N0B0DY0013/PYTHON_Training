import os
import requests
import spotipy
import dotenv
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

year_ = input("What year would you like to to create your playlist? ")

response = requests.get(f"https://www.billboard.com/charts/year-end/{year_}/hot-100-songs/", headers = {"User-Agent": "Mozilla/5.0"})
response.raise_for_status()

dotenv.load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_USER = os.getenv("SPOTIFY_USER")
scope = "user-library-read playlist-read-private playlist-modify-private playlist-modify-public playlist-read-collaborative"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id = SPOTIFY_CLIENT_ID,
                                               client_secret = SPOTIFY_CLIENT_SECRET,
                                               redirect_uri = "http://example.com",
                                               scope = scope))

playlists = [item["name"] for item in sp.user_playlists(user = SPOTIFY_USER)["items"] if item != None] 

playlist_name = f"{year_} Billboard 100"

if playlist_name not in playlists:

    song_rows =  BeautifulSoup(response.text, "html.parser").select(selector = ".o-chart-results-list-row-container > .o-chart-results-list-row > .lrv-u-width-100p > .lrv-a-unstyle-list")

    song_list = []
    song_artist = []

    for row in song_rows:
        song_list.append(BeautifulSoup(str(row), "html.parser").select_one(selector=".o-chart-results-list__item > #title-of-a-story").getText().strip())
        song_artist.append(BeautifulSoup(str(row), "html.parser").select_one(selector=".o-chart-results-list__item > .c-label").getText().strip())

    spotify_URI = []

    for i in range(0, len(song_list)):
        search_result = sp.search(q = f"track: {song_list[i]} year: {year_} artist: {song_artist[i]}", 
                                  limit = 1)
        spotify_URI.append(search_result["tracks"]["items"][0]["uri"])
        
    created_playlist = sp.user_playlist_create(user = SPOTIFY_USER, name = playlist_name)
    
    sp.playlist_add_items(playlist_id = created_playlist["id"],
                          items = spotify_URI)
    print("Done!")
    
else:
    print("Playlist already exists!")
