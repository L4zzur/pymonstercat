from httpx import URL
from icecream import ic  # type: ignore

from pymonstercat.api_sections.base import PyMonstercatBase
from pymonstercat.models import Release


class PyMonstercatReleases(PyMonstercatBase):
    RELEASES = PyMonstercatBase.BASE + "releases"
    RELEASE = PyMonstercatBase.BASE + "catalog/release/{id}"
    RELATED = PyMonstercatBase.BASE + "related-releases/{id}"
    COVER = "https://www.monstercat.com/release/{id}/cover"

    def browse_releases(
        self,
        limit: int = 50,
        offset: int = 0,
        search: str = "",
    ):
        url = self.RELEASES
        params = {
            "limit": limit,
            "offset": offset,
            "search": search,
        }

        response = self.get(url=url, params=params)

        if response.status_code == 200:
            releases = [
                Release.from_dict(release)
                for release in response.json()["Releases"]["Data"]
            ]
            return releases

    def get_release(
        self,
        catalog_id: str | None = None,
        uuid: str | None = None,
    ) -> Release | None:
        if catalog_id is not None:
            url = self.RELEASE.format(id=catalog_id)
            params = {"idType": "CatalogId"}
        elif uuid is not None:
            url = self.RELEASE.format(id=uuid)
            params = {"idType": "uuid"}
        else:
            return

        response = self.get(url=url, params=params)

        if response.status_code == 200:
            release = Release.from_dict(response.json()["Release"])
            return release

    def get_cover_art(
        self,
        catalog_id: str,
        width: int = 3000,
        encoding: str = "jpeg",
    ) -> URL | None:
        params = {
            "width": width,
            "encoding": encoding,
            "url": self.COVER.format(id=catalog_id),
        }

        response = self.get(url=self.CDX, params=params, follow_redirects=True)

        if response.status_code == 200:
            return response.url

    # TODO: not working yet
    def get_related_releases(
        self,
        catalog_id: str,
    ) -> list[Release] | None:
        url = self.RELATED.format(id=catalog_id)

        response = self.get(url=url)

        ic(response.json())

        if response.status_code == 200:
            releases = [
                Release.from_dict(release)
                for release in response.json()["Releases"]["Data"]
            ]
            return releases
