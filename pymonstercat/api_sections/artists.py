from icecream import ic
from httpx import URL
from pymonstercat.api_sections.base import PyMonstercatBase
from pymonstercat.models import Artist
from pymonstercat.models import Release


class PyMonstercatArtists(PyMonstercatBase):
    ARTISTS = PyMonstercatBase.BASE + "artists"
    ARTIST = PyMonstercatBase.BASE + "artist/{artist_uri}"
    ARTIST_RELEASES = ARTIST + "/releases"
    LATEST_ARTISTS = PyMonstercatBase.BASE + "latest-artists"
    ARTIST_PHOTO = "https://www.monstercat.com/artist/{artist_uri}/photo"

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
        response = self.get(url=url, params=params)
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

        response = self.get(url=url)

        if response.status_code == 200:
            artist = Artist.from_dict(response.json())
            return artist

    def get_artist_photo(
        self,
        artist_uri: str,
        width: int = 3000,
        encoding: str = "jpeg",
    ) -> URL | None:
        params = {
            "width": width,
            "encoding": encoding,
            "url": self.ARTIST_PHOTO.format(artist_uri=artist_uri),
        }

        response = self.get(url=self.CDX, params=params, follow_redirects=True)

        if response.status_code == 200:
            return response.url

    def get_artist_releases(
        self,
        artist_uri: str,
        limit: int = 50,
        offset: int = 0,
    ) -> list[Release] | None:
        url = self.ARTIST_RELEASES.format(artist_uri=artist_uri)
        params = {
            "limit": limit,
            "offset": offset,
        }

        response = self.get(url=url, params=params)

        if response.status_code == 200:
            releases = [
                Release.from_dict(release)
                for release in response.json()["Releases"]["Data"]
            ]
            return releases

    def get_latest_artists(
        self,
        limit: int = 100,
        offset: int = 0,
    ) -> list[Artist] | None:
        url = self.LATEST_ARTISTS
        params = {
            "limit": limit,
            "offset": offset,
        }

        response = self.get(url=url, params=params)

        if response.status_code == 200:
            artists = [
                Artist.from_dict(artist)
                for artist in response.json()["LatestArtists"]["Data"]
            ]
            return artists
