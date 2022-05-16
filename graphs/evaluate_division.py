from unittest import TestCase

from collections import defaultdict
from typing import Dict, List, Set


class Solution:
    """
    https://leetcode.com/problems/evaluate-division/

    Each equation given to us represents an edge in an undirected, weighted graph.
    Each query asks us to find if there is a path between two vertices, and calculate its weight if present.

    We iterate through equations and values to construct the graph.

    For each query, we use depth-first search to find a path and calculate its value, or confirm there is no path.

    Time Complexity - O(Q* N)
    Space Complexity - O(N)

    N - length of equations
    Q - length of queries
    """

    def calc_equation(self, equations: List[List[str]], values: List[float],
                      queries: List[List[str]]) -> List[float]:
        graph = self.build_graph(equations, values)
        return [self.dfs(s, e, set(), graph, 1.0) for s, e in queries]

    def build_graph(self, equations: List[List[str]],
                    values: List[float]) -> Dict[str, float]:
        graph = defaultdict(list)
        for edge, value in zip(equations, values):
            source, dest = edge
            graph[source].append((dest, value))
            graph[dest].append((source, 1 / value))
        return graph

    def dfs(self, start: str, end: str, seen: Set[str],
            graph: Dict[str, float], value: float) -> float:
        if start not in graph or end not in graph or start in seen:
            return -1
        if start == end:
            return value
        seen.add(start)
        for vertex, weight in graph[start]:
            product = self.dfs(vertex, end, seen, graph, weight * value)
            if product != -1:
                return product
        return -1


class TestSolution(TestCase):
    solution = Solution()

    def test_input_1(self):
        equations = [["a", "b"], ["b", "c"]]
        values = [2.0, 3.0]
        queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        self.assertEqual([6.0, 0.5, -1.0, 1.0, -1.0],
                         self.solution.calc_equation(equations, values,
                                                     queries))

    def test_input_2(self):
        equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
        values = [1.5, 2.5, 5.0]
        queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
        self.assertEqual([3.75000, 0.40000, 5.00000, 0.20000],
                         self.solution.calc_equation(equations, values,
                                                     queries))

    def test_input_3(self):
        equations = [["a", "b"]]
        values = [0.5]
        queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
        self.assertEqual([0.50000, 2.00000, -1.00000, -1.00000],
                         self.solution.calc_equation(equations, values,
                                                     queries))

    def test_input_4(self):
        equations = [["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]]
        values = [3.0, 4.0, 5.0, 6.0]
        queries = [["x1", "x5"], ["x5", "x2"], ["x2", "x4"], ["x2", "x2"],
                   ["x2", "x9"], ["x9", "x9"]]
        self.assertEqual([360.0, 0.008333333333333333, 20.0, 1.0, -1, -1],
                         self.solution.calc_equation(equations, values,
                                                     queries))
