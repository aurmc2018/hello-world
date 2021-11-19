                # class TopTenList:
                #
                #     def __init__(self):
                #         self.num = 1
                #
                #     def __iter__(self):
                #         return self
                #
                #     def __next__(self):
                #
                #         if self.num < 11:
                #             val = self.num
                #             self.num += 1
                #
                #             return val
                #         else:
                #             raise StopIteration
                #
                # values =TopTenList()
                # print(next(values))
                #
                # for i in values:
                #     print(i)

            # def trycatchelsefinallyDemo():
            #     # The try block will raise an error when trying to write to a read-only file:
            #
            #     try:
            #         f = open("alpha.txt") #
            #         try:
            #             f.write("abcdefghijklmnopqrstuvwxyz")
            #         except:
            #             print("Something went wrong when writing to the file")
            #         finally:
            #             f.close()
            #     except:
            #         print("Something went wrong when opening the file")
            #
            # trycatchelsefinallyDemo()


def iterAteSimple():

    numList = [1,2,3,4,5]
    # for i in numList:
    #     print(i,type(i))


    it = iter(numList)
    print(it)

    print(next(it))
    print(next(it))
    print(it.__next__())
    print(it.__next__())
    print(next(it))
    #next(it)# raise an error since 5 elements


def iterateRaiseError():
    numList = [1, 2, 3, 4, 5]
    # for i in numList:
    #     print(i,type(i))

    itobject = iter(numList)
    #print(itobject)

    while True:
        try:
            # get the next item
            print(next(itobject))
            # do something with element
        except StopIteration:
            # if StopIteration is raised, break from loop
            break

# iterAteSimple()
# iterateRaiseError()