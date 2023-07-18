student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades={}

for i in student_scores.keys():
    student_grades[i]=student_scores[i]
    if student_grades[i]>90:
        student_grades[i]="Outstanding"
    elif student_grades[i]>80:
        student_grades[i]="Exceeds Expectations"
    elif student_grades[i]>70:
        student_grades[i]="Acceptable"
    else:
        student_grades[i]="Fail"

print(student_grades)