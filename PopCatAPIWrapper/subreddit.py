from .http import HTTPClient
from io import BytesIO

__all__ = ("SubReddit",)


class SubReddit(HTTPClient):
    def __init__(self, res):
        self.res = res

    @property
    def name(self) -> str:
        """
        The name of the subreddit
        """
        return self.res["name"]

    @property
    def title(self) -> str:
        """
        The title of the subreddit
        """
        return self.res["title"]

    @property
    def active_users(self) -> int:
        """
        Number of active users in the subreddit
        """
        return self.res["active_users"]

    @property
    def members(self) -> int:
        """
        Number of members of the subreddit
        """
        return self.res["members"]

    @property
    def description(self) -> int:
        """
        The description of the subreddit
        """
        return self.res["description"]

    @property
    def icon_url(self) -> str:
        """
        The **URL** of the ICON of the subreddit
        """
        return self.res["icon"]

    @property
    def banner_url(self) -> str:
        """
        The **URL** of the BANNER of the subreddit
        """
        return self.res["banner"]

    @property
    def allows_images(self) -> str:
        """
        If sending images is allowed
        """
        return self.res["allow_images"]

    @property
    def allows_videos(self) -> bool:
        """
        If sending videos is allowed
        """
        return self.res["allow_videos"]

    @property
    def is_over_18(self) -> bool:
        """
        If the subreddit is over 18+
        """
        return self.res["over_18"]

    async def get_icon(self) -> BytesIO:
        """
        A :class:`BytesIO` object co-relating the icon of the subreddit
        """
        resp = await self._request("GET", self.res["icon"])
        image = BytesIO(await resp.read())
        await self._close()
        return image

    async def get_banner(self) -> BytesIO:
        """
        A :class:`BytesIO` object co-relating the banner of the subreddit
        """
        resp = await self._request("GET", self.res["banner "])
        image = BytesIO(await resp.read())
        await self._close()
        return image
