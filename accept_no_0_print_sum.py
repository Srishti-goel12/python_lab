Accept numbers until 0 and print sum
total = 0
num = int(input())

while num != 0:
    total += num
    num = int(input())

print("Sum =", total)

 #Input
5
10
3
0
# Output
Sum = 18