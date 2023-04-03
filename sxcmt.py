departments = {
    'bca': {
        1: {'it': 0, 'it(p)': 0, 'python': 0, 'python(p)': 0, 'pmo': 0, 'english': 0},
        2: {'maths': 0, 'c': 0, 'c(p)': 0, 'sad': 0, 'english': 0, 'os': 0, 'os(p)': 0}
    }
}

name = str(input("Enter the name of the student: "))
roll = int(input("Enter the roll number of the student: "))
sem = int(input("enter the semester: "))
sem = departments['bca'][sem]
for i, key in enumerate(sem):
    sem[key] = int(input(f'Enter the marks for {key} out of 60: '))
crossed_subject = []
note = ""
for key in sem:
    if sem[key] < 24:
        crossed_subject.append(key)

if len(crossed_subject) <= 1:
    note += "You have to meet coordinator"
elif len(crossed_subject) <= 2:
    note += "You have to meet Vice-Principle"
else:
    note += "You have to meet Principle"
remarks = str(input("Enter the remarks for the student: "))
print("Name of the student is: ", name)
print("\b And the rollNo of the student is: ", roll)
for key in sem:
    print(f"Marks obtained in {key} is {sem[key]}")
print("Note: ", note)
print("Remark from the teacher:", remarks)
total_marks = len(sem) * 60
# print(total_marks)
total_marks_gained = 0
for key in sem:
    total_marks_gained += sem[key]
percentage = round(float((total_marks_gained / total_marks) * 100), 2)
print(percentage)