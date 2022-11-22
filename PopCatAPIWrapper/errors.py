__all__ = [
    "NPMPackageNotFound"
    "ColorNotFound",
    "SteamAppNotFound",
    "GenericError",
    "NotValid",
    "SongNotFound",
    "FilmNotFound",
    "ElementNotFound",
]


class GenericError(Exception):
    """
    Exception raised during a generic error

    Attributes
    ----------
    msg: :class:`str`
        the error message
    """

    def __init__(self, msg):
        self.error = msg
        super().__init__(f"Encountered a generic error. {self.error}")


class NotValid(Exception):
    """
    Exception raised when the argument(s) given are invalid.
    """

    def __init__(self):
        super().__init__("The argument(s) given are invalid.")


class ElementNotFound(Exception):
    """
    Exception raised when the element is not found.
    """

    def __init__(self):
        super().__init__(f"Element could not be found")

class SubRedditNotFound(Exception):
    """
    Exception raised when the subreddit is not found.
    """

    def __init__(self):
        super().__init__(f"SubReddit could not be found")


class SongNotFound(Exception):
    """
    Exception raised when the song is not found.
    """

    def __init__(self):
        super().__init__(f"Song could not be found")


class FilmNotFound(Exception):
    """
    Exception raised when the film is not found.
    """

    def __init__(self):
        super().__init__(f"Film could not be found")


class SteamAppNotFound(Exception):
    """
    Exception raised when the steam application is not found.
    """

    def __init__(self):
        super().__init__(f"Steam application could not be found")

class NPMPackageNotFound(Exception):
    """
    Exception raised when the NPM Package is not found.
    """

    def __init__(self, err):
        super().__init__(err)

class ColorNotFound(Exception):
    """
    Exception raised when the color is not found.
    """

    def __init__(self):
        super().__init__(f"Color could not be found, make sure you are typing it correctly (refer documentation)")
