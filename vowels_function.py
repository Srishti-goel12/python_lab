def count_vowels(s):
    count = 0
    for ch in s.lower():
        if ch in "aeiou":
            count += 1
    return count

s = input()
print("Vowels =", count_vowels(s))

Input

apple

#Output

Vowels = 2