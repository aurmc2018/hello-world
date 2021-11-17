
# Simple Function

def fun1():
    return 5
values = fun1()
print(values)


# Simple Generator

def fun2():
    yield 5
values = fun2()
print(values)
print(values.__next__())

# Simple Iterator

def fun3():
    yield 1
    yield 2
    yield 3
values = fun3()
print(values)
print(values.__next__())
print(values.__next__())
print(values.__next__())

# Print descending squares
def fun4():
    n = 10
    while n > 0:
        sq = n * n
        yield sq
        n -= 1
values = fun4()
print(values)

for i in values:
    print(i)

