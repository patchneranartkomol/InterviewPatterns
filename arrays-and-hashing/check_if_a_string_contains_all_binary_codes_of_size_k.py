from unittest import TestCase


class Solution:
    """
    https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

    Calculate 2^k, the total number of possible binary codes of size k.

    For each substring of length k in s, add that substring to a hash set.
    If the total number of elements in the set == total possible binary codes,
    then s contains all binary codes.

    Time Complexity: O(log(k) + s - k)
    Space Complexity: O(k * S^k)
    N - size of input list
    """

    def has_all_codes(self, s: str, k: int) -> bool:
        permutation_count = 2**k
        if len(s) < permutation_count:
            return False

        binary_codes = set()
        # Check every substring of length k
        for i in range(len(s) - k + 1):
            binary_codes.add(s[i:i + k])

        return len(binary_codes) == permutation_count


class TestSolution(TestCase):
    solution = Solution()

    def test_string_contains_k_of_2(self):
        s = "00110110"
        k = 2
        self.assertTrue(self.solution.has_all_codes(s, k))

    def test_string_contains_k_of_1(self):
        s = "00110110"
        k = 1
        self.assertTrue(self.solution.has_all_codes(s, k))

    def test_string_does_not_contain_k_of_2(self):
        s = "011011"
        k = 2
        self.assertFalse(self.solution.has_all_codes(s, k))

    def test_string_too_short(self):
        s = "010"
        k = 5
        self.assertFalse(self.solution.has_all_codes(s, k))
