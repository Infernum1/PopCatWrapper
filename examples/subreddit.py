import PopCatAPIWrapper
import asyncio

client = PopCatAPIWrapper.client.PopCatAPI()


async def get_subr(name: str):
    film = await client.get_subreddit(name)
    print(film.active_users)
    print(film.banner_url)


if __name__ == "__main__":
    asyncio.run(get_subr("memes"))
