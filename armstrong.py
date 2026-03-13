Armstrong Number
num = int(input())
temp = num
power = len(str(num))
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp //= 10

if total == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
🔹 Input
153
🔹 Output
Armstrong Number