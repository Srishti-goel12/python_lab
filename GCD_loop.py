GCD using while loop
a = int(input())
b = int(input())

while b != 0:
    a, b = b, a % b

print("GCD =", a)
🔹 Input
12
18
🔹 Output
GCD = 6