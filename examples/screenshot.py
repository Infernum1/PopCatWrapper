import PopCatAPIWrapper
import asyncio
from io import BytesIO
from PIL import Image

client = PopCatAPIWrapper.client.PopCatAPI()

async def screenshot_site(url: str):
    image = await client.get_screenshot(url=url)
    im = Image.open(image)
    im.save("file.png")


if __name__ == "__main__":
    asyncio.run(screenshot_site("https://twitch.tv"))

#Something similar can be done for the 'sadcat meme' module