from functools import lru_cache
from unittest import TestCase
from typing import List


class Solution:

    def coin_change(self, coins: List[int], amount: int) -> int:
        """
        https://leetcode.com/problems/coin-change/

        Recursively evaluate subtracting all possible types of coins
        from amount.

        Base Cases:
        1) amount < 0, choice of coins did not make up amount
        2) amount == 0, choice of coins make up exact amount

        Recursive case:
        Recursively evalute subtracting c from amount, for all c in coins.
        Take the smallest successful result and add 1 coin used in this iteration.

        The lru_cache decorator memoizes this function, to avoid repeated
        work when we run into the same amount by subtracting different coins.

        Time - O(N * C)
        Space - O(N * C)
        Where N is the amount, and C is the number of coins.
        """

        @lru_cache(maxsize=None)
        def _backtrack_coins(amount: int) -> int:
            if amount < 0:
                return float('inf')
            if amount == 0:
                return 0
            return min(1 + _backtrack_coins(amount - c) for c in coins)

        count = _backtrack_coins(amount)
        return count if count != float('inf') else -1


class TestSolution(TestCase):
    solution = Solution()

    def test_3_coins(self):
        coins = [1, 2, 5]
        amount = 11
        self.assertEqual(3, self.solution.coin_change(coins, amount))

    def test_impossible_change(self):
        coins = [2]
        amount = 5
        self.assertEqual(-1, self.solution.coin_change(coins, amount))

    def test_change_for_no_amount(self):
        coins = [1]
        amount = 0
        self.assertEqual(0, self.solution.coin_change(coins, amount))

    def test_quarters(self):
        coins = [1, 5, 10, 25]
        amount = 157
        self.assertEqual(9, self.solution.coin_change(coins, amount))
