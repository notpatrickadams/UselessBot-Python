import requests

# Steals ideas from itsthisforthat.com
BASE_URL = "https://itsthisforthat.com/api.php?json"

def idea_generator():
    try:
        res = requests.get("https://itsthisforthat.com/api.php?json").json()
        return f"Basically, it's { res['this'] } for { res['that'] }"
    except:
        return "Error generating random idea."