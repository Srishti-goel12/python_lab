attendance = [1,0,1,1,0,0,1,0,0,0]

# Calculate percentage
percentage = sum(attendance)/len(attendance)*100

# Students below 75% (example: assuming one value per student)
# Here for demo, assume each item is student total
below_75 = [i+1 for i,a in enumerate(attendance) if a*100 < 75]

# Replace consecutive absences with 'Warning'
for i in range(len(attendance)-1):
    if attendance[i] == 0 and attendance[i+1] == 0:
        attendance[i+1] = 'Warning'

print("Attendance:", attendance)
print("Attendance %:", percentage)
print("Students below 75%:", below_75)

#output
Attendance: [1, 0, 1, 1, 0, 'Warning', 1, 0, 'Warning', 0]
Attendance %: 40.0
Students below 75%: [2, 5, 6, 8, 9, 10]