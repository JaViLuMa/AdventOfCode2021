from collections import deque


def part1(graph, node, end, visited):
    
    if node == end:
        return 1;

    visited = visited if node.isupper() else visited | {node}

    paths = 0
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            paths += part1(graph, neighbor, end, visited)

    return paths


def part2(graph, node, end, visited, twice) -> int: 
    if node == end:
        return 1;

    visited = visited if node.isupper() else visited | {node}

    paths = 0
    
    for neighbor in graph[node]:
        if neighbor.isupper():
            paths += part2(graph, neighbor, end, visited, twice)
        elif neighbor not in visited:
            paths += part2(graph, neighbor, end, visited, twice)
        elif twice and neighbor != 'start':
            paths += part2(graph, neighbor, end, visited, False)
    
    return paths

        
def main():
    graph = {}

    with open('L - inputs.txt') as f:
        for line in f:
            pointA, pointB = line.strip().split('-')

            if pointA in graph:
                graph[pointA].append(pointB)
            else:
                graph[pointA] = [pointB]

            if pointB in graph:
                graph[pointB].append(pointA)
            else:
                graph[pointB] = [pointA]


    print(f'PART 1 - {part1(graph, "start", "end", visited={"start"})}')
    print(f'PART 2 - {part2(graph, "start", "end", visited={"start"}, twice=True)}')

if __name__ == "__main__":
    main()
