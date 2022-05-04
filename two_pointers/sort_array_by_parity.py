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
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        start = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i], nums[start] = nums[start], nums[i]
                start += 1
        return nums


class TestSolution(TestCase):
    solution = Solution()

    def testArrayOfLen1(self):
        array = [1]
        self.assertTrue(self.checkArrayParity(self.solution.sortArrayByParity(array)))

    def testArrayInput(self):
        array = [1,5,2,10]
        self.assertTrue(self.checkArrayParity(self.solution.sortArrayByParity(array)))

    @staticmethod
    def checkArrayParity(array: List[int]) -> bool:
        odd_found = False
        for num in array:
            if odd_found and num % 2 == 0:
                return False
            if num % 2 != 0:
                odd_found == True
        return True


if __name__ == '__main__':
    main()
