

An async API wrapper around [popcat-api](https://popcat.xyz/api)


### Get started || [Documentation](https://popcat-api.readthedocs.io/en/latest/)

#### to get started, type this in your terminal
```
pip install -U PopCatWrapper
```

#### or to install the main branch
```
pip install -U git+https://github.com/Infernum1/PopCatWrapper
```
###### (make sure you have [git](https://gitforwindows.org) installed)
### Examples

#### For examples, checkout the [examples directory](https://github.com/Infernum1/PopCatWrapper/tree/main/examples)
##### If you plan to use the lib in a discord bot

```py
import discord
import PopCatWrapper

client = PopCatWrapper.PopCatAPI()
bot = discord.ext.commands.Bot()

@bot.command()
async def element(element: str): #you can feed either the atomic number, symbol, or element name
  image = await client.get_element_info(element)
  await ctx.send(content=element.summary)
```

###### these are just examples! it's upto you how you want to use this lib.

### Add `Infernum#7041` on discord for help
