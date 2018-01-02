#Think of a class as a blueprint to an object.
#An object is an instance of a class.
#Data inside an object or class is called a data attribute.
#Functions inside the object are called methods.

#Turtle example
import turtle
Yertle=turtle.Pen()
Myrtle=turtle.Pen()
Yertle.shape("turtle")
Yertle.color("green")
Myrtle.color("blue")
Myrtle.shape("turtle")
Yertle.up()
Myrtle.up()
Myrtle.back(50)
Myrtle.left(90)
for x in range(0,5):
    Yertle.circle(100)
    Myrtle.circle(100)

 

 

#Bank Account example
class BankAccount:
    # __init__ is a built-in "method" that initializes a new
    # instance or object of this class.
    def __init__(self,name,amount):
        self.name = name
        self.balance = amount

    # The method used to print a statement
    def statement(self):
        print("%s balance is %s." % (self.name, self.balance))

    # The method used to take money out of the account.
    def withdraw(self, amount):
        self.balance -= amount
        self.statement()

    # The method used to put money into the account.
    def deposit(self, amount):
        self.balance += amount
        self.statement()

    def transfer(self, amount, ToAccount):
        self.balance -= amount
        ToAccount.balance += amount
        self.statement()
        ToAccount.statement()

WECU=BankAccount("WECU",100)
ICU=BankAccount("ICU",50)

WECU.statement()
ICU.statement()

WECU.withdraw(20)

WECU.transfer(25,ICU)

 

 

#Employee example

class Employee:
    #Common base class for all employees
    empCount = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        self.empNum = Employee.empCount
    
    def displayCount(self):
        print ("%s is employee %d of %d" % (self.name,self.empNum,Employee.empCount))
    
    def displayEmployee(self):
        print ("Name : ", self.name, ", Salary: ", self.salary)


#This would create first object of Employee class
Luke = Employee("Luke", 2000)
#This would create second object of Employee class
Han = Employee("Han", 3000)

Luke.displayEmployee()
Han.displayEmployee()
Luke.displayCount()

#Manager class derived from Employee that also has a department and can adjust salaries
class Manager(Employee):
    
    def __init__(self, name, salary, department):
        self.department = department
        Employee.__init__(self, name, salary)
    
    def displayManager(self):
        self.displayEmployee()
        print("%s manages the %s department." % (self.name, self.department))
    
    def adjustSalary(self, employee, amount, reason):
        employee.salary += amount
        print ("%s\'s new salary is %s." % (employee.name,employee.salary))
        print ("Reason for adjustment: %s" % reason)

 

#Create a new instance of a Manager which also includes all the attributes of an Employee

Darth=Manager("Darth",4500,"Death Star")

Darth.displayManager()

#Only Managers can adjust salaries
Darth.adjustSalary(Luke,-25,"Attacking my department")
