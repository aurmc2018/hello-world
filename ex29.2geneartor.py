#PipeLining Generators

def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        #print(x)
        yield x

def square(nums):
    for num in nums:
        #print(num**2)
        yield num**2

print(sum(square(fibonacci_numbers(10))))