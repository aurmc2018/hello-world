year = int(input("Which year do you want to check? "))
isLeapYear = False

if year % 4 == 0:
    isLeapYear = True
    if year % 100 == 0:
        if year % 400 == 0:
            isLeapYear = True
        else:
            isLeapYear = False

print(f'{"Leap year." if isLeapYear else "Not leap year."}')