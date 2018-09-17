#The Local, Enclosing, Global, Builtin


#LOCAL AD GLOBAL
x = 'i am global x'

def test():
    y = 'local y'
    x= 'local x'
    print(x)
    print(y)

test()   #will print local x and y
print(y) # will throw error'''

x = 'hello'
def test():
    global x
    x = 'bye'
    print(x)

test()
print(x) #Will print x since it has been declared a global variable '''
#########################################################
    
#BUILT INS

#print(dir(builtins))
def min() #will override the inbuilt func
    pass

print(min([3,4,5,6,7,]))    #throws error due to overide'''
################################################################
#ENCLOSING

def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()   #prints outer then inner'''

def outer():
    x = 'outer x'

    def inner():
        nonlocal x #using global will modify even outside the outer
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()   #prints inner both times

def outOuter():
    x = '1 outer'
    def outer():
        x = 'outer x'

        def inner():
            nonlocal x  #non local only modified variable it is enclosed into
            x = 'inner x'
            print(x)

        inner()
        print(x)
    outer()
    print(x)
outOuter()


x = 'global x'
def outer():
    x = 'outer x'

    def inner():
        global x   #using global here modifies global x not outer x
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
print(x)