from ..http import HTTPClient
from io import BytesIO

__all__ = ("ColorInfo",)


class ColorInfo(HTTPClient):
    def __init__(self, res):
        self.res = res

    @property
    def hex(self) -> str:
        """
        Hex of the color
        """
        return self.res["hex"]

    @property
    def name(self) -> str:
        """
        Name of the color
        """
        return self.res["name"]

    @property
    def rgb(self) -> str:
        """
        RGB of the color
        """
        return self.res["rgb"]

    @property
    def brightened(self) -> str:
        """
        Brightened version of the color
        """
        return self.res["brightened"]


    async def get_color_image(self) -> BytesIO:
        """
        **Method:** Get a :class:`BytesIO` object co-relating the color **IMAGE**
        """
        if not resp["name"].startswith("Invalid"):
            resp = await self._request("GET", self.res["color_image"])
            image = BytesIO(await resp.read())
            await self._close()
            return image
        else:
            return "Invalid color, no image found"