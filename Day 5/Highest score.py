print("This program calculates the average height of a c;ass of students")
student_scores = input("Enter student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)


highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the classs is: {highest_score}")