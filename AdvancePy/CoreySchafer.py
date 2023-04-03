class Employee:
    raised_amount = 1.04
    numbers_of_employee = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.fullname = first+last
        self.email = first+"."+last+"@company.com"
        Employee.numbers_of_employee += 1
        # self.numbers_of_employee += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def applyraise(self):
        return self.pay*self.raised_amount


emp1 = Employee('sajid', 'khan', 70000)
# print(emp1.fullname())
# print(emp1.email)
# print(emp1.pay)
# print(emp1.applyraise())


# print(Employee.__dict__)
# print(emp1.__dict__)
emp1.raised_amount = 1.05
Employee.raised_amount = 1.30

print(emp1.raised_amount)
print(Employee.raised_amount)

print(Employee.numbers_of_employee)

# Closer
# Decorators