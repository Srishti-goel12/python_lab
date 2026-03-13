lst = list(map(int, input().split()))
unique = list(set(lst))
print("After removing duplicates =", unique)

Input

1 2 2 3 4 4 5

#Output

After removing duplicates = [1, 2, 3, 4, 5]