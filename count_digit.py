Count digits in a number
num = int(input())
count = 0
while num > 0:
    count += 1
    num //= 10
print("Digits =", count)
🔹 Input
4567
🔹 Output
Digits = 4