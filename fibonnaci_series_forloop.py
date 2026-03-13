n = int(input())
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

Input

5

#Output

0 1 1 2 3