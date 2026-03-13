lst = list(map(int, input().split()))

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print("Sorted List =", lst)

Input

5 3 8 1

#Output

Sorted List = [1, 3, 5, 8]