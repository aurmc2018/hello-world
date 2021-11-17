#Most Readable 2020,1989

year = int(input("Which year did you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is  a Leap Year")
        else:
            print(f"{year} is Not a Leap Year")
    else:
        print(f"{year} is  a Leap Year")

else:
    print(f"{year} is Not a Leap Year")
