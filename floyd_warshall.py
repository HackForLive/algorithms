"""
Floyd-Warshall algorithm

time complexity: O(n^3)
memory complexity: O(n^2)

Description:
Find minimum path between each pair of vertices. 
"""
from typing import List


inf = float('inf')


def get_initial_next_matrix(adjacency_matrix: List[List[float]]):
    """
    @param adjacency_matrix: adjacency matrix

    return initial next matrix
    """
    n_v = len(adjacency_matrix)
    next_matrix = [[-1 for i in range(n_v)] for i in range(n_v)]

    for i in range(n_v):
        for j in range(n_v):
            # There is an edge between node
            # i and j
            if graph[i][j] != inf:
                next_matrix[i][j] = j
    return next_matrix


def construct_path(u: int, v: int, next_matrix: List[List[float]]):
    """
    Function construct the shortest
    path between u and v

    @param u: from node
    @param v: to node
    """
    # If there's no path between
    # node u and v, simply return
    # an empty array
    if next_matrix[u][v] == -1:
        return {}

    # Storing the path in a vector
    path = [u]
    while u != v:
        u = next_matrix[u][v]
        path.append(u)

    return path


def print_path(path):
    """
    Print the shortest path
    @param path: path
    """
    n = len(path)
    for i in range(n - 1):
        print(path[i], end=" -> ")
    print (path[n - 1])


def floyd_warshall(adjacency_matrix: List[List[float]], next_matrix: List[List[float]]):
    """
    Standard Floyd Warshall Algorithm with little modification.
    Now if we find that dis[i][j] > dis[i][k] + dis[k][j] then 
    we modify next[i][j] = next[i][k]
    
    @param adjacency_matrix: adjacency matrix
    @param next_matrix: initial next matrix
    """
    n_v: int = len(adjacency_matrix)
    distance = [row[:] for row in adjacency_matrix]

    for k in range(n_v):
        for i in range(n_v):
            for j in range(n_v):
                 # We cannot travel through
                # edge that doesn't exist
                if inf in (distance[i][k], distance[k][j]):
                    continue
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
                    next_matrix[i][j] = next_matrix[i][k]

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

    initial_next_matrix = get_initial_next_matrix(adjacency_matrix=graph)
    result = floyd_warshall(adjacency_matrix=graph, next_matrix=initial_next_matrix)

    print_path(path=construct_path(u=0, v=3, next_matrix=initial_next_matrix))
    print(f"{result[0][3]=}")

    for row in result:
        print(row)
