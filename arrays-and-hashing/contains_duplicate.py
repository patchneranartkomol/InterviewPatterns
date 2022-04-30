from unittest import main, TestCase
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(nums) > len(set(nums)) else False


class TestSolution(TestCase):
    solution = Solution()

    def test_array_of_len_1(self):
        array = [1]
        self.assertFalse(self.solution.containsDuplicate(array))

    def test_contains_duplicate(self):
        array_with_duplicates = [1,2,3,1]
        self.assertTrue(self.solution.containsDuplicate(array_with_duplicates))

    def test_does_not_contain_duplicate(self):
        array_without_duplicates = [1,2,3,4]
        self.assertFalse(self.solution.containsDuplicate(array_without_duplicates))

    def test_longer_array_with_duplicates(self):
        longer_array_with_duplicates = [1,1,1,3,3,4,3,2,4,2]
        self.assertTrue(self.solution.containsDuplicate(longer_array_with_duplicates))


if __name__ == '__main__':
    main()
