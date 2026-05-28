import json
from pathlib import Path

from src.heroes import get_tallest_hero
from src.api import load_heroes_data


BASE_DIR = Path(__file__).resolve().parent.parent

LOADED_PATH = BASE_DIR / "tests" / "data" / "loaded.json"
ANSWER_PATH = BASE_DIR / "tests" / "data" / "answer.json"

# SMOKE
# 1. Проверка существования loaded.json
def test_loaded_file_exists():
    assert LOADED_PATH.exists()


# 2. Проверка чтения JSON
def test_loaded_json_can_be_loaded():
    with open(LOADED_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert data is not None


# 3. Проверка что JSON содержит список
def test_loaded_json_is_list():
    with open(LOADED_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)

    assert isinstance(data, list)


# 4. Проверка запуска функции поиска
def test_get_tallest_hero_runs():
    result = get_tallest_hero("Male", True)

    assert result is not None


# 5. Проверка создания answer.json
def test_answer_file_created():
    get_tallest_hero("Female", True)

    assert ANSWER_PATH.exists()

#POSITIVE
# 6 Male + work
def test_male_with_work():
    result = get_tallest_hero("Male", True)

    assert result is not None


# 7 Male + no work
def test_male_without_work():
    result = get_tallest_hero("Male", False)

    assert result is not None


# 8 Female + work
def test_female_with_work():
    result = get_tallest_hero("Female", True)

    assert result is not None


# 9 Female + no work
def test_female_without_work():
    result = get_tallest_hero("Female", False)

    assert result is not None

# NEGATIVE
# 10 Неверный gender
def test_wrong_gender():
    result = get_tallest_hero("Alien", True)

    assert result is None


# 11 Пустой gender
def test_empty_gender():
    result = get_tallest_hero("", True)

    assert result is None


# 12 gender = None
def test_none_gender():
    result = get_tallest_hero(None, True)

    assert result is None


# 13 has_work строкой вместо bool
def test_wrong_has_work_type():
    result = get_tallest_hero("Male", "yes")

    assert result is None


# 14 has_work = None
def test_none_has_work():
    result = get_tallest_hero("Female", None)

    assert result is None

# NonFunctional
# 15 function NOT mess with data
def test_source_data_not_modified():
    import copy
    import json

    with open(LOADED_PATH, encoding="utf-8") as file:
        original_data = json.load(file)

    original_copy = copy.deepcopy(original_data)

    get_tallest_hero("Male", True)

    with open(LOADED_PATH, encoding="utf-8") as file:
        current_data = json.load(file)

    assert current_data == original_copy

# 16 time work
def test_function_execution_speed():
    import time

    start = time.time()

    get_tallest_hero("Male", True)

    end = time.time()

    assert (end - start) < 1

# 17 multuply run
def test_multiple_runs_stability():
    for _ in range(100):
        result = get_tallest_hero("Female", True)

        assert result is not None

# 18 type of result?
def test_result_is_dict():
    result = get_tallest_hero("Male", True)

    assert isinstance(result, dict)

# 19 result is correct
def test_result_contains_required_fields():
    result = get_tallest_hero("Male", True)

    assert "name" in result
    assert "appearance" in result
    assert "work" in result

# 20 same? or podtype?
def test_result_contains_height():
    result = get_tallest_hero("Female", True)

    assert "height" in result["appearance"]

# 21 not empy - bad this is functional
def test_result_not_empty():
    result = get_tallest_hero("Male", True)

    assert result != {}

# 22 result is same
def test_same_request_same_result():
    result_1 = get_tallest_hero("Male", True)
    result_2 = get_tallest_hero("Male", True)

    assert result_1 == result_2

# 23 we have saved logo file
def test_answer_file_created():
    import os

    get_tallest_hero("Male", True)

    assert os.path.exists(ANSWER_PATH)

# 24 api worked
def test_loaded_file_created():
    import os

    load_heroes_data()

    assert os.path.exists(LOADED_PATH)

# 25 api is list
def test_loaded_data_is_list():
    import json

    load_heroes_data()

    with open(LOADED_PATH, encoding="utf-8") as file:
        data = json.load(file)

    assert isinstance(data, list)