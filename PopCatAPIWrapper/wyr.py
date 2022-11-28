__all__ = ("Wyr",)


class Wyr:
    def __init__(self, res):
        self.res = res

    @property
    def option1(self) -> str:
        """
        The **first** option of the Would You Rather
        """
        return self.res["ops1"]

    @property
    def option2(self) -> str:
        """
        The **second** option of the Would You Rather
        """
        return self.res["ops2"]
