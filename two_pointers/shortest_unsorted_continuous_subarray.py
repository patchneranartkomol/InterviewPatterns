from unittest import TestCase
from typing import List


class Solution:
    """
    https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

    If the array is one element, return 0.

    Iterate through array from the front to find the index of the last element that is unsorted.
    Iterate through array from the back to find the index of the first element that is unsorted.

    If found, return the distance between those elements.

    Time Complexity: O(N)
    Space Complexity: O(1)
    N - size of input list
    """

    def find_unsorted_subarray(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        # one forward pass - find the last element
        prev, last = nums[0], 0
        for i, num in enumerate(nums):
            if num < prev:
                last = i
            else:
                prev = num

        # one backward pass - find the first element out of place
        prev, first = nums[-1], len(nums) - 1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > prev:
                first = i
            else:
                prev = nums[i]

        return last - first + 1 if last > 0 else 0


class TestSolution(TestCase):
    solution = Solution()

    def test_array_of_len_1(self):
        array = [1]
        self.assertEqual(0, self.solution.find_unsorted_subarray(array))

    def test_sorted_input(self):
        array = [1, 2, 3, 5, 10]
        self.assertEqual(0, self.solution.find_unsorted_subarray(array))

    def test_input_1(self):
        array = [2, 6, 4, 8, 10, 9, 15]
        self.assertEqual(5, self.solution.find_unsorted_subarray(array))
