from ..http import HTTPClient
from io import BytesIO

__all__ = ("SteamApp",)


class SteamApp(HTTPClient):
    def __init__(self, res):
        self.res = res

    @property
    def type(self) -> str:
        """
        The type of the application
        """
        return self.res["type"]

    @property
    def name(self) -> str:
        """
        The name of the application
        """
        return self.res["name"]

    @property
    def publishers(self) -> list:
        """
        The publishers of the application
        """
        return self.res["publishers"]

    @property
    def developers(self) -> list:
        """
        The developers of the application
        """
        return self.res["developers"]

    @property
    def price(self) -> int:
        """
        The price of the application
        """
        return self.res["price"]

    @property
    def description(self) -> str:
        """
        The description of the application
        """
        return self.res["description"]

    @property
    def thumbnail_url(self) -> str:
        """
        The **THUMBNAIL URL** of the application
        """
        return self.res["thumbnail"]

    @property
    def banner_url(self) -> str:
        """
        The **BANNER URL** of the application
        """
        return self.res["banner"]


    async def get_thumbnail(self) -> BytesIO:
        """
        A :class:`BytesIO` object co-relating the **THUMBNAIL** of the application
        """
        resp = await self._request("GET", self.res["thumbnail"])
        image = BytesIO(await resp.read())
        await self._close()
        return image

    async def get_banner(self) -> BytesIO:
        """
        A :class:`BytesIO` object co-relating the **BANNER** of the application
        """
        resp = await self._request("GET", self.res["banner"])
        image = BytesIO(await resp.read())
        await self._close()
        return image