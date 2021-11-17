# Simple function
def greet():
    print("1. Have a good day Ramasamy Sanjay!")
greet()
print(greet())

# Function with parameters---------------------------

def greetp(fname,lname):
    print(f'2. Have a good day, {lname} {fname}! ')
greetp('Sanjay','Ramasamy')

#Function with return-----------------------------

def get_greetp(fname,lname):
    return(f'3. Have a good day, {lname} {fname}! ')
msg = get_greetp('Sanjay','Ramasamy')
print(msg)

# To introduce default and variable no.of parameters-----------------------------

def add(n1,n2):
    return n1+n2
x=add(100,100)
print(x)

#-----------------------------

def add1(n1,by=1):
    return n1+by
x=add1(100)
print(x)
x=add1(100,300)
print(x)

#-----------------------------

def add2(*n):
    print(n)
print(add2(1,2,3,4,5))

def add3(*n):
    sum = 0
    for i in n:
        sum += i
    return sum   # Note indentation
print(add3(1,2,3,4,5))

#T0 introduce a key value pair | keyword  arguments-------------------

def save_data(**data):   # MULTIPLE PARAMETERS
    print(data)  # dictionary
    print(*data)  # keywords
    print(data["name"]) # key-value pair
#print(save_data)
save_data(id=1,name='rmc')    #MULTIPLE ARGUMENTS

#Scope local/global #-----------------------------
msg ='Global '
def wish(name):
    localmsg = 'Thara Local'
    print(f'{localmsg} {name} {msg}')
wish("VSP")

def wish1(name):
    localmsg = 'Thara Local Local'
    print(f'{localmsg} {name} {msg}')
wish1("VSP")

#-----------------------------
msg ='Global Message'
def wish():
    msg = 'Local Message'
wish()
print(msg)

msg ='Global Message '
def wish():
    global msg
    msg = 'Local Message'  # Changing global variable in function is not a good practice
wish()
print(msg)


#-----------------------------
def fizzbuzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if (input % 3 == 0):
        return "Fizz"
    if (input % 5 == 0):
        return "Buzz"
    return input
print(fizzbuzz(3))
print(fizzbuzz(5))
print(fizzbuzz(15))
print(fizzbuzz(8))
print(fizzbuzz(2))

#Clear screen
import os
clear = lambda: os.system('cls')
clear()
#-----------------------------------





