from io import BytesIO
from pathlib import Path

from PIL import Image


def main():
    from pymonstercat import MonstercatAPI

    path = Path("config_test.yaml")
    print(path.absolute())
    api = MonstercatAPI(config_path=path)
    api.sign_in_email()
    # artists = api.get_artists(limit=2, offset=0, search="")
    # for artist in artists:
    #     print(artist.active_years)
    # artist = api.get_artist(artist_uri="curbi")
    # print(artist)
    photo = api.get_artist_photo(artist_uri="curbi")
    if photo is None:
        print("No photo")
        return
    i = Image.open(BytesIO(photo))
    i.show()


if __name__ == "__main__":
    main()
