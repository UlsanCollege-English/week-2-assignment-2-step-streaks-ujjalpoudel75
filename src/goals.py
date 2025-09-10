"""Step Streaks — Starter

You are analyzing a user's daily step counts.
Implement without mutating inputs.
"""
from typing import List, Tuple


def max_window_sum(values: List[int], k: int) -> Tuple[int, int] | None:
    """Return (start_index, window_sum) of the largest sum among all length-k windows.

    If k <= 0, raise ValueError. If k > len(values), return None.
    """
    raise NotImplementedError


def count_goal_windows(values: List[int], k: int, target_avg: float) -> int:
    """Return how many length-k windows have average >= target_avg.

    If k <= 0, raise ValueError. If k > len(values), return 0.
    """
    raise NotImplementedError


def longest_rising_streak(values: List[int]) -> int:
    """Return the length of the longest strictly increasing consecutive streak.

    Empty list -> 0. Single element -> 1.
    """
    raise NotImplementedError