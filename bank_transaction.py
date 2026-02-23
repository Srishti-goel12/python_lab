transactions = [5000, -2000, 15000, -5000, 12000]

# Total balance
balance = sum(transactions)

# Largest withdrawal
withdrawals = [t for t in transactions if t<0]
largest_withdrawal = min(withdrawals) if withdrawals else 0

# Deposits > 10000
large_deposits = len([t for t in transactions if t>10000])

print("Total Balance:", balance)
print("Largest Withdrawal:", largest_withdrawal)
print("Deposits >10000:", large_deposits)

#output
Total Balance: 25000
Largest Withdrawal: -5000
Deposits >10000: 2