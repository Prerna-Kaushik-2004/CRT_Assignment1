#MULTIPLE INHERITANCE
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary
class Manager(Person, Employee):
    def __init__(self, name, age, emp_id, salary):
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)
    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nEmployee ID: {self.emp_id}\nSalary: {self.salary}")
obj=Manager("Prerna",21,1234,50000)
obj.display()        