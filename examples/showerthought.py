import PopCatAPIWrapper
import asyncio

client = PopCatAPIWrapper.client.PopCatAPI()


async def get_thought():
    thought = await client.get_shower_thought()
    print(thought.author)
    print(thought.upvotes)
    print(thought.thought)


if __name__ == "__main__":
    asyncio.run(get_thought())
