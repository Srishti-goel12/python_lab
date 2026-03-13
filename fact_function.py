ef factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

num = int(input())
print("Factorial =", factorial(num))

Input

4

#Output

Factorial = 24