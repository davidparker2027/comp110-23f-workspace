"""Challenge Lesson."""


def w_sum(x: list[float]) -> float:
    """Using a While Loop."""
    idx: int = 0
    answer: float = 0.0

    while idx < len(x):  
        answer += x[idx]  
        idx += 1

    return answer  


def f_sum(y: list[float]) -> float:
    """Using a For Loop."""
    answer: float = 0.0
    for elem in y:
        answer += elem
    return answer


def f_range_sum(z: list[float]) -> float:
    """Using range()."""
    answer: float = 0.0
    for elem in range(0, len(z)): 
        answer += z[elem]  
    return answer