from unittest import TestCase
from typing import Optional

from .treenode import TreeNode


class Solution:
    """
    https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/

    The 2 given trees are guaranteed to be identical clones except for one identical reference.

    We can use any method to traverse the nodes in the same position in both trees. At each node
    we visit, we check if the reference is the same. In Python, this is done with the "is" keyword.

    Using a recursive preorder depth-first search in this implementation.

    Time Complexity - O(N)
    Space Complexity - O(h), where h is the height of the tree.
    It can be O(log N) for a balanced tree, or O(N) for the degenerate case.
    """

    def get_target_copy(self, original: TreeNode, cloned: TreeNode,
                        target: TreeNode) -> Optional[TreeNode]:
        if not original:
            return None
        if cloned is target:
            return cloned
        return self.get_target_copy(original.left, cloned.left,
                                    target) or self.get_target_copy(
                                        original.right, cloned.right, target)


class TestSolution(TestCase):
    solution = Solution()

    def test_tree_depth_of_1(self):
        tree = TreeNode(20)
        self.assertIs(tree, self.solution.get_target_copy(tree, tree, tree))

    def test_tree_depth_of_3(self):
        """
        [4,2,7,1,3,6,9]
               4
              /  \
            2     7
          /  \   / \
         1    3 6   9

        Repeated reference is 7
        """
        target = TreeNode(7)
        tree = TreeNode(4)
        tree.left = TreeNode(2)
        tree.right = target
        tree.left.left = TreeNode(1)
        tree.left.right = TreeNode(3)
        tree.right.left = TreeNode(6)
        tree.right.right = TreeNode(9)

        # Cloned tree
        cloned = TreeNode(4)
        cloned.left = TreeNode(2)
        cloned.right = target
        cloned.left.left = TreeNode(1)
        cloned.left.right = TreeNode(3)
        cloned.right.left = TreeNode(6)
        cloned.right.right = TreeNode(9)

        self.assertIs(target,
                      self.solution.get_target_copy(tree, cloned, target))
