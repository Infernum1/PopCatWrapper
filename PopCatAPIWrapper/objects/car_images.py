from ..http import HTTPClient
from io import BytesIO

__all__ = ("CarImages",)


class CarImages(HTTPClient):
    def __init__(self, res):
        self.res = res

    @property
    def image_url(self) -> str:
        return self.res["image"]

    @property
    def name(self) -> str:
        return self.res["title"]

    async def get_car_image(self) -> BytesIO:
        resp = await self._request("GET", self.res["image"])
        image = BytesIO(await resp.read())
        await self._close()
        return image
