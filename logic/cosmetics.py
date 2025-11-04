import json
import requests
from config import ALL_COSMETICS

def get_all_cosmetics():
    resp = requests.get("https://fortnite-api.com/v2/cosmetics")
    data = resp.json().get("data")

    if not data:
        print("[ERROR] Failed to get data")
        return

    with open(ALL_COSMETICS, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)