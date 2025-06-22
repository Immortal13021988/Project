import json


def transaction():
    try:
        with open("../data/operations.json", encoding="utf-8") as json_file:
            trans = json.load(json_file)
        return trans
    except Exception:
        return []
