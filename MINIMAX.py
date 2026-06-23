def minimax(depth, nodeIndex, isMax, values, height):

    if depth == height:
        return values[nodeIndex]

    if isMax:
        return max(
            minimax(depth + 1, nodeIndex * 2, False, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, False, values, height)
        )
    else:
        return min(
            minimax(depth + 1, nodeIndex * 2, True, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, True, values, height)
        )

# Terminal node values
values = [3, 5, 2, 9, 12, 5, 23, 23]

height = 3

result = minimax(0, 0, True, values, height)

print("Optimal Value:", result)