"""Combining two lists into a dictionary."""
__author__ = 730671567


def zip(str_list: list[str], int_list: list[int]) -> dict[str, int]:
    """Compares two lits together."""
    dict_list: dict[str, int] = {}

    if len(str_list) != len(int_list):
        return dict_list
    
    idx: int = 0
    idx2: int = 0
    while idx < len(int_list):
        dict_list[str_list[idx]] = int_list[idx2]
        idx += 1
        idx2 += 1
    return dict_list


print(zip(["Happy", "Tuesday"], [1, 2]))