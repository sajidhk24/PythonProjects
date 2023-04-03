from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import inch, A4, letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image

data = [["St. Xavier's College of Management & Technology, Patna"], ['Continuous Internal Assessment, 1st Semester'],
        ['Progress Report'], ['Stream', 'BCA 1', '', 'Roll No', 'BCA2021026'],
        ['Name', 'Vishnu Kumar', '', 'Attendance(%)', '90'],
        ['Name of Paper', 'Full Marks', 'Pass Marks', 'Marks Obtained', 'Remarks'],
        ['English', '40', '18', '35', 'Pass'],
        ['Maths', '40', '18', '35', 'Pass'],
        ['Python', '40', '18', '35', 'Pass'],
        ['PMO', '40', '18', '35', 'Pass'],
        ['IT', '40', '18', '35', 'Pass'],
        ['Meet', 'Coordinator', 'Total Marks', '200', ''], ['', '', '', '', ''],
        ['Fr. Dr. A. Sebastian SJ', '', '', 'Fr. Dr. Martin Poras SJ'],
        ['Controller of Examination', '', '', 'Principal']]
filename = 'pdf.pdf'
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
