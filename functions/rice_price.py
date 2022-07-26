# The Price is Rice
import requests

def rice_price():
    r = requests.get("https://api.tradingeconomics.com//markets/search/rice?category=commodity&c=guest:guest&f=json")
    return r.json()[0]["Last"]