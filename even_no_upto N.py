Sum of even numbers up to N
n = int(input())
i = 1
total = 0
while i <= n:
    if i % 2 == 0:
        total += i
    i += 1
print("Sum of even numbers =", total)
🔹 Input
6
🔹 Output
Sum of even numbers = 12