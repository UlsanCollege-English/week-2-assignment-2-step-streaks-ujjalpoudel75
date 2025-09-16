from typing import List, Tuple

def max_window_sum(values: List[int], k: int) -> Tuple[int, int] | None:
    if k <= 0:
        raise ValueError
    if k > len(values):
        return None
    s = sum(values[:k])
    best = (0, s)
    for i in range(1, len(values) - k + 1):
        s = s - values[i-1] + values[i+k-1]
        if s > best[1]:
            best = (i, s)
    return best

def count_goal_windows(values: List[int], k: int, target_avg: float) -> int:
    if k <= 0:
        raise ValueError
    if k > len(values):
        return 0
    s = sum(values[:k])
    count = 1 if s / k >= target_avg else 0
    for i in range(1, len(values) - k + 1):
        s = s - values[i-1] + values[i+k-1]
        if s / k >= target_avg:
            count += 1
    return count

def longest_rising_streak(values: List[int]) -> int:
    if not values:
        return 0
    longest = current = 1
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            current += 1
            if current > longest:
                longest = current
        else:
            current = 1
    return longest
