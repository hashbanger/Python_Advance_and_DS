#Dunder methods or Underscores
#These methods allow us to emulate some built-in behaviour in python
#also this is how we implement operator overloading 


class Employees:
    def __init__(self, firstName, lastName ,mail):
        self.firstName = firstName
        self.lastName = lastName
        self.mail = mail

    def fullName(self):
        return (self.firstName+" "+self.lastName)
    
emp1 = Employees('Bruce','Wayne','BruceWayne@dc.com')
emp2 = Employees('Clark','Kent','ClarkKent@dc.com')

print(emp1) #prints out <__main__.Employees object at 0x000001578A76B7B8>

#The two methods that work under this are
#__repr__ and __str__
#When in absence of __str__ control fallbacks to __repr__
class Employees:
    def __init__(self, firstName, lastName ,mail):
        self.firstName = firstName
        self.lastName = lastName
        self.mail = mail

    def fullName(self):
        return (self.firstName+" "+self.lastName)
    
    def __repr__(self):
        return "Employee({}, {}, {})".format(self.firstName, self.lastName, self.mail)

emp1 = Employees('Bruce','Wayne','BruceWayne@dc.com')
emp2 = Employees('Clark','Kent','ClarkKent@dc.com')

print(emp1)


class Employees:
    def __init__(self, firstName, lastName ,mail):
        self.firstName = firstName
        self.lastName = lastName
        self.mail = mail

    def fullName(self):
        return (self.firstName+" "+self.lastName)
    
    def __repr__(self):
        return "Employee({}, {}, {})".format(self.firstName, self.lastName, self.mail)
    
    def __str__(self):
        return "{} - {}".format(self.firstName, self.lastName)

emp1 = Employees('Bruce','Wayne','BruceWayne@dc.com')
emp2 = Employees('Clark','Kent','ClarkKent@dc.com')

print(emp1)
#we can still call repr manually
print(emp1.__repr__())

#We can alter the builtin operators like '+' calls __add__ under the hood
#thats' how it works for strings as well as numbers

class Employees:
    def __init__(self, firstName, lastName ,pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay

    def fullName(self):
        return (self.firstName+" "+self.lastName)
    
    def __repr__(self):
        return "Employee({}, {}, {})".format(self.firstName, self.lastName, self.pay)

    def __add__(self, other):
        return self.pay + other.pay

emp1 = Employees('Bruce','Wayne',1200000)
emp2 = Employees('Clark','Kent',32600)

#Absence of our __add__ will result in a type error here
print(emp1 + emp2)

