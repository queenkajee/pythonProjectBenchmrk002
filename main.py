import math

import numpy
from numpy import random
import datetime


def comment1():
    Rnum1 = random.randint(0, 100)
    Rnum2 = random.randint(0, 100 - Rnum1)
    Rnum3 = random.randint(0, 100 - Rnum2 - Rnum1)
    Rnum4 = 100 - Rnum1 - Rnum2 - Rnum3

    numP1 = Rnum1 / 100
    numP2 = Rnum2 / 100
    numP3 = Rnum3 / 100
    numP4 = Rnum4 / 100


def HDBenchmark():
    f = open("testHDbenchmark.txt", "w")


    sumRand = 0
    probArr = []
    for i in range(0, 3):
        rand = random.randint(0, 100 - sumRand)
        sumRand += rand
        probArr.append(rand / 100)

    probArr.append((100 - sumRand) / 100)

    # declare array num
    numArr = []
    for i in range(0, 4):
        numArr.append(random.randint(0, 100000000))

    arr = random.choice(numArr, p=probArr, size=(100))
    f.write(numpy.array_str(arr))
    f.close()
    f = open("testHDbenchmark.txt", "r")
    f.read()
    f.close()


start1 = datetime.datetime.now()
HDBenchmark()
stop1 = datetime.datetime.now()
timer = stop1 - start1
print(timer)
