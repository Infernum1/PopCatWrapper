from .http import HTTPClient
from io import BytesIO

__all__ = ("NPMPackage",)


class NPMPackage(HTTPClient):
    def __init__(self, res):
        self.res = res

    @property
    def name(self) -> str:
        """
        The name of the NPM package
        """
        return self.res["name"]

    @property
    def version(self) -> str:
        """
        The version of the NPM package
        """
        return self.res["version"]

    @property
    def description(self) -> str:
        """
        The description of the NPM package
        """
        return self.res["description"]

    @property
    def keywords(self) -> str:
        """
        Keywords of the NPM package
        """
        return self.res["keywords"]

    @property
    def author(self) -> str:
        """
        The author of the NPM package
        """
        return self.res["author"]

    @property
    def author_email(self) -> str:
        """
        The email of the author of the NPM package
        """
        return self.res["author_email"]

    @property
    def last_published(self) -> str:
        """
        Last publish date of the NPM package
        """
        return self.res["discovered_by"]

    @property
    def maintainers(self) -> str:
        """
        The maintainers of the NPM package
        """
        return self.res["maintainers"]

    @property
    def repository(self) -> str:
        """
        The repository of the NPM package
        """
        return self.res["repository"]

    @property
    def downloads_this_year(self) -> str:
        """
        Total downloads of the NPM package in this year
        """
        return self.res["downloads_this_year"]
