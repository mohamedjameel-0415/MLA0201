import heapq

def a_star(graph, start, goal, h):

    open_list = [(0 + h[start], 0, start, [start])]
    visited = set()

    while open_list:

        f, g, node, path = heapq.heappop(open_list)

        if node == goal:
            return path, g

        if node in visited:
            continue

        visited.add(node)

        for neighbor, cost in graph[node]:
            new_g = g + cost
            new_f = new_g + h[neighbor]
            new_path = path + [neighbor]

            heapq.heappush(open_list, (new_f, new_g, neighbor, new_path))

    return None


# Graph with weights
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [('F', 3)],
    'E': [('F', 1)],
    'F': []
}

# Heuristic values
h = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 0
}

start = 'A'
goal = 'F'

result = a_star(graph, start, goal, h)

print("Path:", result[0])
print("Cost:", result[1])