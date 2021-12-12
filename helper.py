def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

dfs(graph, '0')


def neighbours(grid, r, c):
    vals = sum(
        (
            row[c - (c > 0): c + 2]
            for row in grid[r - (r > 0) : r + 2]
        ), []
    )

    vals.remove(grid[r][c])

    return vals       


matrix = [[1, 5, 4, 9], 
        [2, 8, 3, 8], 
        [6, 3, 6, 3], 
        [7, 4, 7, 1]]

print(f'{neighbours(matrix, 2, 2)}')