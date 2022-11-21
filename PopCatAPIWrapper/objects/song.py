from io import BytesIO 

__all__ = ("Song",)


class Song:
    def __init__(self, res):
        self.res = res

    @property
    def title(self) -> str:
        """
        Title of the song
        """
        return self.res["title"]

    @property
    def thumbnail(self) -> str:
        """
        Thumbnail **URL** of the song
        """
        return self.res["image"]

    @property
    def artist(self) -> str:
        """
        Artist of the song
        """
        return self.res["artist"]

    @property
    def lyrics(self) -> str:
        """
        Lyrics of the song
        """
        return self.res["lyrics"]

    async def get_thumbnail(self):
        """
        A :class:`BytesIO` object co-relating the **THUMBNAIL** of the song
        """
        resp = await self._request("GET", self.res["image"])
        image = BytesIO(await resp.read())
        await self._close()
        return image