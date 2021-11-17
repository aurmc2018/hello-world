import time

start =time.perf_counter()
def multiplication_table(begin, end):
    for i in range(begin, end+1):
        for j in range(begin, end+1):
            #temp = i * j
            print(f'{i:<4}*{j:4} ={i * j:6}')

multiplication_table(1,5000)

finish =time.perf_counter()
print(f'\nFinished in {round(finish-start, 2)}second(s)')
