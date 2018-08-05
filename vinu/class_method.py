class Employee:
    def __init__( self, first, last, salary):
         self.first = first
         self.last = last
         self.salary = salary

    def fullname(self):
        name = self.first + self.last
        return name

    def email(self):
        email = self.first + '.' + self.last + '@company.com'
        return email

    def salary(self):
        return int(self.salary)

emp_1 = Employee('salvy', 'joseph' , 50000)
emp_2 = Employee('micheal', 'philip' , 60000)

print emp_1.fullname()
print emp_1.email()
print emp_1.salary

print emp_2.fullname()
print emp_2.email()
print emp_2.salary

