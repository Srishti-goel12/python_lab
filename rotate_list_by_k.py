lst = list(map(int, input().split()))
k = int(input())

k = k % len(lst)
rotated = lst[k:] + lst[:k]

print("Rotated List =", rotated)

Input

1 2 3 4 5
2

#Output

Rotated List = [3, 4, 5, 1, 2]