# https://www.runoob.com/python/python-exercise-example1.html
# Python practice 1
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if( i != k) and (i != j) and (j != k):
#                 print(i,j,k)

# Python practice 2
# i = int(input('净利润:'))
# arr = [1000000,600000,400000,200000,100000,0]
# rat = [0.01,0.015,0.03,0.05,0.075,0.1]
# r = 0
# for idx in range(0,6):
#     if i>arr[idx]:
#         r+=(i-arr[idx])*rat[idx]
#         print ((i-arr[idx])*rat[idx])
#         i=arr[idx]
# print (r)

# Python practice 3
# for i in range(1, 85):
#     if 168 % i == 0:
#         j = 168 / i;
#         if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
#             m = (i + j) / 2
#             n = (i - j) / 2
#             x = n * n - 100
#             print(x)

# Python practice 4
# year  = int(input('year:\n'))
# month = int(input('month:\n'))
# day   = int(input('day:\n'))

# print('This year is: %d' % (year))
#
# months = [31,28,31,30,31,30,31,31,30,31,30,31]
# accu   = months
# for i in range(2,12):
#     accu[i-1] = accu[i-2] + months[i-1]
#     # print(accu[i-2])
#     # if(i >= 11): print(accu[i-1])
#
# if 0 < month <= 12:
#     sum = accu[month-1]
# else:
#     print('data error')
#
# sum = sum + day
# leap = 0
# if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
#     leap = 1
# if (leap == 1) and (month > 2):
#     sum = sum + 1
# print('it is the %dth day of the year.' % sum)

# Python practice 5
# l = []
# for i in range(3):
#     x = int(input('number:\n'))
#     l.append(x)
# l.sort()
# print(l)

# Python practice 6 (Fibonacci)
# def fib(n):
#     a,b = 1,1
#     for i in range(n-1):
#         a, b = b, a+b
#     return a
#
# print(fib(3))

# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     return fib(n-1) + fib(n-2)
#
# print(fib(5))

# Python practice 7
# a = [1,2,3]
# b = a[:]
# print(b)

# Python practice 8 (输出乘法口诀表)
# for i in range(1,10):
#     print()
#     for j in range(1,i+1):
#         print('%d*%d=%d' % (j,i,i*j), end=" ")


# Python practice 9(暂停1秒输出)
# import time
#
# temp = {1:'a', 2:'b', 3:'c', 4:'d'}
# for key, value in dict.items(temp):
#     print(key, value)
#     time.sleep(1)

# Python practice 10
# import time
# print(time.localtime(time.time()))
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
# time.sleep(1)
# print(time.strftime('%Y-%M-%d %H:%M:%S', time.localtime(time.time())))
# time.sleep(1)
# print(time.strftime('%Y-%M-%d %H:%M:%S', time.localtime(time.time())))
# time.sleep(1)
# print(time.strftime('%Y-%M-%d %H:%M:%S', time.localtime(time.time())))
# time.sleep(1)
# print(time.strftime('%Y-%M-%d %H:%M:%S', time.localtime(time.time())))
# import sys
# #sys模块提供了一系列有关Python运行环境的变量和函数。
# print(sys.version)
# import platform
# #platform模块给我们提供了很多方法去获取操作系统的信息
# print(platform.python_version())

# Python practice 11 ??????
# f1 = 1
# f2 = 1
# for i in range(1,22):
#     print ('%12ld %12ld' % (f1,f2), end=" ")
#     if (i % 3) == 0:
#         print ('')
#     f1 = f1 + f2
#     f2 = f1 + f2

# Python practice 12 (prime number)
# from math import sqrt
#
# h = 0
# leap = 1
#
# for i in range(101,200):
#     if i % 2 != 0:
#         k = int(sqrt(i))
#         for j in range(2,k+1):
#             if i % j == 0:
#                 leap = 0
#                 break
#         if (leap == 1):
#             h = h + 1
#             print('%-4d' % i)
#             if h % 10 == 0:
#                 print('')
#         leap = 1
# print('The number of total prime number is %d' % h)

# Python practice 13 (水仙花数)
# for m in range(100,1000):
#     i = m//100
#     j = m//10 % 10
#     k = m%10
#     if m == i**3 + j**3 + k**3:
#         print(m)


# Python practice 14 (reducenum)

# def reduceNum(n):
#     print ('{} = '.format(n), end=" ")
#     if not isinstance(n, int) or n <= 0 :
#         print ('请输入一个正确的数字 !')
#         exit(0)
#     elif n in [1] :
#         print ('{}'.format(n))
#     while n not in [1] : # 循环保证递归
#         for index in range(2, n + 1) :
#             if n % index == 0:
#                 n //= index # n 等于 n//index
#                 if n == 1:
#                     print (index )
#                 else : # index 一定是素数
#                     print ('{} *'.format(index), end=" ")
#                 break
# reduceNum(24)
# reduceNum(100)
# reduceNum(-1)
# reduceNum(1)


# Python practice 15

# score = int(input('score input: \n'))
# if score >= 90:
#     grade = 'A'
# elif score >= 60:
#     grade = 'B'
# else:
#     grade = 'C'
#
# print('%d belongs to %s' % (score,grade))


# Python practice 16 (date time)

# import datetime as dt
#
# if __name__ == '__main__':
#     print(dt.date.today().strftime('%d/%m/%y'))
#
#     date1 = dt.date(1995,10,5)
#     print(date1.strftime('%d/%m/%y'))
#
#     date2 = date1 + dt.timedelta(days = 2)
#     print(date2.strftime('%d/%m/%y'))
#
#     date3 = date1.replace(year = date1.year + 1)
#     print(date3.strftime('%d/%m/%y'))
#

# Python practice 17 (字符，汉字，字母等数量统计)
import string

def chcount(str):
    for s in str:
        # 中文字符范围
        if '\u4e00' <= s <= '\u9fff':
            print(s, end=" ")

chcount('中文f1啊234  *(')
# s = input('please input a string:\n')
print(' ')

def count(s):
    ch = let = spa = dig = oth = 0
    for c in s:
        if c in string.ascii_letters:
            let = let + 1
        elif c.isalpha():
            ch = ch + 1
            print(c)
        elif c.isspace():
            spa = spa + 1
        elif c.isdigit():
            dig = dig + 1
        else:
            oth = oth + 1
    print('ch = %d, char = %d, space = %d, digit = %d, others = %d' % (ch,let, spa, dig, oth))

# count('asdf1234  *(')
count('中文f1234  *(')
breakpoint()

# Python practice 18 (R 中 apply 类似函数)
# from functools import reduce
#
def add(x, y):  # 两数相加
    return x + y


# sum1 = reduce(add, [1,2,3,4,5])   # 计算列表和：1+2+3+4+5
# sum2 = reduce(lambda x, y: x+y, [1,2,3,4,5])  # 使用 lambda 匿名函数
# print(sum1)
# print(sum2)

# from functools import reduce
#
# sn = []
# tn = 0
# n  = int(input('n = \n'))
# a  = int(input('a = \n'))
#
# for i in range(n):
#     tn = tn + a
#     a  = a*10
#     sn.append(tn)
#     print(tn)
#
# su = reduce(lambda x,y: x+y, sn)
# print('the sum is: ', su)

# Python practice 19 (R 中 apply 类似函数)
# for i in range(1,100):
#     print(i)
#     if (i%10==0): break
# def add(x,y):
#     return(x+y)
#
from sys import stdout
# from functools import reduce
# #
# def fac(x):
#     if (x <=0 ) or (not isinstance(x,int)):
#         print('please enter a positive integer')
#         exit(0)
#     else:
#         arr = []
#         for i in range(1,x):
#             if (x%i == 0):
#                 arr.append(i)
#     return(arr)
#
# a = fac(20)
# print(reduce(add,a))
#
#
# for j in range(2,1001):
#     s    = 1
#     temp = fac(j)
#     if reduce(add, temp) == j:
#         s = 0
#     if(s == 0):
#         print(j)
#         for i in range(len(temp)):
#             # stdout.write(str(temp[i]))
#             # stdout.write(' ')
#             print(str(temp[i]),end=" ")
#         print(' ')

# breakpoint()

# import sys
# a = 1
# b = 2
# print('打印第 2 到第 5 个元素：', sys.argv[1:5])
# print('打印所有参数：', sys.argv[:])
# for i in sys.argv:
#     print(i)

# for i in range(1,10): print(i)
# print(sys.argv)

# Python practice 20 小球落下弹起

# tour = []
# height = []
#
# hei = 100.0  # 起始高度
# tim = 10  # 次数
#
# for i in range(1, tim + 1):
#     # 从第二次开始，落地时的距离应该是反弹高度乘以2（弹到最高点再落下）
#     if i == 1:
#         tour.append(hei)
#     else:
#         tour.append(2 * hei)
#     hei /= 2
#     height.append(hei)
#
# print('总高度：tour = {0}'.format(sum(tour)))
# print('第10次反弹高度：height = {0}'.format(height[-1]))

# Python practice 21 猴子吃桃
# x2 = 1
# for day in range(9,0,-1):
#     x1 = (x2+1)*2
#     x2 = x1
# print(x1)

# Python practice 22 乒乓球比赛对战表
# for i in range(ord('x'),ord('z') + 1):
#     for j in range(ord('x'),ord('z') + 1):
#         if i != j:
#             for k in range(ord('x'),ord('z') + 1):
#                 if (i != k) and (j != k):
#                     if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
#                         print ('order is a -- %s\t b -- %s\tc--%s' % (chr(i),chr(j),chr(k)))

# Python practice 23 打印菱形图案
# from sys import stdout
# import numpy as np
#
# mat = np.array([[0,0,1,0,0],
#                 [0,1,1,1,0],
#                 [1,1,1,1,1]])
# for i in range(3):
#     for j in range(5):
#         if (mat[i,j] == 0):
#             stdout.write(' ')
#         else:
#             stdout.write('*')
#     print('')

# Python practice 24 (R 中 apply 类似函数)


## For else 使用
# for i in range(3):
#     if (i > 5):
#         break
# else:
#     print("Else Statements")
#
# for i in range(3):
#     if (i > 1):
#         print("Break")
#         break
# else:
#     print("Else Statements")
#
# for i in range(3):
#     if (i > 1):
#         continue
# else:
#     print("Else Statements after Continue")


# a = 15
# lst = [10,5,6,8,9,7,15,11]
# for i in lst:
#     if(i == 15):
#         print("Found")
#         break
# else:
#      print("Not Found Loop Over")
