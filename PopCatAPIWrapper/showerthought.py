__all__ = ("ShowerThought",)


class ShowerThought:
    def __init__(self, res):
        self.res = res

    @property
    def thought(self) -> str:
        """
        The "shower thought"
        """
        return self.res["result"]

    @property
    def author(self) -> str:
        """
        Author of the "shower thought"
        """
        return self.res["author"]

    @property
    def upvotes(self) -> int:
        """
        Up-votes received
        """
        return self.res["upvotes"]
