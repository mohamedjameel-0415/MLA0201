# Regions and their neighbors
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']

def is_safe(region, color, assignment):
    for neighbor in graph[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def map_coloring(assignment):

    if len(assignment) == len(graph):
        return True

    region = [r for r in graph if r not in assignment][0]

    for color in colors:
        if is_safe(region, color, assignment):

            assignment[region] = color

            if map_coloring(assignment):
                return True

            del assignment[region]

    return False

assignment = {}

if map_coloring(assignment):
    print("Solution:")
    for region, color in assignment.items():
        print(region, "->", color)
else:
    print("No solution exists")