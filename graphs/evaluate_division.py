from unittest import main, TestCase

from collections import defaultdict
from typing import Dict, List, Set

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = self.buildGraph(equations, values)
        return [self.dfs(s, e, set(), graph, 1.0) for s, e in queries]

    def buildGraph(self, equations: List[List[str]], values: List[float]) -> Dict[str, float]:
        graph = defaultdict(list)
        for edge, value in zip(equations, values):
            source, dest = edge
            graph[source].append((dest, value))
            graph[dest].append((source, 1 / value))
        return graph

    def dfs(self, start: str, end: str, seen: Set[str], graph: Dict[str, float], value: float) -> float:
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
        equations = [["a","b"],["b","c"]]
        values = [2.0,3.0]
        queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
        self.assertEqual([6.0, 0.5, -1.0, 1.0, -1.0], self.solution.calcEquation(equations, values, queries))

    def test_input_2(self):
        equations = [["a","b"],["b","c"],["bc","cd"]]
        values =  [1.5, 2.5, 5.0]
        queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
        self.assertEqual([3.75000, 0.40000, 5.00000, 0.20000], self.solution.calcEquation(equations, values, queries))



if __name__ == '__main__':
    main()
