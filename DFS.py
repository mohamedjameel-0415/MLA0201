def dfs(graph, start, goal):

    stack = [[start]]
    visited = set()

    while stack:

        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph[node]:
                new_path = path + [neighbor]
                stack.append(new_path)

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

start = 'A'
goal = 'F'

result = dfs(graph, start, goal)

print("Path:", result)