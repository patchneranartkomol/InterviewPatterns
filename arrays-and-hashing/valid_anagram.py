from collections import Counter
from unittest import TestCase


class Solution:
    """
    https://leetcode.com/problems/valid-anagram/

    Iterate through s and t, storing a count of each character in a hash table.
    Python gives a convenient library implementation called Counter.

    For example 2, the dictionaries look like this:
    S -
    {
        'r': 1,
        'a': 1,
        't': 1
    }
    T -
    {
        'c': 1,
        'a': 1,
        'r': 1

    }

    Then compare each key in each dictionary, and check that their values are equal.

    Time Complexity - O(N)
    Space Complexity - O(N)
    N - sum of length of input strings, s + t
    """

    def is_anagram(self, s: str, t: str) -> bool:
        return True if Counter(t) == Counter(s) else False


class TestSolution(TestCase):
    solution = Solution()

    def test_anagram(self):
        s = "anagram"
        t = "nagaram"
        self.assertTrue(self.solution.is_anagram(s, t))

    def test_not_anagram(self):
        s = "rat"
        t = "car"
        self.assertFalse(self.solution.is_anagram(s, t))
