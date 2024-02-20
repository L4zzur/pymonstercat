from dataclasses import dataclass

from dataclass_wizard import JSONSerializable

from .brand import Brand
from .link import Link


@dataclass
class ReleaseArtist(JSONSerializable):
    """Class represents Release Artist object

    Attributes:
        artist_uuid (str): Artist's unique id.
        position (int): Artist's order in release credit.
        name (str): Artist's name.
        profile_file_uuid (str): ID of the profile image asset:
        platform (str): Artist platform.
        is_public (bool): Whether the artist's profile page is public.
        release_uuid (str): ID of the release this artist is linked to.
        role (str): Artist's role in the release.
        uri (str): Public url slug to the artist's profile page.
    """

    artist_uuid: str
    position: int
    name: str
    profile_file_uuid: str
    platform: str
    is_public: bool
    release_uuid: str
    role: str
    uri: str

    class Meta(JSONSerializable.Meta):
        json_key_to_field = {
            "ArtistId": "artist_uuid",
            "ArtistNumber": "position",
            "Name": "name",
            "ProfileFileId": "profile_file_uuid",
            "Platform": "platform",
            "Public": "is_public",
            "ReleaseId": "release_uuid",
            "Role": "role",
            "URI": "uri",
        }

    def __str__(self):
        return f"Release Artist:\n" f"Name: {self.name}\n" f"uri = {self.uri}\n"


@dataclass
class Release(JSONSerializable):
    """Class represents Release object

    Attributes:
        artists_string (str):
        catalog_id (str): The catalog ID of the release. \
            After Dec 1, 2022 the UPC is used.
        description (str): Description of the release.
        uuid (str): The unique ID of the release.
        release_date (str): ISO8601 timestamp. The release date.
        release_date_timezone (str): Timezone identifier for the release date.
        title (str): The title of the release.
        type (str): The type of the release (Single, EP, Album, etc).
        version (str): The version of the release (shown in parentheses).
        notes (str): Liner Notes for the release.
        artists (list[ReleaseArtist]): List of Artists for the release.
        brand (Brand): The ID of the brand the release belongs to.
        brand_string (str): Human readable name of the brand the release belongs to.
        copyright_p_line (str): Notice of sound recording copyright (℗).
        is_downloadable (bool): Whether the release can be downloaded with Gold.
        featured_artists_string (str): Human readable featured artists (unused?).
        global_release_id (str): The Global Release Identifier of the release.
        genre (str): Primary genre of the release.
        subgenre (str): The subgenre of the release.
        is_early_access (bool): Whether the release is currently in Gold Early Access.
        links (list[Link]): list of Links on this release.
        prerelease_date (str): The pre-release date.
        presave_date (str): The date when the release went up for presave.
        spotify_uuid (str): The spotify id for the release (see Links instead).
        is_streamable (bool): Whether the release can be streamed on the site/player.
        tags (list[str]): The list of tags of the release.
        universal_product_code (str): The Universal Product Code code of the release.
        youtube_url (str): The youtube video for the release (see Links instead).
    """

    artists_string: str
    catalog_id: str
    description: str
    uuid: str
    release_date: str
    release_date_timezone: str
    title: str
    type: str | None = None
    version: str | None = None
    notes: str | None = None
    artists: list[ReleaseArtist] | None = None
    brand: Brand | None = None
    brand_string: str | None = None
    copyright_p_line: str | None = None
    is_downloadable: bool | None = None
    featured_artists_string: str | None = None
    global_release_id: str | None = None
    genre: str | None = None
    subgenre: str | None = None
    is_early_access: bool | None = None
    links: list[Link] | None = None
    prerelease_date: str | None = None
    presave_date: str | None = None
    spotify_uuid: str | None = None
    is_streamable: bool | None = None
    tags: list[str] | None = None
    universal_product_code: str | None = None
    youtube_url: str | None = None

    class Meta(JSONSerializable.Meta):
        json_key_to_field = {
            "ArtistsTitle": "artists_string",
            "CatalogId": "catalog_id",
            "Description": "description",
            "Id": "uuid",
            "ReleaseDate": "release_date",
            "ReleaseDateTimezone": "release_date_timezone",
            "Title": "title",
            "Type": "type",
            "Version": "version",
            "AlbumNotes": "notes",
            "Artists": "artists",
            "BrandId": "brand",
            "BrandTitle": "brand_string",
            "CopyrightPLine": "copyright_p_line",
            "Downloadable": "is_downloadable",
            "FeaturedArtistsTitle": "featured_artists_string",
            "GRid": "global_release_id",
            "GenrePrimary": "genre",
            "GenreSecondary": "subgenre",
            "InEarlyAccess": "is_early_access",
            "Links": "links",
            "PrereleaseDate": "prerelease_date",
            "PresaveDate": "presave_date",
            "SpotifyId": "spotify_uuid",
            "Streamable": "is_streamable",
            "Tags": "tags",
            "UPC": "universal_product_code",
            "YoutubeUrl": "youtube_url",
        }

    def __str__(self) -> str:
        return (
            f"Release:\n"
            f"catalog_id = {self.catalog_id}\n"
            f"uuid = {self.uuid}\n"
            f"release_date = {self.release_date}\n"
            f"release_date_timezone = {self.release_date_timezone}\n"
            f"title = {self.title}\n"
            f"type = {self.type}\n"
            f"version = {self.version}\n"
        )
