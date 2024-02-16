from icecream import ic  # type: ignore

from pymonstercat.api_sections.base import PyMonstercatBase
from pymonstercat.models import Release


class PyMonstercatReleases(PyMonstercatBase):
    RELEASES = PyMonstercatBase.BASE + "releases"
    RELEASE = PyMonstercatBase.BASE + "catalog/release/{id}"

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
    ):
        if catalog_id is not None:
            url = self.RELEASE.format(id=catalog_id)
            params = {"idType": "CatalogId"}
        elif uuid is not None:
            url = self.RELEASE.format(id=uuid)
            params = {"idType": "uuid"}
        else:
            return
        ic(url, params)
        response = self.get(url=url, params=params)
        ic(response.status_code)
        if response.status_code == 200:
            release = Release.from_dict(response.json())
            return release
