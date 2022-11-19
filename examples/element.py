import PopCatAPIWrapper
import asyncio
client = PopCatAPIWrapper.client.PopCatAPI()

async def el(element: str):
    element = await client.get_element_info(element=element)
    print(element.summary)

if __name__ == "__main__":
    asyncio.run(el("Oxygen"))