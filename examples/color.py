import PopCatAPIWrapper
import asyncio
from PIL import Image

client = PopCatAPIWrapper.client.PopCatAPI()


async def color(color: str):
    color_obj = await client.get_color_info(color=color)
    print(color_obj.name)
    print(color_obj.brightened)
    print(color_obj.hex)
    print(color_obj.rgb)
    im = Image.open(await color_obj.get_color_image())
    im.save("image.png")


if __name__ == "__main__":
    asyncio.run(color("547df0"))
