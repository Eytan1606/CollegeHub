import json
from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

def save_data(entity, data):
    with open(DATA_DIR / f"{entity}.json" , "w") as f:
        json.dump(data, f, indent=2)

def load_data(entity):
    file_path = DATA_DIR / f"{entity}.json"
    if file_path.exists():
        with open(file_path) as f:
            return json.load(f)
    return []

