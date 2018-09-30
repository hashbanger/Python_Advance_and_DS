import sqlite3

conn = sqlite3.connect('employee.db')

c = conn.cursor()

c.execute('''CREATE TABLE employee(
            fName text,
            lName text,
            pay integer
                        )''')

c.execute(''' INSERT INTO employee VALUES('Prashant','Brahmbhatt', 90000 )''')
c.execute(''' INSERT INTO employee VALUES('Bruce','Springsteen', 40000 )''')

c.execute("SELECT * FROM employee WHERE fName = 'Prashant' ")

# print(c.fetchone())
# print(c.fetchmany(5))
print(c.fetchall())    #To fetch al the rows of the result

conn.commit() #To commit the changes
conn.close() #To close the connection
#------------------------------------------------------------------------------------------------------------------------------
#Now using objects and classes data for the database

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        self.email = self.first+ "."+self.last + "@outlook.com"

    @property
    def fullname(self):
        self.fullname = self.first+ " "+self.last
    
    def __repr__(self):
        return "Employee({}, {}, {})".format(self.first, self.last, self.pay)

conn = sqlite3.connect(':memory:')
#putting memory allows us to start fresh and not commit to any physical database
# very handy for testing purposes

c = conn.cursor()

c.execute('''CREATE TABLE employee(
            fName text,
            lName text,
            pay integer
                        )''')

emp1 = Employee('John','Doe', 10000)
emp2 = Employee('Jane','Doe', 6000)

c.execute("INSERT INTO employee VALUES(?, ?, ?)", (emp1.first, emp2.last, emp1.pay)) 
#Even if there's a single value, you still need to put it in a tuple

#Another morereadable way is through a dictionary
c.execute("INSERT INTO employee VALUES(:first, :last, :pay)", {'first': emp2.first, 'last': emp2.last, 'pay':emp2.pay})

c.execute("SELECT * FROM employee WHERE fName = ?", ('John',))
print(c.fetchall())

#A More readable form
c.execute("SELECT * FROM employee WHERE lName = :last",{'last':'Doe'})
print(c.fetchall())

conn.commit() #To commit the changes
conn.close() #To close the connection
#----------------------------------------------------------------------------------------------------------------
#Putting it all together

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        self.email = self.first+ "."+self.last + "@outlook.com"

    @property
    def fullname(self):
        self.fullname = self.first+ " "+self.last
    
    def __repr__(self):
        return "Employee({}, {}, {})".format(self.first, self.last, self.pay)

conn = sqlite3.connect(':memory:')
#putting memory allows us to start fresh and not commit to any physical database
# very handy for testing purposes

c = conn.cursor()

c.execute('''CREATE TABLE employee(
            fName text,
            lName text,
            pay integer
                        )''')

def insert_emp(emp):
    with conn:  #Using with eradicates the nned to commit each query
        c.execute("INSERT  INTO employee VALUES (:first, :last, :pay)",{'first': emp.first, 'last': emp.last, 'pay': emp.pay})
        
def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employee WHERE lName = :last",{'last': lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employee SET pay = :pay
                     WHERE fName= :first AND lName= :last""",{'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE FROM employee WHERE fNAME = :first AND lName = :last",{'first': emp.first, 'last': emp.last})


emp1 = Employee('John','Doe', 10000)
emp2 = Employee('Jane','Doe', 6000)

insert_emp(emp1)
insert_emp(emp2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp1, 12000)
remove_emp(emp1)

emps = get_emps_by_name('Doe')
print(emps)

conn.close() #To close the connection
