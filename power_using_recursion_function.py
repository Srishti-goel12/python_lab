def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp-1)

b = int(input())
e = int(input())

print("Power =", power(b,e))

Input

2
3

#Output

Power = 8