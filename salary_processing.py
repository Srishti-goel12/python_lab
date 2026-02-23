salaries = [30000, 60000, 45000, 70000, 25000]

# Remove below minimum wage (30000)
salaries = [s for s in salaries if s >= 30000]

# Add 5% bonus if > 50000
salaries = [s*1.05 if s>50000 else s for s in salaries]

# Sort descending
salaries.sort(reverse=True)

# Display top 3
top3 = salaries[:3]

print("Processed Salaries:", salaries)
print("Top 3 Salaries:", top3)

#output
Processed Salaries: [73500.0, 63000.0, 45000, 30000]
Top 3 Salaries: [73500.0, 63000.0, 45000]