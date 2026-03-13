lst = list(map(int, input().split()))

if lst == lst[::-1]:
    print("Palindrome List")
else:
    print("Not Palindrome")

Input

1 2 3 2 1

#Output

Palindrome List