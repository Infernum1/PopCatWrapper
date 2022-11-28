import PopCatAPIWrapper
import asyncio

client = PopCatAPIWrapper.client.PopCatAPI()


async def fact():
    fact = await client.get_fact()
    print(fact)


if __name__ == "__main__":
    asyncio.run(fact())
