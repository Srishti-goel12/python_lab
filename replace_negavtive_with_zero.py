lst = list(map(int, input().split()))
new_lst = [x if x >= 0 else 0 for x in lst]

print("Updated List =", new_lst)

Input

5 -2 3 -1 7

#Output

Updated List = [5, 0, 3, 0, 7]