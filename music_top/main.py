# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
#
# sp = spotipy.Spotify(
#     auth_manager=SpotifyOAuth(
#         scope="playlist-modify-private",
#         redirect_uri="http://example.com/callback/",
#         client_id='47d78ab4264047b09ec4874ecfc8ee95',
#         client_secret='f70fc65eecac45fda0f7c74213fb5c2e',
#         show_dialog=True,
#         cache_path="token.txt"
#     )
# )
# user_id = sp.current_user()["id"]
import sp as sp
from bs4 import BeautifulSoup
import requests




BILLBOARD_HOT_TOP_100_URL = "https://www.billboard.com/charts/hot-100/"

date = input("Which year do you want to travel to? type the date in this format 'YYYY-MM-DD':\n")
response = requests.get(url=BILLBOARD_HOT_TOP_100_URL + date)
html_page = response.text
soup = BeautifulSoup(html_page, "html.parser")

all_songs = soup.select(".a-no-trucate")
data_list = [record.getText().strip() for record in all_songs]
user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

