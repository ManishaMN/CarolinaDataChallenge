import requests

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

# What do we want to search for?
SONG = "Glamorous"

# Search for song using Search API
r = requests.get(SEARCH_URL + f"?q={SONG}&type=track&limit=1", headers=headers)

# Make sure status code is 200 OK
if r.status_code == 200:
    # Grab and print response
    response = r.json()
    print(response)

    # Make sure keys exist in response
    if "tracks" in response:
        if "items" in response["tracks"]:
            # Obtain track ID
            items = response['tracks']['items']
            track_id = items[0]["id"]

            # Using track ID, get audio features
            r = requests.get(AUDIO_URL + f"/{track_id}", headers=headers)
            print(r)

            # Make sure status code is 200 OK
            if r.status_code == 200:
                # Grab and print response
                audio_json = r.json()
                print(audio_json)