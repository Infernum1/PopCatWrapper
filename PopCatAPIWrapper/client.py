from .objects.lyrics import Lyrics
from .objects.element import Element
from .objects.film import Film
from .http import HTTPClient
from io import BytesIO
from .objects.color import ColorInfo
from .errors import FilmNotFound, NotValid, SongNotFound, ElementNotFound, GeneralError, ColorNotFound

default_background = "https://images.pexels.com/videos/3045163/free-video-3045163.jpg?auto=compress&cs=tinysrgb&dpr=1&w=500"
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
        :return: a :class:`ColorInfo` class instance with the following attributes and method

        Attributes
        ----------
        name: :class:`str`
            name of the color
        hex: :class:`str`
            hexadecimal representation of the color
        rgb: :class:`str`
            rgb representation of the color
        brightened: :class:`str`
            brightened version of the color

        Methods
        -------

        await get_color_image()
            get a :class:`BytesIO` object co-relating the color image
        """
        resp = await self._request("GET", base_url.format(f"color/{color}"))
        data = await resp.json()
        try:
            data['error']
            await self._close()
            raise ColorNotFound()
        except KeyError:
            await self._close()
            return ColorInfo(data)
        
    
    async def get_song_info(self, song: str):
        """
        :param song: song to search for
        :type song: :class:`str`
        :return: a :class:`Lyrics` class instance with the following attributes

        Attributes
        ----------
        title: :class:`str`
            title of the song
        thumbnail_url: :class:`str`
            thumbnail URL of the song
        artist: :class:`str`
            artist of the song
        lyrics: :class:`str`
            lyrics of the song

        """
        resp = await self._request("GET", base_url.format(f"songlyrics?song={song}"))
        data = await resp.json()
        try:
            data['error']
            await self._close()
            raise SongNotFound(song)
        except KeyError:
            await self._close()
            return Lyrics(data)
    
    async def get_film_info(self, film: str):
        """
        :param film: film to search for (can be a series too)
        :type film: :class:`str`
        :return: a :class:`Film` class instance with the following attributes

        Attributes
        ----------
        ratings: :class:`list`
            ratings of the film
        title: :class:`str`
            title of the film
        year: :class:`int`
            the year of release of the film
        rated: :class:`str`
            the PG rating of the film
        runtime: :class:`str`
            the total runtime of the film
        genres: :class:`str`
            the genres the film fits into
        director: :class:`str`
            the director of the film
        writer: :class:`str`
            the writer of the film
        actors: :class:`str`
            actors in the film
        plot: :class:`str`
            the plot of the film
        languages: :class:`str`
            languages the film is available in
        country: :class:`str`
            country the film was majorly filmed in
        awards: :class:`str`
            awards received by the film
        poster_url: :class:`str`
            **URL** for the poster of the film
        metascore: :class:`str`
            metascore of the film
        votes: :class:`str`
            votes received by the film
        imdb_id: :class:`str`
            IMDB ID of the film
        type: :class:`str`
            type of the film. e.g - movie, series. etc
        box_office: :class:`str`
            box office earnings of the film
        is_series: :class:`bool`
            :class:`False` if the film is not a series, :class:`True` if it is
        imdb_url: :class:`str`
            IMDB :class:`URL` of the film
        
        """
        resp = await self._request("GET", base_url.format(f"imdb?q={film}"))
        data = await resp.json()
        try:
            data['error']
            await self._close()
            raise FilmNotFound(film)
        except KeyError:
            await self._close()
            return Film(data)

    async def get_element_info(self, element: str):
        """
        :param element: element to get information for. You can feed the name, chemical symbol, or atomic number to get the information.
        :type element: :class:`str`
        :return: an :class:`Element` class instance with the following attributes

        Attributes
        ----------
        name: :class:`str`
            name of the element
        symbol: :class:`str`
            symbol of the element
        atomic_number: :class:`int`
            atomic number of the element
        atomic_mass: :class:`int`
            atomic mass of the element
        period: :class:`int`
            period of the element in the periodic table
        discovered_by: :class:`str`
            discoverer of the element
        image_url: :class:`str`
            get the image **URL** of the element
        phase: :class:`str`
            natural phase of the element
        summary: :class:`str`
            a little more information about the element
        """
        resp = await self._request("GET", base_url.format(f"periodic-table?element={element}"))
        data = await resp.json()
        try:
            data['error']
            await self._close()
            raise ElementNotFound(element)
        except KeyError:
            await self._close()
            return Element(data)

    # async def get_screenshot(self, url: str):
    #     """
    #     :param url: site URL to take a screenshot of
    #     :type url: :class:`str`
    #     :return: a :class:`BytesIO` object co-relating the screenshot of the site
    #     """
    #     resp = await self._request("GET", base_url.format(f"screenshot?url={url}"))
    #     try:
    #         await resp.json()
    #     except:
    #         image = BytesIO(await resp.read())
    #     
    #         return image