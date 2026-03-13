def unique_list(lst):
    return list(set(lst))

lst = list(map(int, input().split()))
print("Unique =", unique_list(lst))

Input

1 2 2 3 4 4 5

#Output

Unique = [1, 2, 3, 4, 5]