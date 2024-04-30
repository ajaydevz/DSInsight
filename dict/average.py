student_grades = {
    "Math": 85,
    "Science": 90,
    "History": 75,
    "English": 88
}

total = sum(student_grades.values())
average = total / len(student_grades)

print(average)
total = 0
for i in student_grades.values():
    total += i

ave_rage = total/len(student_grades)
print(total)
print(ave_rage)
        