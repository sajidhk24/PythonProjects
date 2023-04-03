from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import inch, A4, letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image

departments = {
    'bca': {
        # 1: {'it': 0, 'it(p)': 0, 'python': 0, 'python(p)': 0, 'pmo': 0, 'english': 0},
        1: {'it': 0, 'it(p)': 0, 'python': 0, 'python(p)': 0, 'pmo': 0},
        2: {'maths': 0, 'c': 0, 'c(p)': 0, 'sad': 0, 'english': 0, 'os': 0, 'os(p)': 0}
    }
}
sub_data = []
# name will take name of the student
name = str(input("Enter the name of the student: ")).title()
# roll will take roll of the student
roll = int(input("Enter the roll number of the student: "))
# attendance of the student
attendance = int(input("Enter the attendance of the stdudent: "))
# it will take semester of the exam
semestere = int(input("enter the semester: "))
# it will fetch data of particular semester of particular department
sem = departments['bca'][semestere]
crossed_subject = []
for i, key in enumerate(sem):
    remark = ''
    sub = []
    sem[key] = int(input(f'Enter the marks for {key} out of 60: '))
    list(key)
    sub.append(key.title())
    sub.append('40')
    sub.append('18')
    sub.append(sem[key])
    if sem[key] >= 24:
        remark += 'Pass'
        sub.append(remark)
    else:
        remark += 'Fail'
        sub.append(remark)
        crossed_subject.append(sem[key])
    sub_data.append(sub)
note = ""
if len(crossed_subject) <= 1:
    note += "Meet coordinator"
elif len(crossed_subject) <= 2:
    note += "Vice-Principle"
else:
    note += "Principle"
total_marks = len(sem) * 40
# print(total_marks)
total_marks_gained = 0
for key in sem:
    total_marks_gained += sem[key]
percentage = round(float((total_marks_gained / total_marks) * 100), 2)

########################################

data = [["St. Xavier's College of Management & Technology, Patna"], ['Continuous Internal Assessment, 1st Semester'],
        ['Progress Report'], ['Stream', f'BCA {semestere}', '', 'Roll No', f'BCA20210{roll}'],
        ['Name', name, '', 'Attendance(%)', str(attendance)],
        ['Name of Paper', 'Full Marks', 'Pass Marks', 'Marks Obtained', 'Remarks']] + sub_data + [
        ['Meet', str(note), 'Total Marks', str(total_marks), ''], ['', '', '', '', ''],
        ['Fr. Dr. A. Sebastian SJ', '', '', 'Fr. Dr. Martin Poras SJ'],
        ['Controller of Examination', '', '', 'Principal']]
filename = 'sxcm.pdf'
pagesize = (5 * inch, 6 * inch)
pdf = SimpleDocTemplate(filename, pagesize=pagesize)
t = Table(data)
style = TableStyle(
    [('SPAN', (0, 0), (4, 0)), ('SPAN', (0, 1), (4, 1)), ('SPAN', (0, 2), (4, 2)), ('SPAN', (0, 13), (1, 13)),
     ('SPAN', (3, 13), (4, 13)), ('SPAN', (0, 14), (1, 14)), ('SPAN', (3, 14), (4, 14)),
     ('TEXTCOLOR', (0, 0), (4, 14), colors.black), ('ALIGN', (0, 0), (4, 14), 'CENTER'),
     ('VALIGN', (0, 0), (4, 14), 'MIDDLE'), ('FONTNAME', (0, 0), (4, 14), 'Times-Roman'),
     ('FONTSIZE', (0, 0), (4, 14), 8), ('BOX', (0, 3), (4, 11), 1, colors.black),
     ('INNERGRID', (0, 3), (4, 11), 0.25, colors.black)])
t.setStyle(style)
elems = []
elems.append(t)
pdf.build(elems)
