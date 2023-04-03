departments = {
    'bca': {
        1: {'it': 0, 'it(p)': 0, 'python': 0, 'python(p)': 0, 'pmo': 0, 'english': 0},
        2: {'maths': 0, 'c': 0, 'c(p)': 0, 'sad': 0, 'english': 0, 'os': 0, 'os(p)': 0}
    }
}
sub_data = []
# name will take name of the student
name = str(input("Enter the name of the student: "))
# roll will take roll of the student
roll = int(input("Enter the roll number of the student: "))
# it will take semester of the exam
semestere = int(input("enter the semester: "))
# it will fetch data of particular semester of particular department
sem = departments['bca'][semestere]
crossed_subject = []
for i, key in enumerate(sem):
    sub = []
    sem[key] = int(input(f'Enter the marks for {key} out of 60: '))
    list(key)
    sub.append(key)
    sub.append(sem[key])
    sub.append('40')
    sub.append('18')
    sub.append('35')
    sub_data.append(sub)
    if sem[key] < 24:
        remark = 'Pass'
    else:
        remark = 'Fail'
        crossed_subject.append(sem[key])
note = ""
if len(crossed_subject) <= 1:
    note += "Meet coordinator"
elif len(crossed_subject) <= 2:
    note += "Meet Vice-Principle"
else:
    note += "Meet Principle"
print("Name of the student is: ", name)
print("\b And the rollNo of the student is: ", roll)
total_marks = len(sem) * 60
# print(total_marks)
total_marks_gained = 0
for key in sem:
    total_marks_gained += sem[key]
percentage = round(float((total_marks_gained / total_marks) * 100), 2)