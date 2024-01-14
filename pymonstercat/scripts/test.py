import os
from pathlib import Path


def main():
    from pymonstercat import MonstercatAPI

    path = Path("config_test.yaml")
    print(path.absolute())
    api = MonstercatAPI(config_path=path)
    # artists = api.get_artists(limit=2, offset=0, search="")
    # for artist in artists:
    #     print(artist.active_years)
    artist = api.get_artist(artist_uri="fool")
    print(artist)


if __name__ == "__main__":
    main()
