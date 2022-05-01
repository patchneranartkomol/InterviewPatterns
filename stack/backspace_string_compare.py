from unittest import main, TestCase
from typing import List


class Solution:
    """
    https://leetcode.com/problems/backspace-string-compare/

    Evaluate each input string by appending chars to a stack, and popping if deletion is valid.

    Compare elements of both stacks.

    Time Complexity: O(N)
    Space Complexity: O(N)
    N - size of input strings

    TODO - followup - Find an O(N) time, O(1) space solution
    """

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.evaluateBackspaceString(s) == self.evaluateBackspaceString(t)

    def evaluateBackspaceString(self, s: str) -> List[str]:
        stack = []
        for char in s:
            if char == '#':
                if stack:
                    stack.pop()
                continue
            stack.append(char)
        return stack


class TestSolution(TestCase):
    solution = Solution()

    def test_same_input(self):
        s = "ab#c"
        t = "ad#c"
        self.assertTrue(self.solution.backspaceCompare(s,t))

    def test_same_input_empty_final_string(self):
        s = "ab##"
        t = "y#x#"
        self.assertTrue(self.solution.backspaceCompare(s,t))

    def test_different_input(self):
        s = "a#c"
        t = "g"
        self.assertFalse(self.solution.backspaceCompare(s,t))


if __name__ == '__main__':
    main()
