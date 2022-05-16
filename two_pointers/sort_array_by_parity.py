from unittest import TestCase
from typing import List


class Solution:
    """
    https://leetcode.com/problems/sort-array-by-parity/

    Use a pointer, called start, to keep track of where evens are swapped to, beginning with index 0.
    Iterate through the list.
    If we encounter an even number, swap to the starting even index, and increment start index.

    Time Complexity: O(N)
    Space Complexity: O(1)
    N - size of input list
    """

    def sort_array_by_parity(self, nums: List[int]) -> List[int]:
        start = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[start] = nums[start], nums[i]
                start += 1
        return nums


class TestSolution(TestCase):
    solution = Solution()

    def test_array_of_len_1(self):
        array = [1]
        self.assertTrue(
            self.check_array_parity(self.solution.sort_array_by_parity(array)))

    def test_array_input(self):
        array = [1, 5, 2, 10]
        self.assertTrue(
            self.check_array_parity(self.solution.sort_array_by_parity(array)))

    def test_array_input2(self):
        array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertTrue(
            self.check_array_parity(self.solution.sort_array_by_parity(array)))

    @staticmethod
    def check_array_parity(array: List[int]) -> bool:
        odd_found = False
        for num in array:
            if odd_found and num % 2 == 0:  # pragma: no cover
                return False
            if num % 2 != 0:
                odd_found == True
        return True
