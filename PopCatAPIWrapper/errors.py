__all__ = ['NotValid', 'SongNotFound', 'FilmNotFound', 'ElementNotFound']

class NotValid(Exception):
    """
    Exception raised when the argument(s) given are invalid.
    """
    def __init__(self):
        super().__init__("The argument(s) given are invalid.")

class ElementNotFound(Exception):
    """
    Exception raised when the element is not found.

    Attributes
    ----------
    name: :class:`str`
        name of the element that was not found
    """
    def __init__(self, name: str):
        self.name = name
        super().__init__(f"Element with the name {self.name} was not found")

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

class FilmNotFound(Exception):
    """
    Exception raised when the film is not found.

    Attributes
    ----------
    title: :class:`str`
        title of the film that was not found
    """
    def __init__(self, title: str):
        self.title = title
        super().__init__(f"A Film with the name {self.title} was not found")