def isEvenCheck():
    try:
        number = int(input("Enter  number you want to check? "))
    except ValueError:
        print("That's not a valid entry.")
        return

    # if number & 1:
    #     print("This is an odd number.")
    # else:
    #     print("This is an even number.")

    if (number %2 == 0):
        print("This is an even number.")
    else:
        print("This is an odd number.")




if __name__ == "__main__":
    isEvenCheck()