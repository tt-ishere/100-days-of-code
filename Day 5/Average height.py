print("This program calculates the average height of a c;ass of students")
student_heights = input("Enter student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
number_ofStudents = 0

sum_ofheight = 0
for height in student_heights:
    sum_ofheight += height
    number_ofStudents += 1

# print(f"Number of students: {number_ofStudents}")
# print(f"Sum of students height: {sum_ofheight}")
average_height = round(sum_ofheight / number_ofStudents)


print(f"Average height of the class is {average_height}")