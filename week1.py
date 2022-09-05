import sys
# print(dir(sys))
import numpy as np
import math
import collections
from collections import Counter
import random

# a1 = np.zeros(5)
#
# a = 1
# b = 2.5
# print('a+b = %d' % (a+b))
# print('a+b = %f' % (a+b))
# print('my name is %s' % ('yang杨'))

# math.pi
# a  = abs(-2)
# a1 = math.ceil(3.4)
# a2 = math.floor(1.2)
# a3 = math.sin(math.pi/2)
# a4 = math.cos(math.pi)
# a5 = math.asin(1)
# num = [1,2,3,5,7] # list--tuple
# a6 = max(num)
# a7 = min(num)
# a8 = math.modf(1.23)  # math.sqrt, pow(2,3), round(1.2345, 2)


# The definition of a function
def cmp(x,y):
    if x < y:
        return(-1)
    elif x == y:
        return(0)
    elif x > y:
        return(1)

print(cmp(2,4))

# Generate random number
b1 = random.choice(range(10))
b2 = random.randrange(0,10)
b3 = random.uniform(1,6)

# for i in range(10):
#     print(i)
#
lis = [1,2,3,4]
random.shuffle(lis)
c2  = random.sample(lis,3)

# dict = ['yes', 'yes, 'no']
# print(collections.Counter(dict))

# generation of sequence and plot
N  = 10
x1 = np.linspace(1,0,10)
x2 = np.arange(1,0,-0.1)
x3 = np.logspace(1,4,4, endpoint= True, base = 2)
x4 = np.logspace(1,5,3, endpoint= True, base = 2)

# import matplotlib.pyplot as plt




brea
