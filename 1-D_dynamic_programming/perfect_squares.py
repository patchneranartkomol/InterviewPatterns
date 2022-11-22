from functools import lru_cache
from unittest import TestCase
from typing import List


class Solution:

    def num_squares(self, n: int) -> int:
        """
        https://leetcode.com/problems/perfect-squares/

        Top-down dynamic programming approach to perfect squares. Very similar to Coin Change.

        Recursively evaluate all possible squares summing to amount, n.

        Base Cases:
        1) amount < 0, choice of square did not sum up.
        2) amount == 0, choice of square made exact

        Recursive case:
        Recursively evalute subtracting the square from amount, for all squares < the sum.
        Take the smallest result and add 1 to total.

        The lru_cache decorator memoizes this function, to avoid repeated work.

        Time - O(N * sqrt(N))
        Space - O(N) # Call stack + cache
        """
        squares = []
        # Compute squares from 1 to sqrt(n)
        for i in range(1, n + 1):
            s = i**2
            if s > n:
                break
            squares.append(s)
        return self.dp_squares(squares, n)

    def dp_squares(self, squares: List[int], amount: int) -> int:

        @lru_cache(maxsize=None)
        def dp(amount: int) -> int:
            if amount < 0:
                return float('inf')
            if amount == 0:
                return 0
            return min(1 + dp(amount - s) for s in squares)

        return dp(amount)


class TestSolution(TestCase):
    solution = Solution()

    def test_13(self):
        amount = 13
        self.assertEqual(2, self.solution.num_squares(amount))

    def test_12(self):
        amount = 12
        self.assertEqual(3, self.solution.num_squares(amount))
