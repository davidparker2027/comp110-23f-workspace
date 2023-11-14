"""Dictionary file for EX06!"""

__author__ = 730671567


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Will invert a dictionary when called."""
    e_dict: dict[str, str] = {}
    for key in dict1:
        e_dict[dict1[key]] = key
    if len(dict1) != len(e_dict):
        raise KeyError("You cannot have more than 1 of the same key!")
    return e_dict


def favorite_color(dict1: dict[str, str]) -> str:
    """Will return the favorite color."""
    e_dict: dict[str, int] = {}
    for key in dict1:
        if dict1[key] in e_dict:
            e_dict[dict1[key]] += 1
        else:
            e_dict[dict1[key]] = 1
    num: int = 0
    for key2 in e_dict:
        if e_dict[key2] > num:
            num = e_dict[key2]
    for color in e_dict:
        if e_dict[color] == num:
            return color
    return "green"


def count(listy: list[str]) -> dict[str, int]:
    """Function will count terms."""
    e_dict: dict[str, int] = {}
    for key in listy:
        if key in e_dict:
            e_dict[key] += 1
        else:
            e_dict[key] = 1
    return e_dict


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """Looks through a list and pairs a unique letter with words that begin with that letter."""
    e_dict = {}
    for key in list1:
        if key[0].lower() not in e_dict:
            e_dict[key[0].lower()] = [key]
        else:
            e_dict[key[0].lower()].append(key)
    return e_dict


def update_attendance(dict1: dict[str, list[str]], student: str, day: str) -> dict[str, list[str]]:
    """Function that updates attendance."""
    if student not in dict1:
        dict1[student] = [day]
    elif day not in dict1[student]:
        dict1[student].append(day)
    return dict1
    

attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
update_attendance(attendance_log, "Tuesday", "Vrinda")
print(attendance_log)  
