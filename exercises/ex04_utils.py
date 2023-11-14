"""Ex04 Assignment!"""


def all(num_list: list[int], num: int) -> bool:
    """Sees if a given number is found in a given string of integers."""
    # num_list: list[int] = list()
    index: int = 0
    if len(num_list) == 0:
        return False
    while index < len(num_list):
        if str(num) == str(num_list[index]):
            index += 1
        else:
            return False
    return True


def max(nums: list[int]) -> int:
    """Finds the max number in a givn list of integers."""
    if len(nums) == 0:
        raise ValueError("max() age is an empty list")
    largest = nums[0]
    index: int = 1
    while index < len(nums):
        if nums[index] > largest:
            largest = nums[index]
        index += 1
    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Sees if two lists are equal."""
    index: int = 0
    if len(list1) != len(list2):
        return False
    while index < len(list1):
        if list1[index] == list2[index]:
            index = index + 1
        else:
            return False
    return True