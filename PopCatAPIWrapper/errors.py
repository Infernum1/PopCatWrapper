__all__ = ['NotValid', 'SongNotFound', 'MovieNotFound']

class NotValid(Exception):
    """
    Exception raised when the argument(s) given are invalid.
    """
    def __init__(self):
        super().__init__("The argument(s) given are invalid.")
    
class SongNotFound(Exception):
    """
    Exception raised when the song is not found.

    Attributes
    ----------
    name: :class:`str`
        name of the song that was not found
    """
    def __init__(self, name: str):
        self.name = name
        super().__init__(f"Song with the name {self.name} was not found")

class MovieNotFound(Exception):
    """
    Exception raised when the movie is not found.

    Attributes
    ----------
    title: :class:`str`
        title of the movie that was not found
    """
    def __init__(self, title: str):
        self.title = title
        super().__init__(f"Movie with the name {self.title} was not found")