from collections import deque

def is_valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    if m > 0 and m < c:
        return False

    if (3 - m) > 0 and (3 - m) < (3 - c):
        return False

    return True

def bfs():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        m, c, boat = state

        moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]

        for dm, dc in moves:

            if boat == 1:
                new = (m-dm, c-dc, 0)
            else:
                new = (m+dm, c+dc, 1)

            if is_valid(new[0], new[1]):
                queue.append((new, path + [new]))

    return None

solution = bfs()

for state in solution:
    print(state)