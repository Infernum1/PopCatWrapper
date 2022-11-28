import PopCatAPIWrapper
import asyncio
from io import BytesIO
from PIL import Image

client = PopCatAPIWrapper.client.PopCatAPI()


async def screenshot_site(f1, f2):
    image = await client.get_welcome_card(
        first_field=f1, second_field=f2, third_field="F3", avatar="https://cdn.discordapp.com/embed/avatars/0.png"
    )
    im = Image.open(image)
    im.save("file.png")


if __name__ == "__main__":
    asyncio.run(screenshot_site("First field", "Second field"))

# Something similar can be done for the 'sadcat meme' module
