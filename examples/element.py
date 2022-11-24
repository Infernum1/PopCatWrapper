import PopCatAPIWrapper
import asyncio
from PIL import Image
client = PopCatAPIWrapper.client.PopCatAPI()


async def el(el: str):
    element = await client.get_element_info(element=el)
    print(element.summary)
    print(element.atomic_mass)
    print(element.atomic_number)
    print(element.chemical_symbol)
    im = Image.open(await element.get_image())
    im.save("image.png")


if __name__ == "__main__":
    asyncio.run(el("Oxygen"))
