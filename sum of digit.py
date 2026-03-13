num = int(input())
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num = num // 10

print("Sum of digits =", total)


# Sample Input
1234
# Output
Sum of digits = 10