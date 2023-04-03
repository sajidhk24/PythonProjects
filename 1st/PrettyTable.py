from prettytable import PrettyTable

table = PrettyTable()
table.add_column("subjects",
                 ['Maths', 'English', 'CS'])
table.add_column("marks",
                 [90, 92, 96])
print(table)