"""
Floyd-Warshall algorithm

time complexity: O(n^3)
memory complexity: O(n^2)

Description:
Find minimum path between each pair of vertices. 
"""
from typing import List


inf = float('inf')


def floyd_warshall(adjacency_matrix: List[List[float]]):
    """
    @param adjacency_matrix: adjacency matrix
    """
    n_v: int = len(adjacency_matrix)
    distance = [row[:] for row in adjacency_matrix]

    for k in range(n_v):
        for i in range(n_v):
            for j in range(n_v):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance


if __name__ == '__main__':
    graph = [
        [0, 2, 2, inf, inf, inf],
        [inf, 0, 2, inf, inf, inf],
        [inf, inf, 0, 2, 2, 6],
        [inf, inf, inf, 0, inf, 2],
        [inf, inf, inf, inf, 0, 2],
        [inf, inf, inf, inf, inf, 0]
    ]

    result = floyd_warshall(graph)

    for row in result:
        print(row)
