__all__ = ('Film',)

class Film:
    def __init__(self, res):
        self.res = res

    @property
    def ratings(self):
        """
        Returns a list of dictionaries with the source and the ratings of the movie
        """
        return self.res['ratings']
    
    @property
    def title(self) -> str:
        """
        Returns the title of the movie
        """
        return self.res['title']
    
    @property
    def year(self) -> int:
        """
        Returns the release year of the movie
        """
        return self.res['year']
    
    @property
    def rated(self) -> str:
        """
        Returns the PG rating of the movie
        """
        return self.res['rated']
    
    @property
    def runtime(self) -> str:
        """
        Returns the runtime of the movie
        """
        return self.res['runtime']
    
    @property
    def genres(self) -> str:
        """
        Returns the genres of the movie
        """
        return self.res['genres']
    
    @property
    def director(self) -> str:
        """
        Returns the director of the movie
        """
        return self.res['director']
    
    @property
    def writer(self) -> str:
        """
        Returns the writer of the movie
        """
        return self.res['writer']
    
    @property
    def actors(self) -> str:
        """
        Returns the actors of the movie
        """
        return self.res['actors']

    @property
    def plot(self) -> str:
        """
        Returns the brief plot of the movie
        """
        return self.res['plot']
    
    @property
    def languages(self) -> str:
        """
        Returns the languages of the movie
        """
        return self.res['languages']
    
    @property
    def country(self) -> str:
        """
        Returns the country the movie was shot in
        """
        return self.res['country']
    
    @property
    def awards(self) -> str:
        """
        Returns the awards given to the movie
        """
        return self.res['awards']
    
    @property
    def poster(self) -> str:
        """
        Returns the URL of the poster of the movie
        """
        return self.res['poster']
    
    @property
    def metascore(self) -> str:
        """
        Returns the metascore of the movie
        """
        return self.res['metascore']
    
    @property
    def votes(self) -> str:
        """
        Returns the number of votes received by the movie
        """
        return self.res['votes']
    
    @property
    def imdb_id(self) -> str:
        """
        Returns the IMDB ID of the movie
        """
        return self.res['imdbid']
    
    @property
    def type(self) -> str:
        """
        Returns the type of the movie
        """
        return self.res['type']
    
    @property
    def box_office(self) -> str:
        """
        Returns the box office earnings of the movie
        """
        return self.res['boxoffice']
    
    @property
    def is_series(self) -> bool:
        """
        Whether the movie is a series
        """
        return self.res['series']
    
    @property
    def imdb_url(self) -> str:
        """
        Returns the URL of the movie on IMDB
        """
        return self.res['imdburl']
    