from io import BytesIO

__all__ = ("Film",)

class Film:
    def __init__(self, res):
        self.res = res

    @property
    def ratings(self):
        """
        A list of dictionaries with the source and the ratings of the movie
        """
        return self.res["ratings"]

    @property
    def title(self) -> str:
        """
        The title of the movie
        """
        return self.res["title"]

    @property
    def year(self) -> int:
        """
        The release year of the movie
        """
        return self.res["year"]

    @property
    def rated(self) -> str:
        """
        The PG rating of the movie
        """
        return self.res["rated"]

    @property
    def runtime(self) -> str:
        """
        The runtime of the movie
        """
        return self.res["runtime"]

    @property
    def genres(self) -> str:
        """
        The genres of the movie
        """
        return self.res["genres"]

    @property
    def director(self) -> str:
        """
        The director of the movie
        """
        return self.res["director"]

    @property
    def writer(self) -> str:
        """
        The writer of the movie
        """
        return self.res["writer"]

    @property
    def actors(self) -> str:
        """
        The actors of the movie
        """
        return self.res["actors"]

    @property
    def plot(self) -> str:
        """
        The brief plot of the movie
        """
        return self.res["plot"]

    @property
    def languages(self) -> str:
        """
        The languages of the movie
        """
        return self.res["languages"]

    @property
    def country(self) -> str:
        """
        The country the movie was shot in
        """
        return self.res["country"]

    @property
    def awards(self) -> str:
        """
        The awards given to the movie
        """
        return self.res["awards"]

    @property
    def poster(self) -> str:
        """
        The URL of the poster of the movie
        """
        return self.res["poster"]

    @property
    def metascore(self) -> str:
        """
        The metascore of the movie
        """
        return self.res["metascore"]

    @property
    def votes(self) -> str:
        """
        The number of votes received by the movie
        """
        return self.res["votes"]

    @property
    def imdb_id(self) -> str:
        """
        The IMDB ID of the movie
        """
        return self.res["imdbid"]

    @property
    def type(self) -> str:
        """
        The type of the movie
        """
        return self.res["type"]

    @property
    def box_office(self) -> str:
        """
        The box office earnings of the movie
        """
        return self.res["boxoffice"]

    @property
    def is_series(self) -> bool:
        """
        Whether the movie is a series
        """
        return self.res["series"]

    @property
    def imdb_url(self) -> str:
        """
        The URL of the movie on IMDB
        """
        return self.res["imdburl"]

    async def get_poster(self):
        """
        A :class:`BytesIO` object co-relating the **POSTER** of the film
        """
        resp = await self._request("GET", self.res["poster"])
        image = BytesIO(await resp.read())
        await self._close()
        return image