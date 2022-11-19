import PopCatAPIWrapper
import asyncio
client = PopCatAPIWrapper.client.PopCatAPI()

async def get_song(song_name: str):
    song_name = song_name.replace(" ", "+")
    song = await client.get_song_info(song=song_name)
    print(song.thumbnail_url)
    print(song.artist)
    print(song.lyrics)

if __name__ == "__main__":
    asyncio.run(get_song("my little pony"))