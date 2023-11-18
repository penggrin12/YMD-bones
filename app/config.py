from genericpath import isfile
import json
import os.path

if not os.path.isfile("config.json"):
    with open("config.json", "w") as file:
        json.dump({"allow_external_apps": False, "discord_id": 1175386427681415241}, file)

with open("config.json", "r") as file:
    json_config = json.load(file)

ALLOW_EXTERNAL_APPS = json_config["allow_external_apps"]
DISCORD_ID = json_config["discord_id"]
