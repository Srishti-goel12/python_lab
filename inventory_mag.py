stock = [0, 5, 20, 8, 0, 15]

# Remove 0 stock
stock = [s for s in stock if s != 0]

# Restock items <10
stock = [s+50 if s<10 else s for s in stock]

# Total inventory
total_inventory = sum(stock)

print("Updated Stock:", stock)
print("Total Inventory:", total_inventory)

#output
Updated Stock: [55, 20, 58, 15]
Total Inventory: 148