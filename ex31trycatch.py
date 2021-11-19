
def simple():
    a = 5
    b = 4
    print(a/b)


def tryError():
   a = 5
   b = 0
   print(a/b)


def handleError():
    a = 5
    b = 0
    try:
       print(a/b)
    except:
        print("Some Error")
    print("Bye")

def throwhandleError():
    a = 5
    b = 0
    try:
       print(a/b)
    except Exception as e:
        print("Error:",e)
    print("Bye")


def synError():
    print(x)


def except_block_on_Error():
    try:
        print(10)
        print(x)
    except:
        print("except block on error")



def throwsynNameError():
    try:
        print(x)
    except Exception as e:
        print("error name",e)

def trycatchElse():
    try:
        print("Elon Musk")
        #print(ElonMuskISnotHERE)
    except:
        print("Something will go wrong")
    else:
        print("Nothing will go wrong")


def trycatchElseFinally():
    try:
        print("Elon Musk")
        #print(ElonMuskISnotHERE)
    except:
        print("Except Block")
    else:
        print("Else Block ")
    finally:
        print("Finally Block ")


def tryexceptFinally():
    try:
        print(x)
    except Exception as e:
        print("error block throwing Exception",e)
    finally:
        print("finally Block")


def raiseException():
    x = 10
    if x > 9:
       raise Exception("x is >9")
    # x="0"
    # print(type(x))
    # if not type(x) is int:
    #     raise TypeError("x is not integer......")



simple()
print(20*'-')

#tryError()         #-> Division by zero error

handleError()         #->Syntax Error
print(20*'-')

throwhandleError() #-> Exception name
print(20*'-')

#synError()

except_block_on_Error()
print(20*'-')

throwsynNameError()#-> Throw System exception name
print(20*'-')

tryexceptFinally()
print(20*'-')

trycatchElse()
print(20*'-')

raiseException()
print("Done!!!! Super simple ?!")



