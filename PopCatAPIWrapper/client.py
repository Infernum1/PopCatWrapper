from .objects.song import Song
from .objects.element import Element
from .objects.color import ColorInfo
from .objects.film import Film
from .objects.steamapp import SteamApp
from .objects.car_images import CarImages
from .http import HTTPClient

from io import BytesIO

from .errors import FilmNotFound, SongNotFound, ElementNotFound, GenericError, ColorNotFound, SteamAppNotFound

default_background = (
    "https://images.pexels.com/videos/3045163/free-video-3045163.jpg?auto=compress&cs=tinysrgb&dpr=1&w=500"
)
base_url = "https://api.popcat.xyz/{}"

__all__ = ["PopCatAPI"]


class PopCatAPI(HTTPClient):
    def __init__(self):
        HTTPClient.__init__(self)

    # async def get_welcome_card(self, first_field: str, second_field: str, third_field: str, avatar: str, background:str = default_background):
    #     """"
    #     :param first_field: first field to display, largest text size
    #     :type first_field: :class:`str`
    #     :param second_field: second field to display, smaller text size than first field
    #     :type second_field: :class:`str`
    #     :param third_field: third field to display, smaller text size than second field
    #     :type third_field: :class:`str`
    #     :param avatar: avatar url to display
    #     :type avatar: :class:`str`
    #     :param background: background url, defaults to a black background
    #     :type background: :class:`str`
    #     """
    #     res = await self._request("GET", base_url.format(f"welcomecard?background={background}&text1={first_field}&text2={second_field}&text3={third_field}&avatar={avatar}"))
    #     image = BytesIO(await res.read())
    #
    #     return image

    async def get_color_info(self, color: str):
        """
        :param color: color to search for (without the #)
        :type color: :class:`str`
        :raise PopCatAPIWrapper.errors.ColorNotFound: If the color is not found
        :return: a `ColorInfo() <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.objects.color.ColorInfo>`_ class instance
        """
        resp = await self._request("GET", base_url.format(f"color/{color}"))
        data = await resp.json()
        try:
            data["error"]
            await self._close()
            raise ColorNotFound()
        except KeyError:
            await self._close()
            return ColorInfo(data)

    async def get_song_info(self, song: str):
        """
        :param song: song to search for
        :type song: :class:`str`
        :raise PopCatAPIWrapper.errors.SongNotFound: If the song is not found
        :return: a `Song() <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.objects.song.Song>`_ class instance

        """
        resp = await self._request("GET", base_url.format(f"lyrics?song={song}"))
        data = await resp.json()
        try:
            data["error"]
            await self._close()
            raise SongNotFound(song)
        except KeyError:
            await self._close()
            return Song(data)

    async def get_car(self):
        """
        :return: a `CarImages() <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.objects.car_images.CarImages>`_ class instance
        """
        resp = await self._request("GET", base_url.format(f"car"))
        data = await resp.json()
        await self._close()
        return CarImages(data)

    async def get_film_info(self, film: str):
        """
        :param film: film to search for (can be a series too)
        :type film: :class:`str`
        :raise PopCatAPIWrapper.errors.FilmNotFound: If the film is not found
        :return: a `Film() <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.objects.film.Film>`_ class instance

        """
        resp = await self._request("GET", base_url.format(f"imdb?q={film}"))
        data = await resp.json()
        try:
            data["error"]
            await self._close()
            raise FilmNotFound(film)
        except KeyError:
            await self._close()
            return Film(data)

    async def get_element_info(self, element: str):
        """
        :param element: element to get information for. You can feed the name, chemical symbol, or atomic number to get the information.
        :type element: :class:`str`
        :raise PopCatAPIWrapper.errors.ElementNotFound: If the element is not found
        :return: an `Element() <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.objects.element.Element>`_ class instance
        """
        resp = await self._request("GET", base_url.format(f"periodic-table?element={element}"))
        data = await resp.json()
        try:
            data["error"]
            await self._close()
            raise ElementNotFound(element)
        except KeyError:
            await self._close()
            return Element(data)

    async def get_screenshot(self, url: str):
        """
        :param url: site URL to take a screenshot of
        :type url: :class:`str`
        :raise PopCatAPIWrapper.errors.GenericError: If the given URL is not valid
        :return: a :class:`BytesIO` object co-relating the screenshot of the site
        """
        resp = await self._request("GET", base_url.format(f"screenshot?url={url}"))
        try:
            await resp.json()
            await self._close()
            return GenericError(
                "Not a valid URL, make sure the URL is valid and/or starts with 'https://' or 'http://'"
            )
        except:
            screenshot = BytesIO(await resp.read())
            await self._close()
            return screenshot

    async def get_sadcat_meme(self, text: str):
        """
        :param text: text to show in the meme
        :type text: :class:`str`
        :raise PopCatAPIWrapper.errors.GenericError: If the given text is not valid
        :return: a :class:`BytesIO` object co-relating the meme image
        """
        resp = await self._request("GET", base_url.format(f"sadcat?text={text}"))
        try:
            await resp.json()
            await self._close()
            return GenericError("Invalid text, make sure the text isn't too long")
        except:
            meme_image = BytesIO(await resp.read())
            await self._close()
            return meme_image

    async def get_pickup_line(self):
        """
        :return: a :class:`str` with the pick-up line
        """
        resp = await self._request("GET", base_url.format(f"pickuplines"))
        data = await resp.json()
        await self._close()
        return data["pickupline"]

    async def get_steam_application(self, app_name: str):
        """
        :param app: steam application to search for
        :type app: :class:`str`
        :raise PopCatAPIWrapper.errors.SteamAppNotFound: If the steam application is not found
        :return: a `SteamApp() <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.objects.steamapp.SteamApp>`_ class instance
        """
        resp = await self._request("GET", base_url.format(f"steam?q={app_name}"))
        data = await resp.json()
        try:
            data["error"]
            await self._close()
            raise SteamAppNotFound(app_name)
        except KeyError:
            await self._close()
            return SteamApp(data)
