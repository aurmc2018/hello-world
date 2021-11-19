# demo for difference between copy and deep copy

import copy

old_list = [[1,2,3,4],5,6,7,8]

def refe():
    old_list = [[1, 2, 3, 4], 5, 6, 7, 8]
    new_list = old_list

    old_list[0][0] = 'c'

    print("old_list    ",old_list,"\told list id ",id(old_list))
    print("new_list    ",new_list,"\tnew_list_id ",id(new_list))

    print("Check values are changed in both lists and ids are same;")

def demoCopy():
    old_list = [[1, 2, 3, 4], 5, 6, 7, 8]
    new_list_copy = copy.copy(old_list)

    new_list_copy[0][0] = 'c'

    print("old_list    ", old_list, "\told list id ", id(old_list))
    print("new_list_copy",new_list_copy,"\tew_list_copy", id(new_list_copy))

    print("Check above values are changed in both lists and ids are different")

def demoDeepCopy():
    old_list = [[1, 2, 3, 4], 5, 6, 7, 8]
    new_list_deepcopy = copy.deepcopy(old_list)
    new_list_deepcopy[0][0] = 'c'

    print("old_list         ", old_list, "\told list id ", id(old_list))
    print("new_list_deepcopy", new_list_deepcopy,"\tew_list_deepcopy_id", id(new_list_deepcopy))

    print("Check above values in the \nold_list are not changed \nnew_list changed \nand ids are changed")


refe()
print(20*'*')
demoCopy()
print(20*'*')
demoDeepCopy()