import os
import json
from flask import jsonify

def load_json(filename):
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "JSON/" + filename)
    if not os.path.exists(path):
        return {"error": f"{filename} not found"}
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {"error": f"{filename} is invalid JSON"}