lst = list(map(int, input().split()))

even = [x for x in lst if x % 2 == 0]
odd = [x for x in lst if x % 2 != 0]

print("Even =", even)
print("Odd =", odd)

Input

1 2 3 4 5 6

#Output

Even = [2, 4, 6]
Odd = [1, 3, 5]