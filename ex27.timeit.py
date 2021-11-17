#    # Syntax timeit.timeit(stmt, setup,timer, number)

# def checktimit():
#     import timeit
#     # print(timeit.timeit(("RMC")))
#     print(timeit.timeit('output = 100'))
#     print(timeit.timeit('output = 100*100'))
#     print(timeit.timeit('output = 100*100*100'))
#     print("The time taken is ",timeit.timeit(stmt='a=10;b=10;sum=a+b'))
#     print("The time taken is ",timeit.timeit(stmt='a=10;b=10;sum=a*b'))
#     print("The time taken is ",timeit.timeit(stmt='a=10;b=10;sum=a/b'))
#     # print("The time taken is ",timeit.timeit(stmt='a=10;b=10;sum=a//b'))
#     print("The time taken is ",timeit.timeit(stmt='a=10;b=10;sum=a%b'))
# checktimit()


# import timeit
# import_module = "import random"
# testcode = '''
# def test():
#     return random.randint(10, 100)
# '''
# print(timeit.timeit(stmt=testcode, setup=import_module))
# print(timeit.repeat(stmt=testcode, setup=import_module))
#
#
# import timeit
# testcode = "print(random.randint(10,100))"
# import_module = "import random"
# print(timeit.timeit(stmt=testcode, setup=import_module))
#
#
# ###testing timeit deafault_timer()
# import timeit
# import random
#
# def test():
#     return random.randint(10, 100)
#
# starttime = timeit.default_timer()
# print("The start time is  :", starttime)
# test()
# endtime = timeit.default_timer()
# print("The end time is    :", endtime)
# print("Time difference is : {:.9f}".format(endtime - starttime))
#
#

# stmt='a=10;b=10;sum=a+b'
import timeit

import timeit

def testformats():
    subject  = "Data Science"
    language = "Python"
    year     = 2021
    f1 = 'Format 1.Studying %s using %s as the programming language in %s.' % (subject, language,year)
    print(f1)
    f2 =f'Format 2.Studying {subject} using {language} as the programming language in {year}'
    print(f2)
    f3 ='Format 3.Studying {} using {} as the programming language in {}'.format(subject,language,year)
    print(f3)

testformats()
print(timeit.timeit())
print(timeit.timeit('x=5;y=10;sum=x+y'))




#f-STRINGS ARE FASTER THAN BOTH %-FORMATTING AND STR.FORMAT()
# Speed comparison
# t1 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000) #()
# t2 = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000) #[]
# t3 = timeit.timeit('"-".join(map(str, range(100)))', number=10000)#map
# t4 = timeit.timeit(lambda: "-".join(map(str, range(100))), number=10000)
# print(f"Using\n\tstr    = {t1}\n\tlist   = {t2}\n\tmap    = {t3}\n\tlambda = {t4}")


# def testit():
#     """Do nothing test function"""
#     L = [i for i in range(100)]
#
# if __name__ == '__main__':
#     import timeit
#     print(timeit.timeit("testit()", setup="from __main__ import test"))

# import timeit
# import_module = "import random"
# testcode = '''
# def test():
#     return random.randint(10, 100)
# '''
# print(timeit.repeat(stmt=testcode, setup=import_module))

# Install wkhtmltopdf
# Install Pdfkit >>  pip install pdfkit

#print(timeit.timeit(stmt='',setup='',timer='time.perf_counter',number='1',globals=None))

print(timeit.timeit(stmt='',setup='',timer='time.perf_counter',number='1',globals=None))

