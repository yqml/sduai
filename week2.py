### Week 2(data type： number, string, list, tuple, dictionary)

## Unicode character <--> integer Unicode value
# print(ord('a'))
# print(chr(97))

# String
# a = 'Hello'
# b = 'world'

# print(a+b)
# print(a*2)
# print(a[1])
# print(a[1:4])

# print('H' in a)
# print('h' in a)

# print('my name is %s' % ('啊'))

## List
# 新建一个list
# lis = []
# print(lis)
# lis.append([1,2])
# print(lis)
#
# lis = []
# lis.extend([1,2])
# print(lis)

# list1,2,3分别为字符串+数字，纯数字，纯字符串的list
# list1 = ['physics', 'chemistry', 1997, 2000]
# list2 = [1,2,3,4,5]
# list3 = ['a','b','c','d']

# 在for循环中使用list
# for x in list1:
#     print(x)

# 在list中截取特定位置的元素
# ind = [0,2,3]
# for i in ind:
#     print(list2[i])

# print(list2[1])
# print(list2[1:5])
# print(len(list2))

# print(list1 + list2)
# print(3 in list2)
# print(0 in list2)

# print(list2[1:])
# print(list2[-1])
# print(list2[-2])
# print(list2[-6])

## List .reverse(), .append(), .extend(), .count(), .index(), .sort() 函数使用
# .reverse()
# row = [1,2,'a','b',3]
# row[4] = 5
# print(row)
# row.reverse()
# print(row)

# subsection and .extend()函数使用
# row = [1,2,'a','b',3]
# # print(row[:2])
# redu = row[:2]
# print(redu)

# print(row[3:])
# redu.extend(row[3:])
# print(redu)

# row = [1,2,'a','b',3]
# del row[2]
# print(row)

# .append(), .count(), .index()函数使用
# row = [1,2,'a','b',3]
# res = []
# # print(res)
# res.append(row)
# print(res)
# print(res[0])
# print(res[0][2])

# extend and append difference,结合上面这一块.append部分对比着看
# row = [1,2,'a','b',3]
# res = []
# res.extend(row)
# print(res)

# append 也可以放在非空list里面 For 彭定康’s question thumbup for you~!!!
# lis1 = [[1,2]]
# print(lis1)
# lis1.append([3,4,5])
# print(lis1)
# # 对比一下
# lis2 = [1,2]
# lis2.append([3,4,5])
# print(lis2)

# .count(), .index()
# row = [1,2,'a','b',3]
# print(row.count('b'))
# print(row.count('c'))
# print(row.index('b'))
# print(row.index('c')) ## this is a wrong sentence.

## Homework:
# 0. 搞懂上面所有code~！！！
# 1. 写一个程序，判定一个数字为奇数、偶数（x对2做除法，判定余数是0还是1）
# 2. 写一个函数，判定一个数字是否为质数
# 3. 写一个程序，输出1-100之间的质数（for x in range(101): 使用2中的函数判定，是质数就输出出来。）
# Homework 命名规则： Group1-name-hw1.py


# breakpoint()