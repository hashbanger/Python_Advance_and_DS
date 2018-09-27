#classmethods and static methods

class Employees:
    empCount = 0
    raiseValue = 1.04
    
    def __init__(self, firstName, lastName ,pay, mail):
        self.firstName = firstName
        self.lastName = lastName
        self.mail = mail
        self.pay = pay
    
        Employees.empCount += 1
    
    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def apply_raise(self):
        self.pay = self.pay * self.raiseValue 
    
    @classmethod
    def set_raise_amt(cls, amount): #takes in class as defoault argumet in 'cls' by common convention like 'self'
        cls.raiseValue = amount

emp1 = Employees('Bruce','Wayne',1000000,'BruceWayne@dc.com')
emp2 = Employees('Clark','Kent',25000,'ClarkKent@dc.com')


Employees.set_raise_amt(1.05)
#we could also make changes to the class variable from classmethod using instance
#but that generally doesn't make a lot of sense
# 'emp1.set_raise_amt(1.05)'
print(Employees.raiseValue)
print(emp1.raiseValue)
print(emp2.raiseValue)

#We can use class methods to make alternative constructors
#Consider a scenario where for creating the Employee object
#we are required to parse a string everytime
# 'Diana-Prince-12000'

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
    
    @classmethod
    def set_raise_amt(cls, amount): #takes in class as defoault argumet in 'cls' by common convention like 'self'
        cls.raiseValue = amount

    @classmethod
    def parseString(cls, emp_string):
        firstname, lastname, pay, mail = emp_string.split('-')
        return cls(firstname, lastname, pay, mail)

emp1 = Employees('Bruce','Wayne',1000000,'BruceWayne@dc.com')
emp2 = Employees('Clark','Kent',25000,'ClarkKent@dc.com')

emp_str_3 = 'Diana-Prince-12000-DianaPrince@dc.com'
emp3 = Employees.parseString(emp_str_3)


print(emp3.firstName)
print(emp3.lastName)
print(emp3.pay)
print(emp3.mail)

#---------------------------------------------------------------------------------------------------
#Static Methods
#Static methods are the ones which do ot require a default argument passing 
#unlike classmethods and instancemethods

#Static methods are usually have operation independent to instances

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
    
    @classmethod
    def set_raise_amt(cls, amount): #takes in class as defoault argumet in 'cls' by common convention like 'self'
        cls.raiseValue = amount

    @classmethod
    def parseString(cls, emp_string):
        firstname, lastname, pay, mail = emp_string.split('-')
        return cls(firstname, lastname, pay, mail)

    @staticmethod
    def isWorking(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True
emp1 = Employees('Bruce','Wayne',1000000,'BruceWayne@dc.com')
emp2 = Employees('Clark','Kent',25000,'ClarkKent@dc.com')

import datetime
my_date = datetime.date(2018, 9, 29)

print(Employees.isWorking(my_date))
