import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import requests
from collections import Counter

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id='d63ff14ecce546f5ad7910d8fc44d12a',
    client_secret='51325a6b4f9647d39274a35a43c0aa28',
    redirect_uri='http://localhost:8888/callback',
    scope='playlist-read-private playlist-read-collaborative'
))

playlists = {
    "Top 50 Global": "6xhKYqOq4z1mTkZOiIW7Ot",
    "Pop Rising": "3K2bOq8IANH2Xja2g7R9TJ",
    "Hot Country": "5Q5BgwXEBUp31hxkvdsUeI",
    "New Music Friday": "4pJDMa48LhSSi0e5HW63o5"
}

artist_first_names = []
for name, playlist_id in playlists.items():
    try:
        results = sp.playlist_tracks(playlist_id, limit=50, market='US')
        for item in results['items']:
            track = item['track']
            if not track:
                continue
            for artist in track['artists']:
                artist_name = artist['name']
                first_name = artist_name.split(" ")[0].lower()
                artist_first_names.append(first_name)
    except spotipy.exceptions.SpotifyException as e:
        print(f"Error with playlist {name}: {e}")

gender_counts = Counter()
seen_names = set()

for name in set(artist_first_names):
    if name in seen_names:
        continue
    seen_names.add(name)

    try:
        res = requests.get(f"https://api.genderize.io?name={name}")
        if res.status_code == 200:
            gender = res.json().get("gender") or "unknown"
        else:
            gender = "unknown"
    except Exception as e:
        gender = "unknown"

    with open("output.txt", "w") as f:
        print(f"{name.capitalize()} → {gender}")
        f.write(f"{name.capitalize()} → {gender}")
    gender_counts[gender] += 1
    time.sleep(1)

total = sum(gender_counts.values())

with open("output.txt", "w") as f:
    for gender, count in gender_counts.items():
        label = "Unknown" if gender is None else gender.capitalize()
        pct = (count / total) * 100 if total else 0
        line = f"{label}: {count} ({pct:.1f}%)"
        print(line)
        f.write(line + "\n")
