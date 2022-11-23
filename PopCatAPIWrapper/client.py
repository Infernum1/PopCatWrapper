from .song import Song
from .element import Element
from .color import ColorInfo
from .film import Film
from .steamapp import SteamApp
from .car_images import CarImages
from .http import HTTPClient
from .showerthought import ShowerThought
from .subreddit import SubReddit
from .npm_package import NPMPackage
from io import BytesIO

from .errors import (
    FilmNotFound,
    NPMPackageNotFound,
    SongNotFound,
    ElementNotFound,
    GenericError,
    ColorNotFound,
    SteamAppNotFound,
    SubRedditNotFound,
)

default_background = "https://cdn.discordapp.com/attachments/850808002545319957/859359637106065408/bg.png"
base_url = "https://api.popcat.xyz/{}"

__all__ = ["PopCatAPI"]


class PopCatAPI(HTTPClient):
    def __init__(self):
        HTTPClient.__init__(self)

    async def get_welcome_card(
        self, first_field: str, second_field: str, third_field: str, avatar: str, background: str = default_background
    ):
        """
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
        res = await self._request(
            "GET",
            base_url.format(
                f"welcomecard?background={background}&text1={first_field}&text2={second_field}&text3={third_field}&avatar={avatar}"
            ),
        )
        image = BytesIO(await res.read())
        await self._close()
        return image

    async def get_color_info(self, color: str):
        """
        :param color: color to search for (without the #)
        :type color: :class:`str`
        :raises `ColorNotFound <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.errors.ColorNotFound>`_: If the color is not found
        :return: a `ColorInfo() <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.color.ColorInfo>`_ class instance
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
        :raises `SongNotFound <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.errors.SongNotFound>`_: If the song is not found
        :return: a `Song() <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.song.Song>`_ class instance

        """
        resp = await self._request("GET", base_url.format(f"lyrics?song={song}"))
        data = await resp.json()
        try:
            data["error"]
            await self._close()
            raise SongNotFound()
        except KeyError:
            await self._close()
            return Song(data)

    async def get_car(self):
        """
        :return: a `CarImages() <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.car_images.CarImages>`_ class instance
        """
        resp = await self._request("GET", base_url.format(f"car"))
        data = await resp.json()
        await self._close()
        return CarImages(data)

    async def get_film_info(self, film: str):
        """
        :param film: film to search for (can be a series too)
        :type film: :class:`str`
        :raises `FilmNotFound <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.errors.FilmNotFound>`_: If the film is not found
        :return: a `Film() <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.film.Film>`_ class instance

        """
        resp = await self._request("GET", base_url.format(f"imdb?q={film}"))
        data = await resp.json()
        try:
            data["error"]
            await self._close()
            raise FilmNotFound()
        except KeyError:
            await self._close()
            return Film(data)

    async def get_element_info(self, element: str):
        """
        :param element: element to get information for. You can feed the name, chemical symbol, or atomic number to get the information.
        :type element: :class:`str`
        :raises `ElementNotFound <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.errors.ElementNotFound>`_: If the element is not found
        :return: an `Element() <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.element.Element>`_ class instance
        """
        resp = await self._request("GET", base_url.format(f"periodic-table?element={element}"))
        data = await resp.json()
        try:
            data["error"]
            await self._close()
            raise ElementNotFound()
        except KeyError:
            await self._close()
            return Element(data)

    async def get_screenshot(self, url: str):
        """
        :param url: site URL to take a screenshot of
        :type url: :class:`str`
        :raises `GenericError <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.errors.GenericError>`__: If the given text is not valid
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
        :raises `GenericError <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.errors.GenericError>`__: If the given text is not valid
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
        :raises `SteamAppNotFound <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.errors.SteamAppNotFound>`_: If the steam application is not found
        :return: a `SteamApp() <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.steamapp.SteamApp>`_ class instance
        """
        resp = await self._request("GET", base_url.format(f"steam?q={app_name}"))
        data = await resp.json()
        try:
            data["error"]
            await self._close()
            raise SteamAppNotFound()
        except KeyError:
            await self._close()
            return SteamApp(data)

    async def get_shower_thought(self):
        """
        :return: a `ShowerThought() <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.showerthought.ShowerThought>`_ class instance
        """
        resp = await self._request("GET", base_url.format(f"showerthoughts"))
        data = await resp.json()
        await self._close()
        return ShowerThought(data)

    async def get_subreddit(self, subreddit: str):
        """
        :param subreddit: subreddit to get information for.
        :type subreddit: :class:`str`
        :raises `SubRedditNotFound <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.errors.SubRedditNotFound>`_: If the subreddit is not found
        :return: a `SubReddit() <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.subreddit.SubReddit>`_ class instance
        """
        resp = await self._request("GET", base_url.format(f"subreddit/{subreddit}"))
        data = await resp.json()
        try:
            data["error"]
            await self._close()
            raise SubRedditNotFound()
        except KeyError:
            await self._close()
            return SubReddit(data)

    async def get_lulcat_text(self, text: str):
        """
        :return: a :class:`str` with the 'lulcat' text
        """
        resp = await self._request("GET", base_url.format(f"lulcat/text={text}"))
        data = await resp.json()
        await self._close()
        return data["text"]

    async def get_npm_package(self, package_name: str):
        """
        :param package_name: package name to get information for.
        :type package_name: :class:`str`
        :raises `NPMPackageNotFound <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.errors.NPMPackageNotFound>`_: If the NPM package is not found
        :return: an `NPMPackage() <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.npm_package.NPMPackage>`_ class instance
        """
        resp = await self._request("GET", base_url.format(f"npm?q={package_name}"))
        data = await resp.json()
        try:
            data["error"]
            await self._close()
            raise NPMPackageNotFound(data["error"])
        except KeyError:
            await self._close()
            return NPMPackage(data)

    async def get_fact(self):
        """
        :return: a :class:`str` with a random fact
        """
        resp = await self._request("GET", base_url.format(f"fact"))
        data = await resp.json()
        await self._close()
        return data["fact"]

    async def ship_avatars(self, image1: str, image2: str):
        """
        :param image1: first image to be displayed (on the left side)
        :type image1: :class:`str`
        :param image2: second image to be displayed (on the right side)
        :type image2: :class:`str`
        :return: a :class:`BytesIO` object co-relating the 'shipped' image
        :raises `GenericError <https://popcat-api.readthedocs.io/en/latest/PopCatAPIWrapper.html#PopCatAPIWrapper.errors.GenericError>`_: If a general error is encountered
        """
        resp = await self._request("GET", base_url.format(f"ship?user1={image1}&user2={image2}"))
        try:
            await resp.json()
            await self._close()
            return GenericError(resp["error"])
        except:
            ship_image = BytesIO(await resp.read())
            await self._close()
            return ship_image

    async def get_joke(self):
        """
        :return: a :class:`str` with a random joke
        """
        resp = await self._request("GET", base_url.format(f"joke"))
        data = await resp.json()
        await self._close()
        return data["joke"]
