import json
import os
from pathlib import Path

from dotenv import load_dotenv, set_key
from .models import ArtistDetails, Artist

# from requests import Session
from .http import HTTPClient


class MonstercatAPI:
    BASE = "https://player.monstercat.app/api/"
    SIGN_IN = BASE + "sign-in"
    ARTISTS = BASE + "artists"
    ARTIST = BASE + "artist/{artist_uri}"

    def __init__(self, config_path: Path = Path(".env")):
        self.client = HTTPClient(config_path=config_path)

    def sign_in_email(self, email: str = None, password: str = None):
        if self.client.has_cookies():
            print("Using cookie from .env")
            self.client.import_cookies()
            return None

        payload = {"Email": email, "Password": password}
        url = self.SIGN_IN
        response = self.client.post(
            url=url,
            json=payload,
        )

        if response.status_code == 200:
            print("Sign in successful")
            self.client.export_cookies()
            return True
        else:
            print("Sign in failed")
            return False

    def get_artists(
        self,
        limit: int = 100,
        offset: int = 0,
        search: str = "",
    ):
        url = self.ARTISTS
        params = {
            "limit": limit,
            "offset": offset,
            "search": search,
        }
        response = self.client.get(url=url, params=params)
        if response.status_code != 200:
            return None
        artists = [
            Artist.from_dict(artist) for artist in response.json()["Artists"]["Data"]
        ]
        return artists

    def get_artist(
        self,
        artist_uri: str,
    ):
        url = self.ARTIST.format(artist_uri=artist_uri)
        response = self.client.get(url=url)
        if response.status_code != 200:
            return None
        artist = Artist.from_dict(response.json())
        return artist
