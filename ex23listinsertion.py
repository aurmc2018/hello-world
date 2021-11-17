#
# my_list = []
# print(my_list)
#
# my_list[:] = "Hello" # ['H', 'e', 'l', 'l', 'o']
# print(my_list)
#
# my_list[:] = (1, 2, 3) # [1, 2, 3]
# print(my_list)
#
# my_list[:] = (i for i in range(5)) # [0, 1, 2, 3, 4]
# print(my_list)
#
# my_list = [1, 2, 3, 4]
# my_list[:2] = [6, 7, 8, 9] # [6, 7, 8, 9, 3, 4]
# print(my_list)
#
# my_list = [1, 2, 3, 4]
# my_list[:0] = [0] # [0, 1, 2, 3, 4]
# print(my_list)
#
# # Statically defined list
# my_list = [2, 5, 6]
# print(my_list)
#
# # Appending using slice assignment
# my_list[len(my_list):] = [5]  # [2, 5, 6, 5]
# print(my_list)
#
# # Appending using append()
# my_list.append(9)  # [2, 5, 6, 5, 9]
# print(my_list)
#
# # Appending using extend()
# my_list.extend([-4])  # [2, 5, 6, 5, 9, -4]
# print(my_list)
#
# # Appending using insert()
# my_list.insert(len(my_list), 3)  # [2, 5, 6, 5, 9, -4, 3]
# print(my_list)
#
# my_list = []
# my_list.append(5)
# print(my_list)
#
#
# my_list = []
# for i in range(10): # using for loop
#     my_list.append(i)
# print(my_list)
#
# my_list = [i for i in range(10)] # List comprehension
# print(my_list)
#
#
# my_list = [3, 2]
# my_list.extend([5, 17, 8])
# print(my_list)
#
# my_list = []
# my_list.insert(0, 5)
# print(my_list)
#
#
# my_list = [2, 5, 7]
# my_list.insert(1, 6) # [2, 6, 5, 7]
#
# my_list = [2, 5, 7]
# my_list.insert(-1, 9)  # [2, 5, 9, 7]
#
# my_list = [4, 5, 6]
# my_list.insert(1, [9, 10])  # [4, [9, 10], 5, 6]

my_list = ['red', 'blue', 'green']
# Get the last item with brute force using len
last_item = my_list[len(my_list) - 1]
# Remove the last item from the list using pop
last_item = my_list.pop()
# Get the last item using negative indices *preferred & quickest method*
last_item = my_list[-1]
# Get the last item using iterable unpacking
*_, last_item = my_list

my_list = list()
# Check if a list is empty by its length
if len(my_list) == 0:
    pass  # the list is empty
# Check if a list is empty by direct comparison (only works for lists)
if my_list == []:
    pass  # the list is empty
# Check if a list is empty by its type flexibility **preferred method**
if not my_list:
    pass  # the list is empty

my_list = [27, 13, -11, 60, 39, 15]
print(my_list)
# Clone a list by brute force
my_duplicate_list = [item for item in my_list]
print(my_duplicate_list)
# Clone a list with a slice
my_duplicate_list = my_list[:]
# Clone a list with the list constructor
my_duplicate_list = list(my_list)
# Clone a list with the copy function (Python 3.3+)
my_duplicate_list = my_list.copy()  # preferred method
# Clone a list with the copy package
import copy
my_duplicate_list = copy.copy(my_list)
my_deep_duplicate_list = copy.deepcopy(my_list)
# Clone a list with multiplication?
my_duplicate_list = my_list * 1  # do not do this
#----------------------------
ethernet_devices = [1, [7], [2], [8374163], [84302738]]
usb_devices = [1, [7], [1], [2314567], [0]]
# The long way
all_devices = [
    ethernet_devices[0] + usb_devices[0],
    ethernet_devices[1] + usb_devices[1],
    ethernet_devices[2] + usb_devices[2],
    ethernet_devices[3] + usb_devices[3],
    ethernet_devices[4] + usb_devices[4]
]
# Some comprehension magic
all_devices = [x + y for x, y in zip(ethernet_devices, usb_devices)]
# Let's use maps
import operator
all_devices = list(map(operator.add, ethernet_devices, usb_devices))
# We can't forget our favorite computation library
# import numpy as np
# all_devices = np.add(ethernet_devices, usb_devices)


print(all_devices)



#---------------------------------

import timeit

setup = """
empty_list = []
small_list = [1, 2, 3, 4]
large_list = [i for i in range(100000)]
"""
static_list_empty = "empty_list = []"
static_list_small = "small_list = [1, 2, 3, 4, 5]"
slice_assignment_empty = "empty_list[len(empty_list):] = [5]"
slice_assignment_small = "small_list[len(small_list):] = [5]"
slice_assignment_large = "large_list[len(large_list):] = [5]"
append_empty = "empty_list.append(5)"
append_small = "small_list.append(5)"
append_large = "large_list.append(5)"
extend_empty = "empty_list.extend([5])"
extend_small = "small_list.extend([5])"
extend_large = "large_list.extend([5])"
insert_empty = "empty_list.insert(len(empty_list), 5)"
insert_small = "small_list.insert(len(small_list), 5)"
insert_large = "large_list.insert(len(large_list), 5)"
print(min(timeit.repeat(setup=setup, stmt=static_list_small)))       #    0.12127927399999999
print(min(timeit.repeat(setup=setup, stmt=slice_assignment_small)))  #    0.3461924679999999
print(min(timeit.repeat(setup=setup, stmt=append_small)))             #    0.14637942200000031
print(min(timeit.repeat(setup=setup, stmt=extend_small)))             #   0.20429766299999974
print(min(timeit.repeat(setup=setup, stmt=insert_small)))             #    0.337170274
