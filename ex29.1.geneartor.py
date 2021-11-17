#------------------------WhyGenerator----
## x=[i**2 for i in range(1000000000000000)]
## print(x)
## for exp in x:
##    print(exp)
## Above code will give memory error
## Below code won't give error

# def gen(n):
#     for i in range(n):
#         yield i**2
# g=gen(1000000000000000)
# # for i in g:
# #     print(i)
#
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
#------------------------------------
# import sys
# def gen(n):
#     for i in range(n):
#         yield i**2
#
# x = [i ** 2 for i in range(100000)]
# g = gen(100000)
# print(sys.getsizeof(x))
# print(sys.getsizeof(g))
#
# x = [i ** 2 for i in range(10000000)]
# g = gen(10000000)
# print(sys.getsizeof(x))
# print(sys.getsizeof(g))
#
# #x = [i ** 2 for i in range(10000000000)] # Memory Error
# g = gen(10000000000)
# #print(sys.getsizeof(x))
# print(sys.getsizeof(g))

#----------------------------------
# def gen(n):
#     for i in range(1000000):
#         yield 1
#         yield 10
#         yield 1000
#         yield 10000
#
# g = gen(10)
# for i in range(len(g)):
#     print(i)

#-----------------------------
def sum(a,b):
    return a+b
    print("After Return")
# print(sum(10,20))

def iter(no):
    for i in range (no):
        return i
        print("After iter Return")
# print(iter(5))

def iter(no):
    for i in range (no):
        yield i
        print(f"After iter yield {i}")
print(iter(3))
print(list(iter(3)))
count = iter(3)
print(next(count))

######################

def squares(number):
    squared = []
    for i in range(len(number)):
        squared.append(number[i]**2)
    return squared
print(squares([2,3,4,5,16,30]))
print(25*'*')

def squares_yield(number):
    # squared =[]
    for i in range(len(number)):
    # squared.append(number[i]**2)
        yield number[i]**2
        print('Y')
print(list(squares_yield([2,3,4,5,16,30])))



