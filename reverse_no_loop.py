Reverse a number (while loop)
num = int(input())
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed =", rev)
🔹 Input
123
🔹 Output
Reversed = 321