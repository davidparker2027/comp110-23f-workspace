"""EX07 Assignment!"""

__author__ = 730671567

from dictionary import invert
from dictionary import favorite_color
from dictionary import count
from dictionary import alphabetizer
from dictionary import update_attendance


# Testing invert


def test_invert() -> None:
    """Testing an empty dictionary!"""
    assert invert({}) == {}


def test_invert_1() -> None:
    """Testing a dictionary!"""
    assert invert({"red": "apple", "blue": "melon"}) == {"apple": "red", "melon": "blue"}


def test_invert_2() -> None:
    """Testing another dictionary!"""
    assert invert({"Apple": "Red", "Banana": "Yellow"}) == {"Red": "Apple", "Yellow": "Banana"}


# Testing Favorite Color


def test_fav_color() -> None:
    """Testing an empty dictionary!"""
    assert favorite_color({}) == "green"


def test_fav_color_1() -> None:
    """Testing a dictionary with 1 color!"""
    assert favorite_color({"Comp": "green"}) == "green"


def test_fav_color_2() -> None:
    """Testing a dictionary with 2 colors!"""
    assert favorite_color({"Comp": "green", "Math": "blue"}) == "green"


# Testing count


def test_count() -> None:
    """Testing count with an empty list!"""
    assert count([]) == {}


def test_count_1() -> None:
    """Testing count with a list!"""
    assert count(["Chicken", "Soup"]) == {2}


def test_count_2() -> None:
    """Testing count with a longer list!"""
    assert count(["Pizza", "Bread", "Tenders", "Tenders"]) == {4}


# Testing alphabetizer


def test_alphabetizer() -> None:
    """Testing alphabetizer with an empty list!"""
    assert alphabetizer([]) == {}


def test_alphabetizer_1() -> None:
    """Testing alphabetizer with a list!"""
    assert alphabetizer(["Bug", "Bagel", "Bread"]) == {"B": ["Bagel", "Bread", "Bug"]}


def test_alphabetizer_2() -> None:
    """Testing alphabetizer with a short list!"""
    assert alphabetizer(["David", "Andrew"]) == {"A": ["Andrew"], "D": ["David"]}


# Testing update_attendance


def test_update_attendance() -> None:
    """Testing update_attendance with an empty dictionary!"""
    assert update_attendance({}, "Monday", "Deku") == {"Monday": ["Deku"]}


def test_update_attendance1() -> None:
    """Testing update_attendance!"""
    assert update_attendance({"monday": ["david", "luke"]}, "monday", "deku") == {"monday": ["david", "deku", "luke"]}


def test_update_attendance2() -> None:
    """Testing update_attendance with another list!"""
    assert update_attendance({"monday": ["david", "hikari"]}, "monday", "kai") == {"monday": ["david", "hikari", "kai"]}
