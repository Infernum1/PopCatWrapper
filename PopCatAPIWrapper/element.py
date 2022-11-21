from .http import HTTPClient
from io import BytesIO

__all__ = ("Element",)


class Element(HTTPClient):
    def __init__(self, res):
        self.res = res

    @property
    def name(self) -> str:
        """
        The name of the element
        """
        return self.res["name"]

    @property
    def chemical_symbol(self) -> str:
        """
        The chemical symbol of the element
        """
        return self.res["symbol"]

    @property
    def atomic_number(self) -> int:
        """
        The atomic number of the element
        """
        return self.res["atomic_number"]

    @property
    def atomic_mass(self) -> int:
        """
        The atomic mass of the element
        """
        return self.res["atomic_mass"]

    @property
    def period(self) -> int:
        """
        The period of the element in the periodic table
        """
        return self.res["period"]

    @property
    def phase(self) -> str:
        """
        The natural phase of the element
        """
        return self.res["phase"]

    @property
    def discovered_by(self) -> str:
        """
        The discoverer of the element
        """
        return self.res["discovered_by"]

    @property
    def image_url(self) -> str:
        """
        The image **URL** of the element
        """
        return self.res["image"]

    @property
    def summary(self) -> str:
        """
        Gives some more information about the element
        """
        return self.res["summary"]

    async def get_image(self) -> BytesIO:
        """
        A :class:`BytesIO` object co-relating the image of the element
        """
        resp = await self._request("GET", self.res["color_image"])
        image = BytesIO(await resp.read())
        await self._close()
        return image
