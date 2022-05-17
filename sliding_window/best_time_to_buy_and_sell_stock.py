from unittest import TestCase
from typing import List


class Solution:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

    We can use a greedy algorithm for this problem.

    Initialize max profit to 0, and buy price to first element.

    Iterate through each element of the array.
        Update max profit if a higher selling price is found.
        Update current buy price if cheaper price is found.

    Return max profit once we've reached the end of the array.

    Time Complexity: O(N)
    Space Complexity: O(1)
    N - size of input list
    """

    def max_profit(self, prices: List[int]) -> int:
        profit, curr_buy = 0, prices[0]
        for price in prices:
            if price - curr_buy > profit:
                profit = price - curr_buy
            if price < curr_buy:
                curr_buy = price
        return profit


class TestSolution(TestCase):
    solution = Solution()

    def test_array_of_len_1_returns_no_profit(self):
        prices = [1]
        self.assertEqual(0, self.solution.max_profit(prices))

    def test_prices_no_profit(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(0, self.solution.max_profit(prices))

    def test_profit(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(5, self.solution.max_profit(prices))
