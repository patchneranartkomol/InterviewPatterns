from unittest import TestCase
from typing import List


class Solution:
    """
    https://leetcode.com/problems/contains-duplicate/

    Iterate through the list once to store in a set (hash table).
    The size of the set grows with each unique value.

    Time Complexity: O(N)
    Space Complexity: O(N)
    N - size of input list
    """
    def contains_duplicate(self, nums: List[int]) -> bool:
        return True if len(nums) > len(set(nums)) else False


class TestSolution(TestCase):
    solution = Solution()

    def test_array_of_len_1(self):
        array = [1]
        self.assertFalse(self.solution.contains_duplicate(array))

    def test_contains_duplicates(self):
        array_with_duplicates = [1, 2, 3, 1]
        self.assertTrue(self.solution.contains_duplicate(array_with_duplicates))

    def test_does_not_contain_duplicate(self):
        array_without_duplicates = [1, 2, 3, 4]
        self.assertFalse(
            self.solution.contains_duplicate(array_without_duplicates))

    def test_longer_array_with_duplicates(self):
        longer_array_with_duplicates = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
        self.assertTrue(
            self.solution.contains_duplicate(longer_array_with_duplicates))
