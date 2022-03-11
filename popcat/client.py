from .lyrics import Lyrics
from .movie import Movie
from .http import HTTPClient
from io import BytesIO
from .color import ColorInfo
from .errors import MovieNotFound, NotValid, SongNotFound

default_background = "https://images.pexels.com/videos/3045163/free-video-3045163.jpg?auto=compress&cs=tinysrgb&dpr=1&w=500"
base_url = "https://api.popcat.xyz/{}"

__all__ = ("PopCatAPI")

class PopCatAPI(HTTPClient):

    def __init__(self):
        HTTPClient.__init__(self)
    
    async def get_welcome_card(self, first_field: str, second_field: str, third_field: str, avatar: str, background:str = default_background):
        """"
        :param first_field: first field to display, largest text size
        :type first_field: :class:`str`
        :param second_field: second field to display, smaller text size than first field
        :type second_field: :class:`str`
        :param third_field: third field to display, smaller text size than second field
        :type third_field: :class:`str`
        :param avatar: avatar url to display
        :type avatar: :class:`str`
        :param background: background url, defaults to a black background
        :type background: :class:`str`
        """
        res = await self._request("GET", base_url.format(f"welcomecard?background={background}&text1={first_field}&text2={second_field}&text3={third_field}&avatar={avatar}"))
        image = BytesIO(await res.read())
        await self._close
        return image
    
    async def get_color_info(self, color: str):
        """
        :param color: color to search for (without the #)
        :type color: :class:`str`
        :return: an image URL of the color

        Attributes
        ----------
        name: :class:`str`
            name of the color
        hex: :class:`str`
            hexadecimal representation of the color
        rgb: :class:`str`
            rgb representation of the color

        Methods
        -------

        await get_color_image: :class:`str`
            get a BytesIO object co-relating the color image
        """
        resp = await self._request("GET", base_url.format(f"colorinfo?color={color}"))
        data = await resp.json()
        try:
            data['error']
            raise NotValid()
        except KeyError:
            return ColorInfo(data)
    
    async def get_song_lyrics(self, song: str):
        """
        :param song: song to search for
        :type song: :class:`str`
        :return: a list of lyrics of the song
        """
        resp = await self._request("GET", base_url.format(f"songlyrics?song={song}"))
        data = await resp.json()
        try:
            data['error']
            raise SongNotFound(song)
        except KeyError:
            return Lyrics(data)
    
    async def get_movie_info(self, movie: str):
        """
        :param movie: movie to search for
        :type movie: :class:`str`
        :return: a list of movie info
        """
        resp = await self._request("GET", base_url.format(f"movieinfo?movie={movie}"))
        data = await resp.json()
        try:
            data['error']
            raise MovieNotFound(movie)
        except KeyError:
            return Movie(data)

    async def get_screenshot(self, url: str):
        """
        :param url: site URL to take a screenshot of
        :type url: :class:`str`
        :return: a :class:`BytesIO` object co-relating the screenshot of the site
        """
        resp = await self._request("GET", base_url.format(f"screenshot?url={url}"))
        try:
            await resp.json()
        except:
            image = BytesIO(await resp.read())
            await self._close
            return image