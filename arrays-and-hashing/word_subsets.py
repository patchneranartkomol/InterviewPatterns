from collections import Counter
from typing import List
from unittest import TestCase


class Solution:
    """
    https://leetcode.com/problems/word-subsets/

    Find the maximum # of occurences in a single word of all chars in words2.

    Compare each word in words1 against that max count.

    If the word is a subset, append it the result.

    Time Complexity: O(N * M)
    Space Complexity: O(N * M)
    N - length of words1
    M - length of words2

    Given the constraint that 1 <= words1[i].length, words2[i].length <= 10,
    we can assume that each counter / multi-set uses constant time and memory
    to create.
    """

    def word_subsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        w2_max_counts = self.get_max_counts(words2)
        for w in words1:
            if self.is_subset(w, w2_max_counts):
                res.append(w)
        return res

    def get_max_counts(self, words: List[str]) -> Counter[str]:
        max_counts = Counter()
        for w in words:
            counts = Counter(w)
            for key in counts:
                max_counts[key] = max(max_counts.get(key, 0), counts[key])
        return max_counts

    def is_subset(self, word: str, word_counter_2: Counter[str]) -> bool:
        return len(word_counter_2 - Counter(word)) == 0


class TestSolution(TestCase):
    solution = Solution()

    def test_input_1(self):
        words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
        words2 = ["e", "o"]
        self.assertEqual(self.solution.word_subsets(words1, words2),
                         ["facebook", "google", "leetcode"])

    def test_input_2(self):
        words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
        words2 = ["l", "e"]
        self.assertEqual(self.solution.word_subsets(words1, words2),
                         ["apple", "google", "leetcode"])
