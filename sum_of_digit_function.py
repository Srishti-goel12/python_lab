def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

num = int(input())
print("Sum =", sum_digits(num))

Input

123

#Output

Sum = 6