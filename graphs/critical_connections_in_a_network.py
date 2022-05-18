from unittest import TestCase

from collections import defaultdict
from typing import List


class Solution:
    """
    https://leetcode.com/problems/critical-connections-in-a-network/

    This video was immensely helpful in explaining the algorithm: https://www.youtube.com/watch?v=aZXi1unBdJA

    Tarjan's Bridge Finding Algorithm - (depth-first-search + union find)

    1 depth-first search pass over the graph, marking the discovery time and lowest link
    number.

    Once we find a strongly connected component, a bridge, or critical connection, is
    any edge where the current node is found earlier than the lowest link of that component.

    Time Complexity - O(V + E) - Linear as we DFS through each vertex, and check each edge.
    Space Complexity - O(V) - disc_time, low, and visited are O(V). Result array bridges
    may grow O(E) in the worst case, where every edge is critical.

    E - Number of connections in the graph
    V - Number of nodes (referred to as vertices) in the graph
    """

    def critical_connections(self, n: int,
                             connections: List[List[int]]) -> List[List[int]]:
        # Convert connections into an adjacency list
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        disc_time, low = [0] * n, [0] * n
        visited = set()
        self.time = 0
        bridges = []

        def dfs(curr: int, prev: int):
            disc_time[curr] = low[curr] = self.time
            self.time += 1
            visited.add(curr)

            for next_node in graph[curr]:
                if next_node not in visited:
                    dfs(next_node, curr)
                    low[curr] = min(low[curr], low[next_node])
                elif next_node != prev:
                    low[curr] = min(low[curr], disc_time[next_node])

                if disc_time[curr] < low[next_node]:
                    bridges.append([curr, next_node])

        dfs(0, -1)
        return bridges


class TestSolution(TestCase):
    solution = Solution()

    def test_input_1(self):
        n = 5
        connections = [[0, 1], [1, 2], [2, 0], [1, 3]]
        self.assertEqual([[1, 3]],
                         self.solution.critical_connections(n, connections))

    def test_input_2(self):
        n = 2
        connections = [[0, 1]]
        self.assertEqual([[0, 1]],
                         self.solution.critical_connections(n, connections))
