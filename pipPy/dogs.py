import requests
import json


def doggie():
    f = r"https://random.dog/woof.json"
    page = requests.get(f)
    data = json.loads(page.text)
    return data["url"]
