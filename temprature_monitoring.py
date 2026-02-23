temps = [38, 42, 45, 47, 40, 35]

# Hottest and coldest
hottest = max(temps)
coldest = min(temps)

# Replace >45 with 'Heat Alert'
temps = ["Heat Alert" if t>45 else t for t in temps]

# Count extreme days >40
extreme_days = len([t for t in temps if isinstance(t,int) and t>40])

print("Temperatures:", temps)
print("Hottest:", hottest, "Coldest:", coldest)
print("Extreme days:", extreme_days)

#output
Temperatures: [38, 42, 45, 'Heat Alert', 40, 35]
Hottest: 47 Coldest: 35
Extreme days: 3