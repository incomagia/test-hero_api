import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "tests" / "data" / "loaded.json"


def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def test_file_exists():
    assert DATA_FILE.exists()


def test_data_is_list():
    data = load_data()
    assert isinstance(data, list)


def test_data_is_not_empty():
    data = load_data()
    assert len(data) > 0


def test_first_hero_has_name():
    data = load_data()
    assert "name" in data[0]


def test_first_hero_has_appearance():
    data = load_data()
    assert "appearance" in data[0]


def test_first_hero_has_work():
    data = load_data()
    assert "work" in data[0]


def test_hero_has_gender_field():
    data = load_data()
    assert "gender" in data[0]["appearance"]


def test_hero_has_height_field():
    data = load_data()
    assert "height" in data[0]["appearance"]


def test_hero_has_occupation_field():
    data = load_data()
    assert "occupation" in data[0]["work"]


def test_at_least_one_male_hero_exists():
    data = load_data()

    males = [
        hero for hero in data
        if hero["appearance"]["gender"] == "Male"
    ]

    assert len(males) > 0

def test_data_IS_empty():
    data = load_data()
    assert len(data) == 0