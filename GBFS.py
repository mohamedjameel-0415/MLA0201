import heapq

def gbfs(graph, start, goal, h):

    queue = [(h[start], start, [start])]
    visited = set()

    while queue:

        heuristic, node, path = heapq.heappop(queue)

        if node == goal:
            return path

        if node in visited:
            continue

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(queue, (h[neighbor], neighbor, path + [neighbor]))

    return None


# Example Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Heuristic values (distance to goal F)
h = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 1,
    'F': 0
}

start = 'A'
goal = 'D'

result = gbfs(graph, start, goal, h)

print("Path:", result)