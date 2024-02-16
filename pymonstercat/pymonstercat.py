from pymonstercat.api_sections import (
    PyMonstercatArtists,
    PyMonstercatAuth,
    PyMonstercatReleases,
)


class MonstercatAPI(
    PyMonstercatAuth,
    PyMonstercatArtists,
    PyMonstercatReleases,
):
    pass
