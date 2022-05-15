from unittest import TestCase
from typing import Optional

from .treenode import TreeNode


class Solution:
    """
    https://leetcode.com/problems/invert-binary-tree/

    Recursive postorder depth-first search.

    Base cases - Node is empty - do nothing
                 Node has no children - return node
    Recursive case - Swap pointers of left and right subtrees.

    For each node, starting with the root, we assign the left subtree to the right inverted subtree,
    and recursively call invertTree to invert that right subtree. We continue that process,
    until the right subtree's left child is a leaf node. Once it returns, we recursively do the
    same for that node's right pointer, assigning it to the left inverted subtree.

    Time Complexity: O(N)
    Space Complexity: O(h)
    N - Nodes in the input tree
    h - Height of tree. This can be at best O(log(N)) for a balanced tree
    or O(N) the degenerate case, a linked list, or completely imbalanced tree
    """

    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        root.left, root.right = self.invert_tree(root.right), self.invert_tree(
            root.left)
        return root


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

               |
               |

               4
              /  \
            7     2
          /  \   / \
         9    6 3   1

        """
        tree = TreeNode(4)
        tree.left = TreeNode(2)
        tree.right = TreeNode(7)
        tree.left.left = TreeNode(1)
        tree.left.right = TreeNode(3)
        tree.right.left = TreeNode(6)
        tree.right.right = TreeNode(9)
        self.solution.invert_tree(tree)
        self.assertEqual(4, tree.val)
        self.assertEqual(7, tree.left.val)
        self.assertEqual(2, tree.right.val)
        self.assertEqual(9, tree.left.left.val)
        self.assertEqual(6, tree.left.right.val)
        self.assertEqual(3, tree.right.left.val)
        self.assertEqual(1, tree.right.right.val)

    def test_tree_depth_of_2(self):
        tree = TreeNode(2)
        tree.left = TreeNode(1)
        tree.right = TreeNode(3)
        self.solution.invert_tree(tree)
        self.assertEqual(2, tree.val)
        self.assertEqual(3, tree.left.val)
        self.assertEqual(1, tree.right.val)

    def test_tree_depth_of_1(self):
        tree = TreeNode(0)
        self.solution.invert_tree(tree)
        self.assertEqual(0, tree.val)

    def test_empty_tree(self):
        tree = None
        self.solution.invert_tree(tree)
        self.assertIsNone(tree)
