from ..http import HTTPClient
from io import BytesIO

__all__ = ("Element",)


class Element(HTTPClient):
    def __init__(self, res):
        self.res = res

    @property
    def name(self) -> str:
        """
        Returns the name of the element
        """
        return self.res["name"]

    @property
    def chemical_symbol(self) -> str:
        """
        Returns the chemical symbol of the element
        """
        return self.res["symbol"]

    @property
    def atomic_number(self) -> int:
        """
        Returns the atomic number of the element
        """
        return self.res["atomic_number"]

    @property
    def atomic_mass(self) -> int:
        """
        Returns the atomic mass of the element
        """
        return self.res["atomic_mass"]

    @property
    def period(self) -> int:
        """
        Returns the period of the element in the periodic table
        """
        return self.res["period"]

    @property
    def phase(self) -> str:
        """
        Returns the natural phase of the element
        """
        return self.res["phase"]

    @property
    def discovered_by(self) -> str:
        """
        Returns the discoverer of the element
        """
        return self.res["discovered_by"]

    async def get_image(self) -> BytesIO:
        """
        Returns a :class:`BytesIO` object co-relating the image of the element
        """
        resp = await self._request("GET", self.res["color_image"])
        image = BytesIO(await resp.read())
        await self._close
        return image

    @property
    def image_url(self) -> str:
        """
        Returns the image *URL* of the element
        """
        return self.res["image"]

    @property
    def summary(self) -> str:
        """
        Returns some more information about the element
        """
        return self.res["summary"]
