import PopCatAPIWrapper
import asyncio
client = PopCatAPIWrapper.client.PopCatAPI()

async def color(color: str):
    color_obj = await client.get_color_info(color=color)
    print(color_obj.name)

if __name__ == "__main__":
    asyncio.run(color("#547df0"))