import json

FILE = "knowledge.json"

def save_fact(key, value):
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
    except:
        data = {}

    data[key] = value

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_fact(key):
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
        return data.get(key)
    except:
        return None
