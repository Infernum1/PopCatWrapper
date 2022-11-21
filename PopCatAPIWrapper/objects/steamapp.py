from ..http import HTTPClient
from io import BytesIO

__all__ = ("SteamApp",)


class SteamApp(HTTPClient):
    def __init__(self, res):
        self.res = res

    @property
    def type(self) -> str:
        """
        Returns the type of the application
        """
        return self.res["type"]

    @property
    def name(self) -> str:
        """
        Returns the name of the application
        """
        return self.res["name"]

    @property
    def publishers(self) -> list:
        """
        Returns the publishers of the application
        """
        return self.res["publishers"]

    @property
    def developers(self) -> list:
        """
        Returns the developers of the application
        """
        return self.res["developers"]

    @property
    def price(self) -> int:
        """
        Returns the price of the application
        """
        return self.res["price"]

    @property
    def description(self) -> str:
        """
        Returns the description of the application
        """
        return self.res["description"]

    async def get_thumbnail(self) -> BytesIO:
        """
        Returns a :class:`BytesIO` object co-relating the **THUMBNAIL** of the application
        """
        resp = await self._request("GET", self.res["thumbnail"])
        image = BytesIO(await resp.read())
        await self._close()
        return image

    @property
    def thumbnail_url(self) -> str:
        """
        Returns the **THUMBNAIL URL** of the application
        """
        return self.res["thumbnail"]

    async def get_banner(self) -> BytesIO:
        """
        Returns a :class:`BytesIO` object co-relating the **BANNER** of the application
        """
        resp = await self._request("GET", self.res["banner"])
        image = BytesIO(await resp.read())
        await self._close()
        return image

    @property
    def banner_url(self) -> str:
        """
        Returns the **BANNER URL** of the application
        """
        return self.res["banner"]
