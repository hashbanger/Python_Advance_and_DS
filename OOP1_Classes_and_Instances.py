#Classes and Instances

class Employees:
    pass


#Storing information of different Employees can be redundant 
emp1 = Employees()
emp1.firstName = 'Bruce'
emp1.lastName = 'Wayne'
emp1.mail  = 'BruceeWayne@dc.com'

emp2 = Employees()
emp2.firstName = 'Clark'
emp2.lastName = 'Kent'
emp2.mail  = 'ClarkKent@DC'

print(emp1.firstName)
print(emp2.firstName)

#To remove this redundancy we can use 'self' keyword
#By default the object name is passed as the self argument
#We can use a constructor as follows for the initialization
class Employees:
    def __init__(self, firstName, lastName ,mail):
        self.firstName = firstName
        self.lastName = lastName
        self.mail = mail

    def fullName(self):
        return (self.firstName+" "+self.lastName)
    
emp1 = Employees('Bruce','Wayne','BruceWayne@dc.com')
emp2 = Employees('Clark','Kent','ClarkKent@dc.com')

print(emp1.firstName)
print(emp1.mail)
print(emp2.lastName)
print(emp1.fullName())
#We can also call a function by its class name but then the object for self
#will need to be passes explicitly
#That's how it actually works under the hood

class Employees:
    def __init__(self, firstName, lastName ,mail):
        self.firstName = firstName
        self.lastName = lastName
        self.mail = mail

    def fullName(self):
        return (self.firstName+" "+self.lastName)
    
emp1 = Employees('Bruce','Wayne','BruceWayne@dc.com')
emp2 = Employees('Clark','Kent','ClarkKent@dc.com')

#emp1 = Employees('Bruce','Wayne','BruceWayne@dc.com') is same as:
print(Employees.fullName(emp1))