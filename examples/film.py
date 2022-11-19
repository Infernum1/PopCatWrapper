import PopCatAPIWrapper
import asyncio

client = PopCatAPIWrapper.client.PopCatAPI()


async def get_film(film_name: str):
    film = await client.get_film_info(film=film_name)
    print(film.ratings)
    print(film.actors)
    print(film.runtime)


if __name__ == "__main__":
    asyncio.run(get_film("Iron Man"))
