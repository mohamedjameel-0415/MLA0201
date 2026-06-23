def hill_climb(values, start):

    current = start

    while True:

        neighbors = []

        if current - 1 >= 0:
            neighbors.append(current - 1)

        if current + 1 < len(values):
            neighbors.append(current + 1)

        best = current

        for n in neighbors:
            if values[n] > values[best]:
                best = n

        if best == current:
            return current, values[current]

        current = best


# Example function values
values = [1, 3, 7, 12, 9, 10, 5]

start = 0

result = hill_climb(values, start)

print("Best State Index:", result[0])
print("Best Value:", result[1])