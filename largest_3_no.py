# Read input
a = int(input())
b = int(input())
c = int(input())

# Find largest
if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)


#output
Largest number is: 25
