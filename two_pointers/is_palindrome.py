import re

from unittest import TestCase


class Solution:
    """
    https://leetcode.com/problems/valid-palindrome/

    Declare left and right pointers. Iterate through the string
    by incrementing left, and decrementing right until we meet in the middle.

    Ignore any non-alphanumeric characters.

    Check that lower-cased s[left] and s[right] are equal.

    Time Complexity: O(N)
    Space Complexity: O(1)
    N - size of input list
    """
    def is_palindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and right > left:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


class Solution2:
    """
    Build a new string with non-alphanumeric chars removed, all lower cased.

    Compare the first element with the last element, then compare each subsequent element.

    Time Complexity: O(N)
    Space Complexity: O(N) - building another string of worst case length N
    N - size of input list
    """
    def is_palindrome(self, s: str) -> bool:
        s = re.sub(r'\W+', '', s).lower()
        for i in range(len(s) // 2):
            if s[i] is not s[-(i + 1)]:
                return False
        return True


class TestSolution(TestCase):
    solution = Solution()
    solution2 = Solution2()

    def test_valid_palindrome(self):
        string = "racecar"
        self.assertTrue(self.solution.is_palindrome(string))
        self.assertTrue(self.solution2.is_palindrome(string))

    def test_invalid_palindrome(self):
        string = "racecara"
        self.assertFalse(self.solution.is_palindrome(string))
        self.assertFalse(self.solution2.is_palindrome(string))

    def test_valid_palindrome_with_nonalnum_chars(self):
        string = "A man, a plan, a canal: Panama"
        self.assertTrue(self.solution.is_palindrome(string))
        self.assertTrue(self.solution2.is_palindrome(string))

    def test_invalid_palindrome_with_nonalnum_chars(self):
        string = "a  z."
        self.assertFalse(self.solution.is_palindrome(string))
        self.assertFalse(self.solution2.is_palindrome(string))

    def test_valid_empty_palindrome_with_nonalnum_chars(self):
        string = "  ."
        self.assertTrue(self.solution.is_palindrome(string))
        self.assertTrue(self.solution2.is_palindrome(string))
