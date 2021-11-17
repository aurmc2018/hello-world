name1 = input("Enter Husband Name   ").lower()
name2 = input("enter Wife's Name    ").lower()

# name1.count('t')
# name2.count('t')
#
# name1.count('r')
# name2.count('r')
#
# name1.count('u')
# name2.count('u')
#
# name1.count('e')
# name2.count('e')
#
# name1.count('l')
# name2.count('l')
#
# name1.count('o')
# name2.count('o')
#
# name1.count('v')
# name2.count('v')
#
# name1.count('e')
# name2.count('e')

Total_TRUE = name1.count('t') + name2.count('t') + name1.count('r') + name2.count('r') + name1.count('u') + name2.count('u') + name1.count('e') + name2.count('e')
A = str(int(Total_TRUE))

Total_LOVE = name1.count('l') + name2.count('l') + name1.count('o') + name2.count('o') + name1.count('v') + name2.count('v') + name1.count('e') + name2.count('e')
B = str(int(Total_LOVE))

score = int(A + B)

# if score <= 40:
#     print(f" Your score is {score}, you are alright together.")
# elif score <= 50:
#         print(f" Your score is {score}, you are alright together.")
# elif score < 10 or score > 90:
#         print(f" Your score is {score}, you go together like coke and mentos.")
# else:
#     print(f" Your score is {score}.")

if  score < 10 or score >90:
    print(f"Your score is{score}%, you go together like coke and mentos.")
elif score >40 and score < 50:
    print(f"Your score is {score}%, you are alright together")
else:
    print(f"Your score is {score}% Compatible")
