from unittest import TestCase
from typing import Optional

from .treenode import TreeNode


class Solution:
    """
    https://leetcode.com/problems/binary-tree-pruning/

    Recursive postorder depth-first search. Note that any recursive solution can
    also be implemented iteratively.

    Visit each node. At each leaf, check if it is a leaf and should be deleted.

    Time Complexity: O(N)
    Space Complexity: O(h)
    N - Nodes in the input tree
    h - Height of tree. This can be at best O(log(N)) for a balanced tree
    or O(N) the degenerate case, a linked list, or completely imbalanced tree
    """

    def prune_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        if root.left:
            root.left = self.prune_tree(root.left)
        if root.right:
            root.right = self.prune_tree(root.right)

        if not root.left and not root.right and root.val == 0:
            return None
        return root


class TestSolution(TestCase):
    solution = Solution()

    def test_tree(self):
        tree = TreeNode(1)
        tree.left = TreeNode(0)
        tree.right = TreeNode(0)

        self.solution.prune_tree(tree)

        self.assertEqual(1, tree.val)
        self.assertIsNone(tree.left)
        self.assertIsNone(tree.right)

    def test_tree_with_empty_children(self):
        tree = TreeNode(1)
        tree.left = None
        tree.right = None

        self.solution.prune_tree(tree)

        self.assertEqual(1, tree.val)
        self.assertIsNone(tree.left)
        self.assertIsNone(tree.right)

    def test_empty_tree(self):
        tree = None

        self.solution.prune_tree(tree)

        self.assertIsNone(tree)
