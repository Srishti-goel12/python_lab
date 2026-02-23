points = [25, 40, -5, 30, 15]

# Replace negative with 0
points = [p if p>=0 else 0 for p in points]

# Sort leaderboard
points.sort(reverse=True)

winner = points[0]
runner_up = points[1]

print("Leaderboard:", points)
print("Winner:", winner)
print("Runner-up:", runner_up)

#output
Leaderboard: [40, 30, 25, 15, 0]
Winner: 40
Runner-up: 30