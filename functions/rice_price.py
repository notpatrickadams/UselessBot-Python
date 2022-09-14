# The Price is Rice
import aiohttp

async def rice_price():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.quandl.com/api/v3/datasets/CHRIS/CME_RR1") as r:
            res_json = await r.json()
            if r.status == 200:
                return res_json["dataset"]["data"][0][4]
            else:
                return 0