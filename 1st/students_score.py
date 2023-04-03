students_score = {
    'Harry': 89,
    'Ron': 78,
    'Hermione': 99,
    'Daraco': 74,
    'Neville': 62
}
students_grade = {}
for students in students_score:
    score = students_score[students]
    if score > 90:
        students_grade[students] = 'Outstanding'
    elif 90 > score > 80:
        (students_grade[students]) = 'Exceeds Expectation'
    elif 70 < score < 80:
        (students_grade[students]) = 'Acceptable'
    else:
        (students_grade[students]) = 'Fail'
print(students_grade)