import os
from pathlib import Path


def main():
    from pymonstercat import MonstercatAPI

    EMAIL = os.environ.get("EMAIL")
    PASSWORD = os.environ.get("PASSWORD")

    path = Path("test.env")
    print(path.absolute())
    api = MonstercatAPI(config_path=path)
    api.sign_in_email(EMAIL, PASSWORD)
    # artists = api.get_artists(limit=2, offset=0, search="")
    # for artist in artists:
    #     print(artist.active_years)
    artist = api.get_artist(artist_uri="fool")
    print(artist)


if __name__ == "__main__":
    main()
