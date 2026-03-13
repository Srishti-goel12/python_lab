s = input()
freq = {}

for ch in s:
    freq[ch] = freq.get(ch,0) + 1

print(freq)

Input

hello

#Output

{'h': 1, 'e': 1, 'l': 2, 'o': 1}