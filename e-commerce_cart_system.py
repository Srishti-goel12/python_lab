prices = [1500, 2000, 1500, 1000, 1200]

# Remove duplicates
prices = list(set(prices))

# Calculate total
total = sum(prices)

# Apply discount if total > 5000
if total > 5000:
    total *= 0.9  # 10% discount

# Add GST 18%
total *= 1.18

print("Final Payable Amount: ₹", round(total, 2))

#output
Final Payable Amount: ₹9444.0