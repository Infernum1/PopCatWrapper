from io import BytesIO
from .http import HTTPClient

__all__ = ("Meme",)


class Meme(HTTPClient):
    def __init__(self, res):
        self.res = res

    @property
    def title(self) -> str:
        """
        Title of the 'meme' reddit post
        """
        return self.res["title"]

    @property
    def post_url(self) -> str:
        """
        URL of the 'meme' reddit post
        """
        return self.res["url"]

    @property
    def image_url(self) -> str:
        """
        Image URL of the actual meme
        """
        return self.res["image"]

    @property
    def upvotes(self) -> str:
        """
        Up-votes received by the 'meme' post
        """
        return self.res["upvotes"]

    @property
    def comments(self) -> str:
        """
        Comments received by the 'meme' post
        """
        return self.res["comments"]

    async def get_meme_image(self):
        """
        A :class:`BytesIO` object co-relating the actual meme
        """
        resp = await self._request("GET", self.res["image"])
        image = BytesIO(await resp.read())
        await self._close()
        return image
