import matplotlib.pyplot as plt


class Personnel:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return '{} {}'.format(self.first.capitalize(), self.last.capitalize())

    @property
    def email(self):
        return '{}.{}@company.com'.format(
            self.first.lower(), self.last.lower())

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last


# stu1 = Personnel('Maiya', 'Hee')
# print(stu1.email)

# stu1.first = 'hak'
# print(stu1.email)
# stu1.fullname = 'Mia Maiya'
# print(stu1.email)


class Employee(Personnel):
    """docstring for Employee"""

    def __init__(self, first, last, pay):
        super().__init__(first, last)
        self.pay = pay


class Manager(Employee):
    """docstring for Manager"""

    def __init__(self, first, last, pay, employees):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees


EMP1 = Employee('Jon', 'Red', 100000)
EMP2 = Employee('Vin', 'Jud', 200000)
MGR1 = Manager('Bishal', 'Shakya', 500000, [EMP1, EMP2])

print(MGR1.email)

plt.plot(list(range(8)), [x * x for x in range(8)])
plt.show()


class Staffs(Personnel):
    """docstring for Staffs"""

    def __init__(self, first, last, hours):
        super().__init__(first, last)
        self.hours = hours


MESSAGE = 'hello\'s cafe!'
print(MESSAGE.upper())
