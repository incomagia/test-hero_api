from src.heroes import get_tallest_hero
import pytest


get_tallest_hero("Female", True)

pytest.main(["tests", "-vv"])