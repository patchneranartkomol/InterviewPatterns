from unittest import TestCase


class Solution:

    def count_substrings(self, s: str) -> int:
        """
        https://leetcode.com/problems/palindromic-substrings/

        Brute Force solution:
        Recursively check if the string is a palindrome.
        Starting a index i, and expanding to end of string.

        Base Cases -
        1) Out of bounds, 0 palindromes
        2) String of len 1 is a palindrome

        Recursive case -
        If s is a palindrome:
            add 1 palindrome, and check s[start:end + 1]
        Else:
            check s[start: end + 1]

        For a string "abc" - the outer loop runs 3 times to traverse:
        "a"
        "ab"
        "abc"

        "b"
        "bc"

        "c"

        Adding memoization to count_palindromes wouldn't really improve our runtime,
        as we're not doing any duplicated work.

        Time Complexity - O(N ^ 3)
        Space Complexity - O(N ^ 2) - call stack grows on the order of N and
        O(N) worst case string slice + comparison operation per function call
        """
        count = 0

        def count_palindromes(start: int, end: int) -> int:
            if (start > end or end == len(s)):
                return 0

            if (s[start:end + 1] == s[start:end + 1][::-1]):
                return count_palindromes(start, end + 1) + 1
            return count_palindromes(start, end + 1)

        for i in range(len(s)):
            count += count_palindromes(i, i)
        return count


class Solution2:

    def count_substrings(self, s: str) -> int:
        """
        https://leetcode.com/problems/palindromic-substrings/

        For each index in the string, check for palindromes
        that begin at that character.

        We use 2 pointers, twice, at each index, to check
        for odd length palindromes and even length palindromes.

        Time Complexity - O(N ^ 2)
        Space Complexity - O(1)
        """
        count = 0

        for i in range(len(s)):
            count += self.count_palindromes(s, i, i)
            count += self.count_palindromes(s, i, i + 1)

        return count

    def count_palindromes(self, s: str, left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count


class TestSolution(TestCase):
    solution = Solution()
    solution2 = Solution2()

    def test_string_of_len_1(self):
        self.assertEqual(1, self.solution.count_substrings("a"))
        self.assertEqual(1, self.solution2.count_substrings("a"))

    def test_no_duplicate_string(self):
        self.assertEqual(3, self.solution.count_substrings("abc"))
        self.assertEqual(3, self.solution2.count_substrings("abc"))

    def test_input_aaa(self):
        self.assertEqual(6, self.solution.count_substrings("aaa"))
        self.assertEqual(6, self.solution2.count_substrings("aaa"))

    def test_input_aaab(self):
        self.assertEqual(7, self.solution.count_substrings("aaab"))
        self.assertEqual(7, self.solution2.count_substrings("aaab"))
