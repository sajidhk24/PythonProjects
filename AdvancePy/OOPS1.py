class Employee:
    number_of_employee = 0  # each time we create instance using init it increments by 1
    raise_amount = 1.04  # Class level variable which is easily accessible for all instances of class

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = int(pay)
        self.email = first + "." + last + "@company.com"

        Employee.number_of_employee += 1  # with ever instance it increments

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee(
    'Sajid', 'Khan', 80000
)
emp_2 = Employee(
    'Maximilian', 'Abr', 70000
)
emp_3 = Employee(
    'Danish', 'xyz', 10000
)
'''
print(emp_1.first)
print(emp_1.email)
print(Employee.fullname(emp_1))  # class level method
print(emp_1.fullname())  # instances level method
emp_1.apply_raise()
emp_2.raise_amount = 2  # redefining the value at instances level
emp_2.apply_raise()
print(emp_1.pay)
print(emp_2.pay)
print(Employee.number_of_employee)
'''
'''
print(isinstance(emp_1, Employee))
x = Employee('x', 'x', 1)
y = Employee('y', 'y', 1)
print(x == y)
'''
