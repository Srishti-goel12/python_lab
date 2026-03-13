lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

merged = list(set(lst1 + lst2))
print("Merged List =", merged)

Input

1 2 3
3 4 5

#Output

Merged List = [1, 2, 3, 4, 5]