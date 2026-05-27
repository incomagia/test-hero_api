import json
from pathlib import Path

import requests


API_URL = "https://akabab.github.io/superhero-api/api/all.json"


def load_heroes_data():
    response = requests.get(API_URL)

    if response.status_code != 200:
        raise Exception(f"API request failed: {response.status_code}")

    data = response.json()

    project_root = Path(__file__).resolve().parent.parent
    output_file = project_root / "tests" / "data" / "loaded.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"Loaded {len(data)} heroes")
    print(f"Saved to: {output_file}")


if __name__ == "__main__":
    load_heroes_data()