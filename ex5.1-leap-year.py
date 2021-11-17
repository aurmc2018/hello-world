# Print leap/Not and Reasons


year =int(input("Which year do you want to check  "))

#2020,2000, 1989

if year % 4 == 0 and year % 100 > 0 or year % 100 == 0 and year % 400 == 0:

    print("Leap year.")

    if year % 4 == 0 and year % 100 > 0:

      print(f"Because {year} is divisible by 4")

      print(f"and {year} is not divisible by 100")

    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:

      print(f"Because {year} is divisible by 4")

      print(f"And {year} is divisible by 100")

      print(f"And {year} is divisible by 400")

else:

    print("Normal year.")

    print(f"Because {year} is NOT divisible by 4")