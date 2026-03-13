t = tuple(map(int, input().split()))

if len(t) == len(set(t)):
    print("All elements are unique")
else:
    print("Elements are not unique")

Input

1 2 3 4

#Output

All elements are unique