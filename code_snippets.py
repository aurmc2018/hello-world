import math

def hello():
    print("Hello, Python")

def print_in_formasts():
    name = "Chandrasekaran"
    age = 100

    # String formatting using concatenation
    print("My name is " + name + ", and I am " + str(age) + " years old.")

    # String formatting using multiple prints
    print("My name is ", end="")
    print(name, end="")
    print(", and I am ", end="")
    print(age, end="")
    print(" years old.")

    # String formatting using join
    print(''.join(["My name is ", name, ", and I am ", str(age), " years old"]))

    # String formatting using modulus operator
    print("My name is %s, and I am %d years old." % (name, age))

    # String formatting using format function with ordered parameters
    print("My name is {}, and I am {} years old".format(name, age))

    # String formatting using format function with named parameters
    print("My name is {n}, and I am {a} years old".format(a=age, n=name))

    # String formatting using f-Strings (Python 3.6+)
    print(f"My name is {name}, and I am {age} years old")

def print_stars():
    line=""
    for i in range(120):
        line += "*"
    print(line)
    
def single_simple_add():
    print('The sum is %.1f' %(float(input('Enter first number: ')) + float(input('Enter second number: '))))

def math_func():
    numbers = (55, 105, 255,25)
    print(min(numbers))
    print(max(numbers))
    element = numbers[3]
    print(pow(element,2))
    element = numbers[3]
    print(pow(element,0.5))

def area_of_triangle():
    side_a = float(input('Enter first side: '))
    side_b = float(input('Enter second side: '))
    side_c = float(input('Enter third side: '))
    # calculate the semi-perimeter
    s = (side_a + side_b + side_c) / 2
    # calculate the area
    area = (s*(s-side_a)*(s-side_b)*(s-side_c)) ** 0.5
    print('The area of the triangle is %0.2f' %area)

def quatratic_solve():
    # Solve the quadratic equation ax**2 + bx + c = 0
    # import complex math module
    import cmath
    a = int(input("Enter for a "))
    b = int(input("Enter for b "))
    c = int(input("Enter for c "))

    # calculate the discriminant
    d = (b ** 2) - (4 * a * c)

    # find two solutions
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)

    print('The solutions are {0} and {1}'.format(sol1, sol2))

def prime_check():
    # Program to check if a number is prime or not
    num = int(input("Enter number tobe checked as prime"))
    flag = False
    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

def fib_print():
    # Program to display the Fibonacci sequence up to n-th term
    nterms = int(input("How many terms? "))

    # first two terms
    n1, n2 = 0, 1
    count = 0

    # check if the number of terms is valid
    if nterms <= 0:
        print("Please enter a positive integer")
    # if there is only one term, return n1
    elif nterms == 1:
        print("Fibonacci sequence upto", nterms, ":")
        print(n1)
    # generate fibonacci sequence
    else:
        print("Fibonacci sequence:")
        str2=""
        while count < nterms:
            # print(n1)
            str2 = str2 + str(n1) +"  "
            print(str2)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1

def is_palindrom():
    a = input("enter sequence")
    b = a[::-1]
    if a == b:
        print("palindrome")
    else:
        print("Not a Palindrome")
def find_factorial():
    num = int(input("Enter a number: "))
    factorial = 1
    # check if the number is negative, positive or zero
    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print("The factorial of", num, "is", factorial)

# Multiplication table (from 1 to 10) in Python
def print_multiplication_table():
    num = int(input("Display multiplication table of? "))
    for i in range(1, 17):
        print("\t\t",num, ' x ', i, '=', num * i)
# dictionary comprehension example
def dict_comprehension():
    square_dict = {num: num * num for num in range(1, 17)}
    print(square_dict)

def f_2_C():
    # Python Program to convert temperature in celsius to fahrenheit
    # change this value for a different result
    celsius = float(input("Enter Celsius toconvert ")) # 37.5
    # calculate fahrenheit
    fahrenheit = (celsius * 1.8) + 32
    print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' % (celsius, fahrenheit))


def km_2_miles():
    # Taking kilometers input from the user
    kilometers = float(input("Enter value in kilometers: "))
    # conversion factor
    conv_fac = 0.621371
    # calculate miles
    miles = kilometers * conv_fac
    print('%0.2f kilometers is equal to %0.2f miles' % (kilometers, miles))

def check_armstrong():
    # Program to check Armstrong numbers in a certain interval
    lower = 100
    upper = 2000
    for num in range(lower, upper + 1):

        # order of number
        order = len(str(num))
        # initialize sum
        sum = 0

        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        if num == sum:
            print(num)

def simple_lambda():
    x = lambda a : a * 10
    print(x(5))

    x = lambda a, b, c: a + b + c
    print(x(150, 160, 20))


import re
def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",lambda mo: mo.group(0)[0].upper() + mo.group(0)[1:].lower(),s)

def simple_map():
   A0 = dict(zip(('annamalai nagar','chidambaram','chennai','delhi','bombay'),(608002,608001,600001,1000001,4000001)))
   A1 = range(10)
   A2 = sorted([i for i in A1 if i in A0])
   A3 = sorted([A0[s] for s in A0])
   A4 = [i for i in A1 if i in A3]
   A5 = [[i, i * i] for i in A1]
   print(A0)
   print(A1)
   print(A2)
   print(A3)
   print(A4)
   print(A5)
def floor_opr():
#The // is a Floor Divisionoperator used for dividing two operands with the result as quotient displaying digits before the decimal point. For instance,
    print(10//5) # return integer without decimal points 2
    print(10.0//5.0)#=print(10/5)=2.0

def list_remove_del_pop():
    list_1 = [1,2,3,4,5,6,7,8,9]
    print("list:             ",list_1)
    # list_1.remove(9)
    # print("After removal:  ", list_1)
    list_1.remove(3)
    print("After removal[3]: ", list_1)
    del list_1[3]
    print("After deleting[3]:",list_1)
    list_1.pop(2)
    print("After poping[2]:  ", list_1)

def swap_case():
    string = "IT IS IN LOWERCASE."
    print(string.swapcase())
    string = "it is in uppercase."
    print(string.swapcase())

def string_strip():
    string3 = "      space stripping   "
    print(string3)
    print(string3.strip())

def string_reverse():
    s = "i love you"
    print(s[::-1])
def string_split():
    a = "Python Is Candy"
    print("Before split  ",a)
    print("After split() ",a.split()) #seperated by space
import random
def shuffle_demo():
    # declare a list
    sample_list1 = ['Z', 'Y', 'X', 'W', 'V', 'U']
    print("Original LIST1: ")
    print(sample_list1)
    ###### first shuffleusing random shuflle function
    random.shuffle(sample_list1)
    print("\nAfter the first shuffle of LIST1: ")
    print(sample_list1)
    # second shuffle
    random.shuffle(sample_list1)
    print("\nAfter the second shuffle of LIST1: ")
    print(sample_list1)


from random import shuffle
def demo_shuffle_v2():
    x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
    print("Before shuffle :",x)
    shuffle(x)
    print("After shuffle  :",x)

def print_unicode():
    unicode_1 = ("\u0123", "\u2665", "\U0001f638", "\u265E", "\u265F", "\u2168","\u2000")
    print(unicode_1)

def file_open():
    with open("art.py", "r") as fp:
        fileData = fp.read()
        # To print the contents of the file
    print(fileData)

def enumerate_demo():
    list_1 = ["I", "Love", "You"]
    s_1 = "I Love You"
    # creating enumerate objects
    object_1 = enumerate(list_1)
    object_2 = enumerate(s_1)

    print("Return type:", type(object_1))
    print(list(enumerate(list_1)))
    print(list(enumerate(s_1)))


import array as arr
def array_list_demo():
    User_Array = arr.array('i', [1, 2, 3, 4])
    User_list = [1, 'abc', 1.20]
    print(User_Array)
    print(User_list)
    print("array operations demo")
    a = arr.array('d', [1.1, 2.1, 3.1])
    print("array            ",a)
    a.append(3.4)
    print("array appended   ",a)
    a.extend([4.5, 6.3, 6.8])
    print("array extended    ",a)
    a.insert(2, 3.8)
    print("array Inserted   ",a)


def demo_init():
    class student_1:
        def __init__(self, name, age, salary):
            self.name = name
            self.age = age
            self.salary = salary

    S_1 = student_1("Annamalai", 62, 25000)
    # S_1 is the instance of class student.
    # __init__ allocates memory for S_1.
    print(S_1.name)
    print(S_1.age)
    print(S_1.salary)


def demo_scope():
    # assigning a variable
    num_global = 100
    # defining a function
    def myfunction():
        # reassigning a variable
        num_global = 200
        # calling the function
    myfunction()
    # printing the value of the variable
    print(num_global) # print only 100 goback to global space

def demo_built_in_data_types():
    num     = 10
    fnum    = 10.0
    cnum    = 10.0+3j
    bool    = True
    str     = "All is well"
    list    = [1,2,3]
    tuple   = (1,2,3)
    set     = {1,2,3}
    dict    = {"1":"one","2": "two","3":"three"}
    print(type(num),num)
    print(type(fnum), fnum)
    print(type(cnum), cnum)
    print(type(bool), bool)
    print(type(str),str)
    print(type(list),list)
    print(type(tuple), tuple)
    print(type(set), set)
    print(type(dict),dict)

def demo_slicing():
    list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    # start = int(input("From which position eg. -1"))
    # end   = int(input("To which position eg. 2"))
    # skip  = int(input("How many chars to be skipped eg.2"))
    print(list)
    print(list[:])
    print(list[2:10]) # until index 4th excluded from index 2 onwards
    print(list[:10])
    print(list[10:])
    print(list[::])
    print(list[2:10:2])
    print(list[-1:])
    print(list[-1:-10])

def demo_print_chart():
    def pyfunc(r):
        for x in range(r):
            print(' ' * (r - x - 1) + '*' * (2 * x + 1))
    pyfunc(60)

def demo_sort_list():
    list = ["1", "4", "0", "6", "9"]
    print("Original list :",list)
    list = [int(i) for i in list]
    list.sort()
    print("Sorted List  :",list)

    alist = ["Appa", "Zeebra", "Apple", "Bannana", "Grapes"]
    print("Original items :", alist)
    alist = [i for i in alist]
    alist.sort()
    print("Sorted items  :", alist)


# Mutable built - in types: Lists,SETS,DICTIONARIES
# Immutable built - in types: Strings,tUPLES, nUMBERS
#hello()
#single_simple_add()
#math_func()
#area_of_triangle()
#quatratic_solve()
#prime_check()
#find_factorial()
#print_multiplication_table()
#dict_comprehension()
#f_2_C()
#km_2_miles()
#check_armstrong()
#print(titlecase(" i love you nayanthara"))
#simple_lambda()
# simple_map()
#floor_opr()
# list_remove_del_pop()
#swap_case()
# string_strip()
# string_reverse()
#shuffle_demo()
# print_unicode()
# file_open()
# enumerate_demo()
# array_list_demo()# array stor similar type elements wheras list store dissimilar type elements
# demo_init()
# demo_scope()
#demo_built_in_data_types()
# demo_shuffle_v2()
# demo_slicing()
# print("a" is 'a') #==
# print(not("a" is 'a'))# false
# string_split()
# monkey_patch()
# demo_print_chart()
# fib_print()
# is_palindrom()
# demo_sort_list()
# print_in_formasts()
print_stars()