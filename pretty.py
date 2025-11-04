import json

with open("JSON/content.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open("JSON/content.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("JSON file formatted successfully!")