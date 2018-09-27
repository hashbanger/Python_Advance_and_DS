#Inheritance

class Employees:
    raiseValue = 1.04
    
    def __init__(self, firstName, lastName ,pay, mail):
        self.firstName = firstName
        self.lastName = lastName
        self.mail = mail
        self.pay = pay
    
    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def apply_raise(self):
        self.pay = self.pay * self.raiseValue 
    
class Developer(Employees):
    raiseValue = 1.05

    def apply_raise(self):
        self.pay = self.pay * self.raiseValue

dev1 = Developer('Bruce','Wayne',1000000,'BruceWayne@dc.com')
dev2 = Developer('Clark','Kent',25000,'ClarkKent@dc.com')

print(dev1.firstName)
print(dev1.lastName)
print(dev1.pay)
print(dev1.mail)

#If method is found in local scope then its superclass method is overriden
#we can check the method resolution using help()

print('\nafter raise')
dev1.apply_raise()
print(dev1.pay)

print(help(dev1))

#We can use the super class's constructor for reusability
#Consider a scenario where we wan an additional argument


class Employees:
    raiseValue = 1.04
    
    def __init__(self, firstName, lastName ,pay, mail):
        self.firstName = firstName
        self.lastName = lastName
        self.mail = mail
        self.pay = pay
    
    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def apply_raise(self):
        self.pay = self.pay * self.raiseValue 
    
class Developer(Employees):
    raiseValue = 1.05
    def __init__(self, firstName, lastname, pay , mail, language):
        super().__init__(firstName, lastname, pay , mail)
        #or Employee.__init__(self, firstName, lastname, pay , mail)
        self.language = language

class Manager(Employees):
    def __init__(self, firstName, lastname, pay , mail, employees = None):
        super().__init__(firstName, lastname, pay , mail)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
        
    def addEmp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def removeEmp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def printEmp(self):
        for emp in self.employees:
            print("--->", emp.firstName)
        
dev1 = Developer('Bruce','Wayne',1000000,'BruceWayne@dc.com', 'Python')
dev2 = Developer('Clark','Kent',25000,'ClarkKent@dc.com', 'Java')

mgr1 = Manager('Amanda', 'Waller', 120000, 'AmandaWaller@dc.com', [dev1, dev2] )
print(mgr1.firstName, end = ' ')
print(mgr1.lastName)
print(mgr1.printEmp())

#We could use methods to check relation of instances and classes
#and also classes and subclasses

print(isinstance(mgr1, Manager))
print(isinstance(mgr1, Employees))
print(isinstance(mgr1, Developer))
print()
print(issubclass(Manager, Employees))
print(issubclass(Developer, Employees))
print(issubclass(Manager, Developer))

#De nada!
