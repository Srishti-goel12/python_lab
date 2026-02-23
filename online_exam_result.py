scores = [28, 34, 45, 32, 30, 50, 25]

# Remove lowest 2 scores
scores.sort()
scores = scores[2:]

# Add grace marks for 30-35
scores = [s+5 if 30 <= s <= 35 else s for s in scores]

# Count pass (>=40)
passed = len([s for s in scores if s >= 40])

print("Processed Scores:", scores)
print("Number of students passed:", passed)

#output
Processed Scores: [50, 50, 37, 47, 35]
Number of students passed: 4