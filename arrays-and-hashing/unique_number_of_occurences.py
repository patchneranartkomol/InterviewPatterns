from collections import Counter
from unittest import TestCase
from typing import List


class Solution:
    """
    https://leetcode.com/problems/unique-number-of-occurrences

    Count frequencies of each element in the array using a counter dict.

    Iterate through values of counter dict to verify if frequencies are unique.

    Time Complexity: O(N)
    Space Complexity: O(N)
    """

    def unique_occurences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        num_occurences = set()
        for n in counts.values():
            if n in num_occurences:
                return False
            num_occurences.add(n)
        return True


class TestSolution(TestCase):
    solution = Solution()

    def test_basic_valid_input(self):
        arr = [1, 2, 2, 1, 1, 3]
        self.assertTrue(self.solution.unique_occurences(arr))

    def test_nonunique(self):
        arr = [1, 2]
        self.assertFalse(self.solution.unique_occurences(arr))

    def test_longer_valid_input(self):
        arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
        self.assertTrue(self.solution.unique_occurences(arr))
