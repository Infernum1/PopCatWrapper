from ..http import HTTPClient
from io import BytesIO

__all__ = ("ColorInfo",)


class ColorInfo(HTTPClient):
    def __init__(self, res):
        self.res = res

    @property
    def hex(self) -> str:
        return self.res["hex"]

    @property
    def name(self) -> str:
        return self.res["name"]

    @property
    def rgb(self) -> str:
        return self.res["rgb"]

    async def get_color_image(self) -> BytesIO:
        if not resp["name"].startswith("Invalid"):
            resp = await self._request("GET", self.res["color_image"])
            image = BytesIO(await resp.read())
            await self._close()
            return image
        else:
            return "Invalid color, no image found"

    @property
    def brightened(self) -> str:
        return self.res["brightened"]
