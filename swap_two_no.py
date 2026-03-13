# Read input
a = int(input())
b = int(input())

# Swap without third variable
a = a + b
b = a - b
a = a - b

# Output
print("After swapping:")
print("a =", a)
print("b =", b)