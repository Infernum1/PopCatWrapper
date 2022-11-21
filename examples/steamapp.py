import PopCatAPIWrapper
import asyncio

client = PopCatAPIWrapper.client.PopCatAPI()


async def steam(name: str):
    steamapp = await client.get_steam_app(app_name=name)
    print(steamapp.description)


if __name__ == "__main__":
    asyncio.run(steam("God Of War"))
