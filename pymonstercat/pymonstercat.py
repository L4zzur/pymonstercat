from pymonstercat.api_sections import PyMonstercatArtists, PyMonstercatAuth


class MonstercatAPI(
    PyMonstercatAuth,
    PyMonstercatArtists,
):
    pass
