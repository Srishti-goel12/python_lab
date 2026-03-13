Fibonacci Series (while loop)
n = int(input())
a, b = 0, 1
i = 0
while i < n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1
🔹 Input
5
🔹 Output
0 1 1 2 3