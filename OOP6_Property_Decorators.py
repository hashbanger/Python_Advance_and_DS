#Property_decorators-  Getters, Setters and Deleters

#Suppose the following scenario
'''
class Employees:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.mail = self.firstName + "." + self.lastName + "@dc.com"

    def fullName(self):
        return (self.firstName+" "+self.lastName)
    
emp1 = Employees('Bruce','Wayne')
emp2 = Employees('Clark','Kent')

emp1.firstName = 'Thomas'

print(emp1.firstName)
print(emp1.mail)
print(emp1.fullName())

#We can observe that if we changed the name then the mail didn't change
#for solving this problem we could make email as method 
#but that would require a lot of code change, as changing attribute to method
#we could use property decorator here

class Employees:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    @property
    def mail(self):
        return (self.firstName + "." + self.lastName + '@dc.com')
        
    def fullName(self):
        return (self.firstName+" "+self.lastName)
    
emp1 = Employees('Bruce','Wayne')
emp2 = Employees('Clark','Kent')

emp1.firstName = 'Thomas'

print(emp1.firstName)
print(emp1.mail)
print(emp1.fullName())
'''

#Consider another scenario
#we want to set the full name and want it to make changes to the
#actual first name and last name as well
#emp1.fullName = 'Thomas Wayne' ----> this would give 'can't set attribute' exception
#So we'll use a setter

class Employees:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    @property
    def mail(self):
        return (self.firstName + "." + self.lastName + '@dc.com')
    
    @property
    def fullName(self):
        return (self.firstName+" "+self.lastName)
    
    @fullName.setter
    def fullName(self, name):
        first , last = name.split(' ')
        self.firstName = first
        self.lastName = last

    #We can implement a deleter also in the similar fashion
    @fullName.deleter
    def fullName(self):
        print("\nFull Name deleted! \n")
        self.firstName = None
        self.lastName = None

emp1 = Employees('Bruce','Wayne')
emp2 = Employees('Clark','Kent')

emp1.fullName = "Thomas Wayne"


print(emp1.firstName)
print(emp1.mail)
print(emp1.fullName)

del emp1.fullName
print(emp1.firstName)
#We can observe that the other attributes have also changed
#Deleter has also deleted the first name

#De nada!