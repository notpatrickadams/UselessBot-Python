# The Price is Rice
import aiohttp

async def urban_dictionary(term):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.urbandictionary.com/v0/define?term={term}") as r:
            res_json = await r.json()
            if r.status == 200:
                return res_json["list"]
            else:
                raise Exception("Could not retrieve dictionary results")