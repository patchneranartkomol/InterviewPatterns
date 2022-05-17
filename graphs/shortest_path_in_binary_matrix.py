from unittest import TestCase

from collections import deque
from typing import List, Set, Tuple


class Solution:
    """
    https://leetcode.com/problems/shortest-path-in-binary-matrix/

    Breadth-first search on a graph is more efficient for finding the shortest path
    as we are asked to here.

    Initialize a queue to hold visited nodes, and length of the visited path.
    For each node in the queue, check its valid 8-directional neighbors.

    If we reach (n - 1, n - 1), return the length of the path.

    If the queue is empty and we have not reached (n - 1, n - 1), there is
    no valid path through the matrix.

    Time Complexity - O(N)
    Space Complexity - O(N) - may be able to space optimize slightly, by modifying the
    input matrix, instead of creating a new visited set. But, it would still be O(N).

    N - Number of cells in n x n matrix.
    """

    DIRECTIONS = {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0),
                  (1, 1)}

    def shortest_path_binary_matrix(self, grid: List[List[int]]) -> int:
        n = len(grid) - 1
        if grid[0][0] or grid[-1][-1]:
            return -1

        visited = set()
        queue = deque([(0, 0, 1)])  # Store (i, j, path_len)
        visited.add((0, 0))
        while queue:
            i, j, path_len = queue.popleft()
            if i == n and j == n:
                return path_len
            self.find_neighbors(queue, i, j, n, path_len, visited, grid)

        return -1

    def find_neighbors(self, queue: deque[Tuple[int, int, int]], i: int,
                       j: int, n: int, path_len: int,
                       visited: Set[Tuple[int, int]], grid: List[List[int]]):
        for x_dir, y_dir in self.DIRECTIONS:
            x, y = i + x_dir, j + y_dir
            if (0 <= x <= n and 0 <= y <= n and (x, y) not in visited
                    and grid[x][y] == 0):
                visited.add((x, y))
                queue.append((x, y, path_len + 1))


class TestSolution(TestCase):
    solution = Solution()

    def test_input_2_by_2(self):
        binary_matrix = [[0, 1], [1, 0]]
        self.assertEqual(
            2, self.solution.shortest_path_binary_matrix(binary_matrix))

    def test_input_1_by_1_valid(self):
        binary_matrix = [[0]]
        self.assertEqual(
            1, self.solution.shortest_path_binary_matrix(binary_matrix))

    def test_input_1_by_1_invalid(self):
        binary_matrix = [[1]]
        self.assertEqual(
            -1, self.solution.shortest_path_binary_matrix(binary_matrix))

    def test_input_3_by_3_valid(self):
        binary_matrix = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
        self.assertEqual(
            4, self.solution.shortest_path_binary_matrix(binary_matrix))

    def test_input_3_by_3_invalid(self):
        binary_matrix = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
        self.assertEqual(
            -1, self.solution.shortest_path_binary_matrix(binary_matrix))

    def test_input_3_by_3_invalid_no_path(self):
        binary_matrix = [[0, 1, 1], [1, 1, 0], [1, 1, 0]]
        self.assertEqual(
            -1, self.solution.shortest_path_binary_matrix(binary_matrix))
