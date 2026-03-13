s = input()
count = 0

for ch in s.lower():
    if ch in "aeiou":
        count += 1

print("Vowels =", count)

Input

hello


#Output

Vowels = 2