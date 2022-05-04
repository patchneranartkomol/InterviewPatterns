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
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(nums) > len(set(nums)) else False


class TestSolution(TestCase):
    solution = Solution()

    def testArrayOfLen1(self):
        array = [1]
        self.assertFalse(self.solution.containsDuplicate(array))

    def testContainsDuplicates(self):
        array_with_duplicates = [1,2,3,1]
        self.assertTrue(self.solution.containsDuplicate(array_with_duplicates))

    def testDoesNotContainDuplicate(self):
        array_without_duplicates = [1,2,3,4]
        self.assertFalse(self.solution.containsDuplicate(array_without_duplicates))

    def testLongerArrayWithDuplicates(self):
        longer_array_with_duplicates = [1,1,1,3,3,4,3,2,4,2]
        self.assertTrue(self.solution.containsDuplicate(longer_array_with_duplicates))
