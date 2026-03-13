def gcd(a,b):
    while b != 0:
        a,b = b,a%b
    return a

x = int(input())
y = int(input())

print("GCD =", gcd(x,y))

Input

12
18

#Output

GCD = 6