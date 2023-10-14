import requests
import pandas as pd
import csv

# Set constants needed to get access token (redacted for Git)
CLIENT_ID = "CLIENT_ID"
CLIENT_SECRET = "CLIENT_SECRET"
AUTH_URL = 'https://accounts.spotify.com/api/token'

# Get authorization responses
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

auth_response_data = auth_response.json()

# Save token
access_token = auth_response_data['access_token']

# Create headers
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}

# URLs of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'
SEARCH_URL = BASE_URL + "search"
TRACK_URL = BASE_URL + "tracks"
AUDIO_URL = BASE_URL + "audio-features"

# Read Top Songs data
df_top_tracks = pd.read_csv("songs_by_month.csv")
df_top_10_tracks = df_top_tracks[df_top_tracks["position"] <= 10]
df_top_10_tracks = df_top_10_tracks.reset_index(drop=True)

# Make list to hold dictionaries to convert to CSV later
to_csv = []

# Save different columns to help creating final CSV
songs = df_top_10_tracks["song"]
artists = df_top_10_tracks["artist"]
months = df_top_10_tracks["month"]
revenues = df_top_10_tracks["indicativerevenue"]
positions = df_top_10_tracks["position"]

# Loop through all songs
for i, song in enumerate(songs):
    # Only obtain songs from 2010 and before
    if (int(months[i][-2:]) <= 10):
        # Give progress
        print(months[i])

        # Search for song using Search API
        r = requests.get(SEARCH_URL + f"?q={song}&type=track&limit=1", headers=headers)

        # Make sure status code is 200 OK
        if r.status_code == 200:
            response = r.json()

            # Make sure keys exist in response
            if "tracks" in response:
                if "items" in response["tracks"]:
                    # Obtain track ID
                    items = response['tracks']['items']
                    track_id = items[0]["id"]

                    # Using track ID, get audio features
                    r = requests.get(AUDIO_URL + f"/{track_id}", headers=headers)

                    # Make sure status code is 200 OK
                    if r.status_code == 200:
                        audio_json = r.json()

                        # Add other fields from original data
                        audio_json["name"] = song
                        audio_json["artist"] = artists[i]
                        audio_json["month"] = months[i]
                        audio_json["revenue"] = revenues[i]
                        audio_json["position"] = positions[i]

                        # Add popularity from track API
                        audio_json["popularity"] = items[0]["popularity"]

                        # Add to list of dicts
                        to_csv.append(audio_json)

# Set keys for header
keys = to_csv[0].keys()

# Write out CSV file using list of dicts
with open("spotify_top10_pop.csv", "w", newline="", encoding="latin") as out:
    # Write header
    writer = csv.DictWriter(out, keys)
    writer.writeheader()

    # Write all other rows
    writer.writerows(to_csv)
