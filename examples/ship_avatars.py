import PopCatAPIWrapper
import asyncio
from io import BytesIO
from PIL import Image

client = PopCatAPIWrapper.client.PopCatAPI()


async def ship(img1, img2):
    image = await client.ship_avatars(image1=img1, image2=img2)
    im = Image.open(image)
    im.save("file.png")


if __name__ == "__main__":
    asyncio.run(ship("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwGGqJcSlXtMD1QWTuJhoTaXts8AKbmEkqUA&usqp=CAU", "https://i.natgeofe.com/k/5e4ea67e-2219-4de4-9240-2992faef0cb6/trump-portrait_3x4.jpg"))

