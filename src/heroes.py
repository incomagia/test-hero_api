import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SAMPLE_PATH = BASE_DIR / "tests" / "data" / "sample.json"
ANSWER_PATH = BASE_DIR / "tests" / "data" / "answer.json"


def get_tallest_hero(gender, has_work):
    with open(SAMPLE_PATH, "r", encoding="utf-8") as file:
        heroes = json.load(file)

    filtered_heroes = []

    for hero in heroes:
        hero_gender = hero["appearance"]["gender"]

        occupation = hero["work"]["occupation"]

        # Есть ли работа
        hero_has_work = (
                occupation is not None
                and occupation != ""
                and occupation != "-"
        )

        if hero_gender != gender:
            continue

        if hero_has_work != has_work:
            continue

        # Рост
        height_str = hero["appearance"]["height"][1]

        try:
            height_cm = int(height_str.replace(" cm", ""))
        except ValueError:
            height_cm = 0

        hero["height_cm"] = height_cm

        filtered_heroes.append(hero)

    if not filtered_heroes:
        print("Герои не найдены")
        return None

    tallest_hero = max(filtered_heroes, key=lambda hero: hero["height_cm"])

    # Сохраняем answer.json
    with open(ANSWER_PATH, "w", encoding="utf-8") as file:
        json.dump(tallest_hero, file, indent=4, ensure_ascii=False)

    print("Самый высокий герой:")
    print(tallest_hero["name"])
    print(f'Рост: {tallest_hero["height_cm"]} cm')

    return tallest_hero