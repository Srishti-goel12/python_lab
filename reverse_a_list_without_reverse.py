lst = list(map(int, input().split()))
rev = []

for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])

print("Reversed List =", rev)

Input

1 2 3 4

#Output

Reversed List = [4, 3, 2, 1]