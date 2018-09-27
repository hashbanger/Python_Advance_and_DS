#Class Variables

#Class variables are the ones that is same and is shared for all instances
#In python it is still accessed by the instance of the class or the class Name itself.

class Employees:
    raiseValue = 1.04
    def __init__(self, firstName, lastName ,pay, mail):
        self.firstName = firstName
        self.lastName = lastName
        self.mail = mail
        self.pay = pay

    def apply_raise(self):
        self.pay = self.pay * Employees.raiseValue #Or self.pay * self.raisePCT 
    
emp1 = Employees('Bruce','Wayne',1000000,'BruceWayne@dc.com')
emp2 = Employees('Clark','Kent',25000,'ClarkKent@dc.com')

emp1.apply_raise()
print(emp1.pay)
emp2.apply_raise()
print(emp2.pay)

#Any changes made to the class variable will be reflected for all instances
class Employees:
    raiseValue = 1.04
    def __init__(self, firstName, lastName ,pay, mail):
        self.firstName = firstName
        self.lastName = lastName
        self.mail = mail
        self.pay = pay

    def apply_raise(self):
        self.pay = self.pay * Employees.raiseValue #Or self.pay * self.raisePCT 
    
emp1 = Employees('Bruce','Wayne',1000000,'BruceWayne@dc.com')
emp2 = Employees('Clark','Kent',25000,'ClarkKent@dc.com')

Employees.raiseValue = 1.05

emp1.apply_raise()
print(emp1.pay)
emp2.apply_raise()
print(emp2.pay)

#We can check the attributes of a class ad the instances as
print(emp1.__dict__)
print(Employees.__dict__)
#However if we make changes to an instance's class variable 
#Then that class variable is implicitly created in that instance's scope


class Employees:
    raiseValue = 1.04
    def __init__(self, firstName, lastName ,pay, mail):
        self.firstName = firstName
        self.lastName = lastName
        self.mail = mail
        self.pay = pay

    def apply_raise(self):
        self.pay = self.pay * self.raiseValue 
    
emp1 = Employees('Bruce','Wayne',1000000,'BruceWayne@dc.com')
emp2 = Employees('Clark','Kent',25000,'ClarkKent@dc.com')

emp1.raiseValue = 1.05

emp1.apply_raise()
print(emp1.pay)
print(emp1.__dict__)
print()
emp2.apply_raise()
print(emp2.pay)
print(emp2.__dict__)

#Sometimes there are scenarios when it doesn't make sense to use self
#For counting the number of Employees
#we won't use self rather the class name for counting the instances

class Employees:
    empCount = 0
    raiseValue = 1.04
    def __init__(self, firstName, lastName ,pay, mail):
        self.firstName = firstName
        self.lastName = lastName
        self.mail = mail
        self.pay = pay
        Employees.empCount += 1
    def apply_raise(self):
        self.pay = self.pay * self.raiseValue 
    
emp1 = Employees('Bruce','Wayne',1000000,'BruceWayne@dc.com')
emp2 = Employees('Clark','Kent',25000,'ClarkKent@dc.com')

print('Number of Employees = ',Employees.empCount)

#De nada!

