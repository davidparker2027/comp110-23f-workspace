"""Test my zip function."""

__author__ = 730671567

from lessons.zip import zip


def test_list1() -> None:
    """Empty Function is tested."""
    assert zip([], []) == {}


def test_contains_elem() -> None:
    """Testing to see if an element is contained."""
    test1: dict[str, int] = {"Yes": 1}
    x: list[str] = ["Yes"]
    y: list[int] = [1]
    assert zip(x, y) == test1


def test_contains_two_elem() -> None:
    """Testing to see if two elements are contained."""
    test2: dict[str, int] = {"Yes": 1, "No": 2}
    x: list[str] = ["Yes", "No"]
    y: list[int] = [1, 2]
    assert zip(x, y) == test2