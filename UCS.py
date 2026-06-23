import heapq

def ucs(graph, start, goal):

    queue = [(0, start, [start])]  # (cost, node, path)
    visited = set()

    while queue:

        cost, node, path = heapq.heappop(queue)

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)

            for neighbor, weight in graph[node]:
                new_cost = cost + weight
                new_path = path + [neighbor]
                heapq.heappush(queue, (new_cost, neighbor, new_path))

    return None


# Example Graph (weighted)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 1)],
    'D': [('F', 3)],
    'E': [('F', 1)],
    'F': []
}

start = 'A'
goal = 'F'

result = ucs(graph, start, goal)

print("Path:", result[0])
print("Cost:", result[1])