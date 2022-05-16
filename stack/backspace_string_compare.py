from unittest import TestCase
from typing import List


class Solution:
    """
    https://leetcode.com/problems/backspace-string-compare/

    Evaluate each input string by appending chars to a stack, and popping if deletion is valid.

    Compare elements of both stacks.

    Time Complexity: O(N + M)
    Space Complexity: O(N + M)
    N - size of input string s
    M - size of input string t
    """

    def backspace_compare(self, s: str, t: str) -> bool:
        return self.evalute_backspace_string(
            s) == self.evalute_backspace_string(t)

    def evalute_backspace_string(self, s: str) -> List[str]:
        stack = []
        for char in s:
            if char == '#':
                if stack:
                    stack.pop()
                continue
            stack.append(char)
        return stack


class Solution2:
    """
    Follow-up - Can you solve it in O(n) time and O(1) space?

    Initialize 2 pointers, i, j, at the end of each string.
    Track count of deletes, '#', encountered.
    Iterating from the back of each string:
        If we encounter a '#', keep trimming valid backspaces.
        Any s[i] or t[j] we encounter are part of the final output string.
        If s[i] !=  t[j], the strings are not equal.
        If we've reached the end of one string, but not the other, the strings are not equal.

    Time Complexity: O(N + M)
    Space Complexity: O(1)
    """

    def backspace_compare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        deletes_s = deletes_t = 0
        while i >= 0 or j >= 0:
            # Trim backspaces in s
            while i >= 0:
                if s[i] == '#':
                    deletes_s += 1
                    i -= 1
                elif deletes_s > 0:
                    deletes_s -= 1
                    i -= 1
                else:
                    break
            # Trim backspaces in t
            while j >= 0:
                if t[j] == '#':
                    deletes_t += 1
                    j -= 1
                elif deletes_t > 0:
                    deletes_t -= 1
                    j -= 1
                else:
                    break

            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            if (i >= 0) != (j >= 0):
                return False
            i -= 1
            j -= 1

        return True


class TestSolution(TestCase):
    solution = Solution()
    solution2 = Solution2()

    def test_same_input(self):
        s = "ab#c"
        t = "ad#c"
        self.assertTrue(self.solution.backspace_compare(s, t))
        self.assertTrue(self.solution2.backspace_compare(s, t))

    def test_same_input_empty_final_string(self):
        s = "ab##"
        t = "y#x#"
        self.assertTrue(self.solution.backspace_compare(s, t))
        self.assertTrue(self.solution2.backspace_compare(s, t))

    def test_different_input(self):
        s = "a#c"
        t = "g"
        self.assertFalse(self.solution.backspace_compare(s, t))
        self.assertFalse(self.solution2.backspace_compare(s, t))

    def test_backspaces_until_empty(self):
        s = "bxj##tw"
        t = "bxj###tw"
        self.assertFalse(self.solution.backspace_compare(s, t))
        self.assertFalse(self.solution2.backspace_compare(s, t))

    def test_backspaces_past_empty(self):
        s = "bxj##tw"
        t = "bxj####tw"
        self.assertFalse(self.solution.backspace_compare(s, t))
        self.assertFalse(self.solution2.backspace_compare(s, t))

    def test_backspaces_past_empty_equal(self):
        s = "bxj#####tw"
        t = "bxj######tw"
        self.assertTrue(self.solution.backspace_compare(s, t))
        self.assertTrue(self.solution2.backspace_compare(s, t))

    def test_no_backspaces_same_input(self):
        s = "bxjtw"
        t = "bxjtw"
        self.assertTrue(self.solution.backspace_compare(s, t))
        self.assertTrue(self.solution2.backspace_compare(s, t))

    def test_no_backspaces_different_input(self):
        s = "bxjtw"
        t = "bxjtwa"
        self.assertFalse(self.solution.backspace_compare(s, t))
        self.assertFalse(self.solution2.backspace_compare(s, t))
