from __future__ import annotations

import json
from dataclasses import dataclass, field
from enum import IntEnum

from dataclass_wizard import JSONSerializable


class Brand(IntEnum):
    """Label's brand enum

    Attributes:
        uncaged (`int`): Uncaged Brand
        instinct (`int`): Instinct Brand
        silk (`int`): Silk Brand
        call_of_the_wild (`int`): Call of The Wild Podcast
        silk_showcase (`int`): Silk Showcase Podcast
    """

    uncaged = 1
    instinct = 2
    silk = 4
    call_of_the_wild = 3
    silk_showcase = 5


@dataclass
class ArtistDetails(JSONSerializable):
    """Class represents ArtistDetails object

    Attributes:
        about (`str`, optional): Artist's bio.
        bookings (`str`, optional): Artist's bio.
        management (`str`, optional): Artist's bio.
    """

    about: str | None = None
    bookings: str | None = None
    management: str | None = None

    class Meta(JSONSerializable.Meta):
        json_key_to_field = {
            "About": "about",
            "Bookings": "bookings",
            "ManagementDetails": "management",
        }

    def __str__(self):
        return (
            f"ArtistDetails:\n"
            f"about = {self.about}\n"
            f"bookings = {self.bookings}\n"
            f"management = {self.management}"
        )


@dataclass
class Link(JSONSerializable):
    """Class represents Link object

    Attributes:
        platform (`str`): The platform this link leads to.
        url (`str`): The url this link leads to.
    """

    platform: str
    url: str

    class Meta(JSONSerializable.Meta):
        json_key_to_field = {
            "Platform": "platform",
            "Url": "url",
        }

    def __str__(self):
        return f"Link:\nplatform = {self.platform}\nurl = {self.url}"


@dataclass
class Artist(JSONSerializable):
    """Class represents Artist object

    Attributes:
        details (`ArtistDetails`): Artist's bio, bookings and mgmt details.
        name (`str`): Artist's name.
        is_public (`bool`): Whether the artist's profile page is public.
        do_show_event (`bool`): Whether events should be shown.
        uri (`str`): Public url slug to the artist's profile page.
        active_years (`list[int]`): Years when the artist has released on Monstercat.
        featured_release_cover_file_uuid (`str`): File ID for the cover of the featured release.
        featured_release_uuid (`str`): ID of artist's featured release.
        featured_video_url (`str`): URL to artist's featured video.
        uuid (`str`): URL to artist's featured video.
        landscape_file_uuid (`str`): File ID for landscape.
        links (list[Link]): List of Links to the artist's socials.
        logo_file_uuid (`str`): File ID for logo.
        portrait_file_uuid (`str`): File ID for portrait.
        profile_file_uuid (`str`): profile_file_uuid.
        square_file_uuid (`str`): File ID for square.
        tags (`list[`str`]`): The list of tags for the artist.
        about (`str`, optional): Artist's bio.
        landscape_file_uuid (`str`, optional): File ID for landscape.
        portrait_file_uuid (`str`, optional): File ID for portrait.
        square_file_uuid (`str`, optional): File ID for square.
        logo_file_uuid (`str`, optional): File ID for logo.
        featured_release_cover_file_uuid (`str`, optional): File ID for the cover of the featured release.
        featured_release_uuid (`str`, optional): ID of artist's featured release.
        featured_video_url (`str`, optional): URL to artist's featured video.
    """

    details: ArtistDetails
    uuid: str
    name: str
    profile_file_uuid: str
    is_public: bool
    do_show_event: bool
    uri: str
    active_years: list[int] | None = field(default_factory=list)
    tags: list[str] | None = field(default_factory=list)
    links: list[Link] | None = field(default_factory=list)
    about: str | None = None
    logo_file_uuid: str | None = None
    square_file_uuid: str | None = None
    portrait_file_uuid: str | None = None
    landscape_file_uuid: str | None = None
    featured_release_cover_file_uuid: str | None = None
    featured_release_uuid: str | None = None
    featured_video_url: str | None = None

    def __post_init__(self):
        self.active_years = sorted(self.active_years)

    class Meta(JSONSerializable.Meta):
        json_key_to_field = {
            "About": "about",
            "ActiveYears": "active_years",
            "Details": "details",
            "Id": "uuid",
            "Name": "name",
            "ProfileFileId": "profile_file_uuid",
            "LogoFileId": "logo_file_uuid",
            "SquareFileId": "square_file_uuid",
            "PortraitFileId": "portrait_file_uuid",
            "LandscapeFileId": "landscape_file_uuid",
            "Public": "is_public",
            "ShowEvent": "do_show_event",
            "Tags": "tags",
            "URI": "uri",
            "FeaturedReleaseCoverFileId": "featured_release_cover_file_uuid",
            "FeaturedReleaseId": "featured_release_uuid",
            "FeaturedVideoURL": "featured_video_url",
            "Links": "links",
        }

    def __str__(self):
        return (
            f"Artist:\n"
            f"active_years = {self.active_years}\n"
            f"uuid = {self.uuid}\n"
            f"name = {self.name}\n"
            f"uri = {self.uri}\n"
        )
