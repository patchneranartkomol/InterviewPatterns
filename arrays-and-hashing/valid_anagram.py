from collections import Counter
from unittest import main, TestCase


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = Counter(s)
        t_chars = Counter(t)
        if s_chars == t_chars:
            return True
        return False


class TestSolution(TestCase):
    solution = Solution()

    def test_anagram(self):
        s = "anagram"
        t = "nagaram"
        self.assertTrue(self.solution.isAnagram(s, t))

    def test_not_anagram(self):
        s = "rat"
        t = "car"
        self.assertFalse(self.solution.isAnagram(s, t))


if __name__ == '__main__':
    main()
