# -- coding:utf-8 --

numbers = []
def getArray(num):
    i = 0
    while i < num:
        print "At the top i is %d " % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d " % i


getArray(10)




print "The numbers: "
for num in numbers:
    print num, " ",
