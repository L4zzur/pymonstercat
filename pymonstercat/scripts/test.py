from io import BytesIO
from pathlib import Path

from icecream import ic
from PIL import Image


def main():
    from pymonstercat import MonstercatAPI

    path = Path("config_test.yaml")
    ic(path.absolute())
    api = MonstercatAPI(config_path=path)
    api.sign_in_email()
    # artists = api.get_artists(limit=2, offset=0, search="")
    # for artist in artists:
    #     print(artist.active_years)
    # artist = api.get_artist(artist_uri="curbi")
    # print(artist)
    # photo = api.get_artist_photo(artist_uri="hayve")
    # if photo is None:
    #     print("No photo")
    #     return
    # i = Image.open(BytesIO(photo))
    # i.show()

    ic(api.browse_releases(limit=2))
    ic(api.get_release(catalog_id="742779551344"))


if __name__ == "__main__":
    main()
