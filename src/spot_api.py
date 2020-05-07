# -*- encoding: utf-8 -*-

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

from config import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET


spot_api = spotipy.Spotify(
    client_credentials_manager=SpotifyClientCredentials(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET))


def query_music_duration(artist, music):
    if isinstance(artist, str) and isinstance(music, str):
        results = spot_api.search(q=artist, limit=50)
    else:
        raise Exception('Artist or Music is not valid')

    for track in results['tracks']['items']:
        if track['name'].lower() == music.lower():
            return track['duration_ms'] // 1000, track['name']
    else:
        raise Exception('Artist or Music not found')
