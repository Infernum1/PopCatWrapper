import PopCatAPIWrapper
import asyncio

client = PopCatAPIWrapper.client.PopCatAPI()


async def npm(name: str):
    npm_obj = await client.get_npm_package(package_name=name)
    print(npm_obj.description)
    print(npm_obj.author)
    print(npm_obj.author_email)
    print(npm_obj.downloads_this_year)
    print(npm_obj.repository)


if __name__ == "__main__":
    asyncio.run(npm("package"))
