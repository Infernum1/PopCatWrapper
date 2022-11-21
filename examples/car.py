import PopCatAPIWrapper
import asyncio
from PIL import Image

client = PopCatAPIWrapper.client.PopCatAPI()

async def car_images():
    car = await client.get_car()
    im = Image.open(await car.get_car_image())
    im.save("car_image.png")
    print(car.name)
    print(car.image_url)


if __name__ == "__main__":
    asyncio.run(car_images())
