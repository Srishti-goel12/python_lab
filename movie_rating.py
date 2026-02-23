ratings = [5, 4, 3, 6, 5, 0, 2]

# Remove invalid ratings
ratings = [r for r in ratings if 1 <= r <=5]

# Average rating
avg_rating = sum(ratings)/len(ratings)

# Count 5-star
five_star = ratings.count(5)

# Sort ascending
ratings.sort()

print("Valid Ratings:", ratings)
print("Average Rating:", avg_rating)
print("5-Star Count:", five_star)