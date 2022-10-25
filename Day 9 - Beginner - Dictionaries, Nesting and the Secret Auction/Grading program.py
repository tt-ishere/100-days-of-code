student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    if student_scores[student] in range(90, 101):
        student_grades[student] = "Outstanding"
    elif student_scores[student] in range(81, 91):
        student_grades[student] = "Exceeds expectations"
    elif student_scores[student] in range(71, 81):
        student_grades[student] = "Acceptable"
    elif student_scores[student] < 70:
        student_grades[student] = "Fair"

# 🚨 Don't change the code below 👇
print(student_grades)
