import json
import uuid
import requests
from datetime import datetime, timezone
from config import TEMPLATE_PATH, ATHENA_PATH, template_type_matrix, ATHENA_TEMPLATE

def generate_athena():
    try:
        athena = ATHENA_TEMPLATE.copy()  

        print("[GEN] Fetching Fortnite cosmetics from Fortnite-API.com...")
        resp = requests.get("https://fortnite-api.com/v2/cosmetics/br")
        if resp.status_code != 200:
            print(f"[ERROR] Fortnite API returned {resp.status_code}")
            return

        data = resp.json().get("data", [])
        print(f"[GEN] Found {len(data)} cosmetics from Fortnite-API.com")

        athena["profileChanges"][0]["profile"]["items"] = {}
        
        for item in data:
            if not isinstance(item, dict):
                continue

            item_id = item.get("id")
            type_info = item.get("type", {})
            backend_value = type_info.get("backendValue")
            type_id = type_info.get("id")

            if not item_id or not backend_value:
                continue

            if "random" in item_id.lower():
                continue

            if type_id in template_type_matrix:
                backend_value = template_type_matrix[type_id]
            
            template_id = f"{backend_value}:{item_id.lower()}"
            
            guid = str(uuid.uuid4().hex).lower()
            
            item_data = {
                "templateId": template_id,
                "attributes": {
                    "max_level_bonus": 0,
                    "level": 1,
                    "item_seen": True,
                    "xp": 0,
                    "favorite": False,
                    "creation_time": "0001-01-01T01:01:01.100Z"
                },
                "quantity": 1
            }

            variants_data = []
            for variant in item.get("variants", []):
                variant_data = {
                    "channel": variant.get("channel", ""),
                    "active": variant.get("options", [{}])[0].get("tag", ""),
                    "owned": [opt.get("tag", "") for opt in variant.get("options", [])]
                }
                variants_data.append(variant_data)
            
            if variants_data:
                item_data["attributes"]["variants"] = variants_data

            athena["profileChanges"][0]["profile"]["items"][guid] = item_data

        victory_crown_guid = str(uuid.uuid4().hex).lower()
        athena["profileChanges"][0]["profile"]["items"][victory_crown_guid] = {
            "templateId": "VictoryCrown:defaultvictorycrown",
            "attributes": {
                "victory_crown_account_data": {
                    "has_victory_crown": False,
                    "data_is_valid_for_mcp": True,
                    "total_victory_crowns_bestowed_count": 0,
                    "total_royal_royales_achieved_count": 0
                },
                "max_level_bonus": 0,
                "level": 1,
                "item_seen": False,
                "xp": 0,
                "favorite": False
            },
            "quantity": 999
        }

        current_time = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
        athena["profileChanges"][0]["profile"]["updated"] = current_time
        athena["serverTime"] = current_time
        athena["updated"] = current_time

        with open(ATHENA_PATH, "w", encoding="utf-8") as f:
            json.dump(athena, f, indent=2)

        print(f"[GEN] Athena generated successfully ({len(athena['profileChanges'][0]['profile']['items'])} items)")

    except Exception as e:
        print(f"[ERROR] Failed to generate Athena: {e}")