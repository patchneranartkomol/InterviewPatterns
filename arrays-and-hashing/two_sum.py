from unittest import main, TestCase
from typing import List

class Solution:
    """
    https://leetcode.com/problems/two-sum/

    Iterate through the nums array, storing values seen, and the last occurence in
    a hash table.

    Look for (target - num[i]) as a key in the hash table while visiting another element.

    For example 3, the hash table contains these values after 3 iterations of the for loop:
    {
        '2': 0,
        '7': 1,
        '11' 2
    }

    On the final iteration, we find '(22 - 15)' in the hash table. '7' had occured at index, 1.
    This gives us the resulting pair of indices, [1, 3].

    Time Complexity: O(N)
    Space Complexity: O(N)
    N - size of input list - nums
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            goal = target - num
            if goal in nums_dict:
                return [nums_dict[goal], i]
            nums_dict[num] = i


class TestSolution(TestCase):
    solution = Solution()

    def testInput1(self):
        input_arr = [2,7,11,15]
        target = 9
        self.assertEquals(self.solution.twoSum(input_arr, target), [0, 1])

    def testInput2(self):
        input_arr = [3,2,4]
        target = 6
        self.assertEquals(self.solution.twoSum(input_arr, target), [1, 2])

    def testInput3(self):
        input_arr = [2,7,11,15]
        target = 22
        self.assertEquals(self.solution.twoSum(input_arr, target), [1, 3])

    def testInputWithDuplicate(self):
        input_arr = [3,2,3]
        target = 6
        self.assertEquals(sorted(self.solution.twoSum(input_arr, target)), [0, 2])


if __name__ == '__main__':
    main()
