import json
import os
from pathlib import Path

from dotenv import load_dotenv, set_key
import httpx

from .exceptions import ConfigHasNoCreds
from .models import ArtistDetails, Artist

# from requests import Session
from .http import HTTPClient


class MonstercatAPI:
    BASE = "https://player.monstercat.app/api/"
    CDX = "https://cdx.monstercat.com"
    SIGN_IN = BASE + "sign-in"
    ARTISTS = BASE + "artists"
    ARTIST = BASE + "artist/{artist_uri}"
    ARTIST_PHOTO = "https://www.monstercat.com/artist/{artist_uri}/photo"

    def __init__(self, config_path: Path):
        self.client = HTTPClient(config_path=config_path)

    def sign_in_email(
        self, email: str | None = None, password: str | None = None
    ) -> bool:
        if email is not None and password is not None:
            print("Setting email and password in yaml config.")
            self.client.set_email(email)
            self.client.set_password(password)
        elif email is None or password is None:
            print("Loading email and password from yaml config.")
            if self.client.has_cookies():
                print("Using cookie from yaml config.")
                self.client.import_cookies()
                return True
            elif not self.client.has_creds():
                raise ConfigHasNoCreds(
                    f"No credentials found in {self.client.get_config_path().name}."
                )

        payload = {
            "Email": self.client.get_email(),
            "Password": self.client.get_password(),
        }
        url = self.SIGN_IN
        response = self.client.post(
            url=url,
            json=payload,
        )

        if response.status_code == 200:
            print("Sign in successful")
            self.client.save_config()
            self.client.export_cookies()
            return True

        print("Sign in failed")
        self.client.remove_creds()
        self.client.remove_cookies()
        return False

    def get_artists(
        self,
        limit: int = 100,
        offset: int = 0,
        search: str = "",
    ) -> list[Artist] | None:
        url = self.ARTISTS
        params = {
            "limit": limit,
            "offset": offset,
            "search": search,
        }
        response = self.client.get(url=url, params=params)
        if response.status_code == 200:
            artists = [
                Artist.from_dict(artist)
                for artist in response.json()["Artists"]["Data"]
            ]
            return artists

    def get_artist(
        self,
        artist_uri: str,
    ) -> Artist | None:
        url = self.ARTIST.format(artist_uri=artist_uri)
        response = self.client.get(url=url)
        if response.status_code == 200:
            artist = Artist.from_dict(response.json())
            return artist

    def get_artist_photo(
        self, artist_uri: str, width: int = 3000, encoding: str = "jpeg"
    ) -> bytes | None:
        url = self.ARTIST_PHOTO.format(artist_uri=artist_uri)

        response = self.client.get(
            url=self.CDX,
            params={"width": width, "encoding": encoding, "url": url},
            follow_redirects=True,
        )

        if response.status_code == 200:
            return self.client.get(str(response.url)).content
