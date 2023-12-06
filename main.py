from pprint import pprint

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from  scrapping import scrapping

# Create a Spotify account, then create an app from spotify for developer. After the creation, you will get the below elements
CLIENT_ID = "Use your own client id from spotify"
CLIENT_SECRET = "Use your own client secret from spotify"


# Scrapping part
period =input("What year do you vwant travel? Type date in this format YYYY-MM-DD : " )
link_request = f"https://www.billboard.com/charts/hot-100/{period}/"
song_title = scrapping(link_request)


# Spotify part

print("Spotify start")
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id= CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="https://www.google.com/",
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"
                                               ))
# Song search
song_urls = []
year = period.split("-")[0]
for song in song_title:
    result = sp.search(q=f"track:{song} year:{year}", type="track")

    try:
        url = result["tracks"]["items"][0]["external_urls"]["spotify"]
    except IndexError :
        continue
    else:
        song_urls.append(url)
# print(song_urls)

# Create playlist

user_id = sp.me()["id"]
playlist_name = f"{period} Bill Board 100"
playlist= sp.user_playlist_create(user_id, playlist_name, public= False)

# Add song to the playlist

sp.playlist_add_items(playlist["id"], song_urls)