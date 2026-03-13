# Read input
P = float(input())   # Principal
R = float(input())   # Rate
T = float(input())   # Time

# Calculate CI
Amount = P * (1 + R/100) ** T
CI = Amount - P

# Output
print("Compound Interest =", CI)

#output
1000
10
2
Compound Interest = 210.0