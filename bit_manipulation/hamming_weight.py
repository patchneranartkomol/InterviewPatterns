from unittest import TestCase


class Solution:
    """
    https://leetcode.com/problems/number-of-1-bits/

    Increment total count if rightmost set bit, if it equals 1.
    Right shift the integer until it is 0.

    Time Complexity: O(1) - O(64) -> O(c) -> O(1) if the largest possible value is a 64-bit integer
    Space Complexity: O(1)
    """

    def hamming_weight(self, n: int) -> int:
        weight = 0
        while n:
            if n & 1:
                weight += 1
            n >>= 1
        return weight


class TestSolution(TestCase):
    solution = Solution()

    def test_1_set(self):
        self.assertEqual(self.solution.hamming_weight(128), 1)

    def test_3_set(self):
        self.assertEqual(self.solution.hamming_weight(3), 2)

    def test_31_set(self):
        self.assertEqual(self.solution.hamming_weight(4294967293), 31)
