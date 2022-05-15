from collections import deque
from unittest import TestCase
from typing import Optional

from .treenode import TreeNode


class Solution:
    """
    https://leetcode.com/problems/deepest-leaves-sum/

    Use breadth-first search to traverse the tree level by level. while calculating each level sum.
    When we complete a traversal of a single level, we can verify that
    all the nodes on a level were leaf nodes, if no nodes had been added to the queue.

    In that case, we return the result.

    Time Complexity: O(N)
    Space Complexity: O(w)
    N - Nodes in the input tree
    w - Width of tree, or the maximum number of nodes on a given level
    For a perfectly balanced tree, the upper bound is O(N)
    In the degenerate case, with a completely unbalanced tree, this is O(1)
    """

    def deepest_leaves_sum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        if root:
            queue.append(root)
        while queue:
            level_sum = 0
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not queue:
                return level_sum
        return 0


class TestSolution(TestCase):
    solution = Solution()

    def test_tree_depth_of_3(self):
        """
        [4,2,7,1,3,6,9]
               4
              /  \
            2     7
          /  \   / \
         1    3 6   9
        """
        tree = TreeNode(4)
        tree.left = TreeNode(2)
        tree.right = TreeNode(7)
        tree.left.left = TreeNode(1)
        tree.left.right = TreeNode(3)
        tree.right.left = TreeNode(6)
        tree.right.right = TreeNode(9)
        res = self.solution.deepest_leaves_sum(tree)
        self.assertEqual(19, res)

    def test_incomplete_tree_depth_of_3(self):
        """
        [4,2,7,1,3,None,9]
               4
              /  \
            2     7
          /  \     \
         1    3     9
        """
        tree = TreeNode(4)
        tree.left = TreeNode(2)
        tree.right = TreeNode(7)
        tree.left.left = TreeNode(1)
        tree.left.right = TreeNode(3)
        tree.right.right = TreeNode(9)
        res = self.solution.deepest_leaves_sum(tree)
        self.assertEqual(13, res)

    def test_tree_depth_of_1(self):
        tree = TreeNode(20)
        res = self.solution.deepest_leaves_sum(tree)
        self.assertEqual(20, res)

    def test_empty_tree(self):
        tree = None
        res = self.solution.deepest_leaves_sum(tree)
        self.assertEqual(0, res)
