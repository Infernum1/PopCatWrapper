__all__ = ('Lyrics',)

class Lyrics:
    def __init__(self, res):
        self.res = res
    
    @property
    def title(self) -> str:
        return self.res['title']
        
    @property
    def thumbnail(self) -> str:
        return self.res['image']

    @property
    def artist(self) -> str:
        return self.res['artist']
    
    @property
    def lyrics(self) -> str:
        return self.res['lyrics']
    
