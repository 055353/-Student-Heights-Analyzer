# Program to take in the heights of students and find the total and average
student_heights = input("Input a list of student heights separated by space: ").split()

# Convert the student heights to integers
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

print("Student Heights:", student_heights)

# Initialize variables to store the total height and number of students
total_height = 0
number_of_students = 0

# Calculate the total height and number of students
for height in student_heights:
    total_height += height
    number_of_students += 1

# Calculate the average height
if number_of_students != 0:
    average_height = total_height / number_of_students
    rounded_average = round(average_height)
    print("The total height is:", total_height)
    print("The average height is:", rounded_average)
else:
    print("The list is empty.")
