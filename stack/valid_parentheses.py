from unittest import TestCase

OPEN_PARENTHESES = {'(', '{', '['}


class Solution:
    """
    https://leetcode.com/problems/valid-parentheses

    Iterate through the input string, adding open parens to stack.

    Compare closing parens in string to top element of stack.

    Time Complexity: O(N)
    Space Complexity: O(N)
    """

    def is_valid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in OPEN_PARENTHESES:
                stack.append(c)
            else:
                if not stack:
                    return False
                check = stack.pop()
                if check == '(' and c != ')':
                    return False
                elif check == '{' and c != '}':
                    return False
                elif check == '[' and c != ']':
                    return False

        return True if not stack else False


class TestSolution(TestCase):
    solution = Solution()

    def test_basic_valid_input(self):
        s = "()"
        self.assertTrue(self.solution.is_valid(s))

    def test_extended_valid_input(self):
        s = "()[]{}"
        self.assertTrue(self.solution.is_valid(s))

    def test_invalid_bracket(self):
        s = "(]"
        self.assertFalse(self.solution.is_valid(s))

    def test_invalid_bracket2(self):
        s = "[}"
        self.assertFalse(self.solution.is_valid(s))

    def test_invalid_bracket3(self):
        s = "{)"
        self.assertFalse(self.solution.is_valid(s))

    def test_invalid_close(self):
        s = "}(("
        self.assertFalse(self.solution.is_valid(s))

    def test_missing_open(self):
        s = "([]"
        self.assertFalse(self.solution.is_valid(s))
