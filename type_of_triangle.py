a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

# Sample Input
5
5
5
# Output
Equilateral Triangle