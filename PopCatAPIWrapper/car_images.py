from .http import HTTPClient
from io import BytesIO

__all__ = ("CarImages",)


class CarImages(HTTPClient):
    def __init__(self, res):
        self.res = res

    @property
    def image_url(self) -> str:
        """
        The image **URL** of the car"""
        return self.res["image"]

    @property
    def name(self) -> str:
        """
        The name of the car in the image
        """
        return self.res["title"]

    async def get_car_image(self) -> BytesIO:
        """
        Get the a :class:`BytesIO` object co-relating the car **IMAGE** (this is not same as the image URL)
        """
        resp = await self._request("GET", self.res["image"])
        image = BytesIO(await resp.read())
        await self._close()
        return image
