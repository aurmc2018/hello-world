import datetime

print(1)
print(type(1))

print('one')
print(type('one'))

print(3.14)
print(type(3.14))

print("String '\nNew line '")
print('String "\nNew line ')

x,y, z, a = 5, 3.14,'One',"Two"

print(x)
print(y)


print(z)
print(a)

print(x+y)
print(type(x+y))
print(f'Sum={x+y}')

print('All is Well with Python\n\n\n')


# Percentage (%) demo to format strings
subject = "Data Science"
language = "Python in Tamil"
output_str = 'I am studying %s and using %s as the programming language.' % (subject, language)
print (output_str)



#Variable Name Conventions
#1Camel case  myFirstVariable
#2Pascal Case MyFirstVariable
#3Snake Case my_first_variable


val = 'Rose'
print(f"{val} is a {val} is a {val} is a {val}.\n\n")

name = 'Ram'
age = 20
print(f"Hai, My name is {name} and I'm {age} years old.")


today = datetime.datetime.today()
print(f"{today:%B %d, %Y}\t")
print(f"{datetime.datetime.today():%B %d, %Y}")

print ("{},  you Scream, we all Scream, for ice cream!\n"
                        .format("I Scream"))


print ("This is {} {} {} {}\n"
       .format("one", "two", "three", "four"))

my_string = "{0}, {1}, {2}, {3}\n"
print(my_string.format("one", "two", "three", "four"))


my_string = "{3}, {2}, {1}, {0}\n"
print(my_string.format("one", "two", "three", "four"))


# If one doctor is onedoctors another doctor,
# Then which doctor is doctoring the doctored doctor?
# Does the doctor who doctors the doctor, doctor the doctor the way the doctor he is doctoring doctors?
# Or does he doctor the doctor the way the doctor who doctors doctors?


# Convert base-10 decimal integers
# to floating point numeric constants
print("This site is {0:f}% securely {1}!!\n".
      format(100, "encrypted"))

# To limit the precision
print(" {1:.2f}% is my  {0} average \n"
      .format("semester", 99.234876))

# For no decimal places
print("My average of this {0} was {1:.0f}%\n"
      .format("semester", 99.234876))

# Convert an integer to its hexa, binary, octal bases



print("The {0} of 100 is {1:b}".format("binary", 100))

print("The {0} of 100 is {1:x}".format("hexa", 100))

print("The {0} of 100 is {1:o}\n".format("octal", 100))

# To demonstrate spacing when
# strings are passed as parameters
print("{0:4}, is the computer science portal for {1:8}!"
      .format("Dudes for Dudes", "dudes"))

# To demonstrate spacing when numeric
# constants are passed as parameters.
print("It is {0:5} degrees outside !"
      .format(40))

# To demonstrate both string and numeric
# constants passed as parameters
print("{0:4} was founded in {1:16}!"
      .format("Dude of Dudes", 2019))



print("{:^50s}".format("Geeks"))
print("{:>50s}".format("Geeks"))
print("{:<50s}".format("Geeks"))
print("{:*^50s}".format("Geeks"))




print("{:*^20s}".format("Spacing Demo"))
# To demonstrate aligning of spaces
print("{0:^16} was founded in {1:>4}!".format("Dude of Dudes", 2019))
print("{0:^16} was founded in {1:<4}!".format("Dude of Dudes", 2019))
print("{0:^16} was founded in {1}!".format("Dude of Dudes", 2019))



#class definition to demo Object
class aObject():
    def aObject_method(self):
        return ('All is well again a gain')

print("\n\n\n\n\n")
print(aObject)  # Prints the class:<class '__main__.aObject'>
print()
aInstance = aObject() # << making a class instance
print()
print(aInstance)
print()# Prints the instance:<__main__.aObject object at 0x100bf7588>
print(aInstance.aObject_method()) # prints the instance method: All is well again a gain


# Add a comma :
print('{:,}'.format(1000000))# >> 1,000,000
# Add a comma and display 2 decimal points:
print('${:,.2f}'.format(1000))#>> $1,000.00
# Express percentages with 2 decimal points:
sureness = 80/99
print ('I am sure about this: {:.2%}'.format(sureness))# >> I am sure about this: 80.81%
# Show only 2 decimal places:
floaty = 10.2222222
print('floaty value is {:.2f} '.format(floaty)) #>> floaty value is 10.22
# Round and show 2 decimals:
floaty = 10.2299999
print('floaty value is {0:.2f} '.format(round(floaty,2))) #>> floaty value is 10.23
#----------------------------------
#multiline f string
name = "Trump"
profession = "Businessman"
affilation ="Trump Corporation, US"
msg = (
        f"Hi {name}. " \
        f"You are a {profession}. "\
        f"You were in {affilation}."
 )
print(msg)
#--------------------------------------
#---------------------------------------
# #handling formats using speed comparison ?
# results = [10.22111, 30.33, 40.69999]
# print('\n'.join('Index: {0} Original {1:>10}, Rounded: {1:>.2f}'.format(*k) for k in enumerate(results)))
# for i,result  in enumerate(results):
#     print (f" Index: {i} Original: {result:>10}, Rounded: {result:>.2f}")
# #Tabulation using pipinstall tabulate
# from tabulate import tabulate
# table = [["LexL","SuperMan",0.12],["Joker","HarleyQ",0.22],["Bane","Batman",0.22]]
# headers = ["Villain", "Nemesis", "Success Rate %"]
# print(tabulate(table, headers, tablefmt="fancy_grid", floatfmt=".1f"))
#------------------------------------
#------------------Aiigned Format
# for x in range(1, 11):
#     print('{0:2d} {1:3d} = {2:8d}'.format(x, x*x, x*x*x))
#
# for x in range(1, 11):
#     print('{0:2.2f} {1:3d} = {2:>8.2f}'.format(x, x*x, x*x*x))
#---------------------------------
#Install wkhtmltopdf
# Install Pdfkit >>  pip install pdfkit
# import pdfkit
# from tabulate import tabulate
# table = [["LexL","SuperMan",0.00],["Joker","HarleyQ",0.00],["Bane","Batman",0.00]]
# headers = ["Villain", "Nemesis", "Success Rate %"]
# exportTable = tabulate(table, headers, tablefmt="html", floatfmt=".1f")
# pdfkit.from_string(exportTable, 'Villains.pdf')
#---------------------------------
#VerticalSpacing
print('123456789012345678901234567890')
print(1,2)

print(1)
print(2)

print(1,end="") #No LF
print(2)
print('1','2')
print('1'+'2')
print('123')
print(1,2,3)
print(1,'\n',2,'\n',3)
print(30*'*')
print('123456789012345678901234567890')
print(1,2*'\t',2,2*'\n',3)

#Horizontal Spacing

print('123456789012345678901234567890')
print(1,'\t',2,'\t',3,'\b',4)

