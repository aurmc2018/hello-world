from art_calculator import logo

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
def mod(n1,n2):
    return n1%n2
def exp(n1,n2):
    return n1 ** n2

arithmetic_operations ={
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }
print(logo)
def calculator():
    n1 = int(input("Enter First Number"))
    for symbol in arithmetic_operations:
        print(symbol)


        should_continue = True
    while should_continue:
        operation_symbol = input("pick the arithmetic operator")
        n2 = int(input("Enter next Number"))
        calculation_function = arithmetic_operations[operation_symbol]
        answer = calculation_function(n1,n2)
        print(f"{n1} {operation_symbol} {n2} = {answer}")

        calc_further=input(f" Type 'y' to continue for more calculation with {answer} or 'c' to start a new calculation or 'q' to quit")
        if calc_further == 'y':
            n1 = answer
        elif calc_further == 'c':
            calculator()
        else:
            should_continue = False


calculator()


