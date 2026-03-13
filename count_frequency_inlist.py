lst = list(map(int, input().split()))

for item in set(lst):
    print(item, ":", lst.count(item))

Input

1 2 2 3 3 3

#Output

1 : 1
2 : 2
3 : 3