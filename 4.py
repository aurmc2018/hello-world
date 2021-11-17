import multiprocessing
import time


start=time.perf_counter()

def print_cube(num):
    print("Cube: {}\n".format(num * num * num))

def print_square(num):
    print("Square {}\n".format(num * num))


def print_multi(begin, end):
    for i in range(begin, end + 1):
        for j in range(begin, end + 1):
            temp = i * j
            print(f'T{i:<4}*{j:4} ={i * j:6}')

if __name__ == "__main__":

    p1 = multiprocessing.Process(target=print_multi, args=(1,1000, ))
    p2 = multiprocessing.Process(target=print_multi, args=(1001,2000 ))
    # p3 = multiprocessing.Process(target=print_multi, args=(2001,3000 ))
    # p4 = multiprocessing.Process(target=print_multi, args=(3001,4000 ))
    # p5 = multiprocessing.Process(target=print_multi, args =(4001,5000, ))


    p1.start()
    p2.start()
    # p3.start()
    # p4.start()
    # p5.start()

    p1.join()
    p2.join()
    # p3.join()
    # p4.join()
    # p5.join()

    print("Done")

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} seconds (s)\n')

