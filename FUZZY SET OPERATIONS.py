A = {'x1': 0.2, 'x2': 0.5, 'x3': 0.8}
B = {'x1': 0.6, 'x2': 0.3, 'x3': 0.9}

union = {}
intersection = {}
complement_A = {}

for x in A:
    union[x] = max(A[x], B[x])
    intersection[x] = min(A[x], B[x])
    complement_A[x] = 1 - A[x]

print("Union:", union)
print("Intersection:", intersection)
print("Complement of A:", complement_A)