import time

start =time.perf_counter()
# for i in range(1, 11):
#     for j in range(1, 11):
#          print(f'{i:<4}*{j:4} ={i*j:6}')

# for i in range(1, 101):
#     for j in range(1, 101):
#          print(f'{i:<4}*{j:4} ={i*j:6}')
#
def multiplication_table(begin, end):
    for i in range(begin, end+1):
        for j in range(begin, end+1):
            print(f'{i:<4}*{j:4} ={i * j:6}')

multiplication_table(1,100)
finish =time.perf_counter()
print(f'Finished in{round(finish-start, 2)}second(s)')









