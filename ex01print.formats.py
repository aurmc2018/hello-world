# print formatting

#
# print("print(5)         =>            ",5)
# print("print(type))        ",(type(5))   )
# print()
#
# print("print(5.0)       =>            ",5.0)
# print("print(type(5.0)) => ",(type(5.0))   )
# print()
#
# print("print(5+3j)       =>            ",5+3j)
# print("print(type(5+3j)) => ",(type(5+3j)))
# print()
#
# print("print(True)       =>            ",True)
# print("print(type(True)) => ",(type(True)))
# print()
#
# print("print('5')        =>            ",'5')
# print("print(type('5'))  => ",type('5'))
# print()
#
# print("print(\"5\")        =>            ","5")
# print("print(type(\"5\"))  => ",type("5"))
# print()
#
# print("print('9\'o clock')       => ",'9\'o clock')
# print("print(type(9\'o clock'))  => ",type('9\'o clock'))
# print()

# #---------------------------------------
# # To precision
print(" {1}% is my  {0} average     \n".format("semester", 99.234876))
print(" {1:.0f}% is my  {0} average \n".format("semester", 99.234876))
print(" {1:0.0f}% is my  {0} average \n".format("semester", 99.234876))
print(" {1:.2f}% is my  {0} average \n".format("semester", 99.234876))
print(" {1:.16f}% is my  {0} average\n".format("semester", 99.234876))
print(" {1:10.2f}% is my  {0} average \n".format("semester", 99))
print(" {1:10.2f}% is my  {0} average \n".format("semester", 99.234876))
print(" {1:10.2f}% is my  {0} average \n".format("semester", 999.234876))
print(" {1:10.2f}% is my  {0} average \n".format("semester", 9999.234876))



#------------------------------
# class aObject():
#     def aObject_method(self):
#         return ('All is well again a gain')
#
# print("\n\n\n\n\n")
# print(aObject)  # Prints the class:<class '__main__.aObject'>
# print()
#
# aInstance = aObject() # << making a class instance
# print()
#
# print(aInstance)
#
# print()# Prints the instance:<__main__.aObject object at 0x100bf7588>
# print(aInstance.aObject_method()) # prints the instance method: All is well again a gain


print("{:^50s}".format("Geeks^Centered"))
print("{:>50s}".format("Geeks>Right"))
print("{:<50s}".format("Geeks<Left"))
print("{:*^50s}".format("*Geeks"))
print("{:^50.1}".format("*Geeks"))
print("{:^50.2s}".format("*Geeks"))
print("{:^50.3s}".format("*Geeks"))
print("{:^50.4s}".format("*Geeks"))
print("{:^50.5s}".format("*Geeks"))
print("{:^50.6s}".format("*Geeks"))
print("{:^50.7s}".format("*Geeks"))
print()
print("{:^50.10s}".format("*Geeks"))
print("{0:4} was founded in {1:16}!".format("Dude of Dudes", 2019))
