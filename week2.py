### Week 2(data type： number, string, list, tuple, dictionary)

## Unicode character <--> integer Unicode value
# print(ord('a'));print(ord('b'));print(ord('c'));
# print(chr(97));print(chr(98));print(chr(99));

## String
# a = 'Hello'
# b = 'world'

## 逐行运行并查看结果
# print(a+b)
# print(a*2)
# print(a[1])
# print(a[1:4]) # 左闭右开原则
# print("H" in a)
# print("h" in a)
# print('my name is %s and weight is %d kg' % ('someone', 65))

## List
# 新建一个list
# lis = []
# lis.append([1,2])
# print(lis)
# lis.append()


# list1,2,3分别为字符串+数字，纯数字，纯字符串的list
# list1 = ['physics', 'chemistry', 1997, 2000]
# list2 = [1, 2, 3, 4, 5 ]
# list3 = ["a", "b", "c", "d"]

# 在for循环中使用list
# for x in list3: # x将遍历整个list3
#   print(x)

# 在list中截取特定位置的元素
# ind = [0,2,3]
# for i in ind:
#     print(list2[i])

# print(list1[1])
# print(list2[1:5])
# print(len(list1))
# print(list1 + list2)
# print(3 in list2)
# print(list1[1]); print(list1[-1]); print(list1[1:])

## List .reverse(), .append(), .extend(), .count(), .index(), .sort() 函数使用

# .reverse()函数使用
# row  = [1,2,'a','b',3]
# row[4] = 5
# print(row)
# row.reverse()
# print(row)

# subsection and .extend()函数使用
# row  = [1,2,'a','b',3]
# print(row[:2])
# redu = row[:2] #取row的第0位，第1位元素，左闭右开，第2位元素取不到
# print(row[3:])
# redu.extend(row[3:]) # 在redu中添加row第3位及其后面所有元素
# print(redu)

# .append(), .count(), .index()函数使用
# row  = [1,2,'a','b',3]
# res  = []
# print(res)
# res.append(row) # 在res这个list中添加row
# print(res)
# print(res[0])
#
# temp = res[0] # 一定要看清楚这里res和res[0]的区别
# print(temp.count('b'))
# print(temp.index('b'))

# .sort()函数使用
# rows = [2,4,21,1]
# print(rows)
# rows.sort() #.后的函数代表了针对前面变量的一个具体运算，原变量名称不变。
# print(rows)

# breakpoint()

## Tuples
# tup1 = ('physics', 'chemistry', 1997, 2000)
# tup2 = (1, 2, 3, 4, 5 )
# tup3 = ("a", "b", "c", "d")

# row  = [1,2,'a','b',3]
# row[4] = 5
# print(row)
# tup1[0] = 100  # TypeError: 'tuple' object does not support item assignment
# tup1 + tup2
# del tup1
## Comments: tuple operates in a similar way as lists.


## Dictionary
# dict = {'a': 1, 'b': '3'}
# print(dict)
# print(dict.keys())
# print(dict.values())
# for item in dict:
#     print(item)
#     print(dict[item])

## 关于list及dictionary的一个综合应用
# def crea():
#     dataSet = [[0, 0, 0, 0, 'no'],         #数据集
#             [0, 0, 0, 1, 'no'],
#             [0, 1, 0, 1, 'yes'],
#             [0, 1, 1, 0, 'yes'],
#             [0, 0, 0, 0, 'no'],
#             [1, 0, 0, 0, 'no'],
#             [1, 0, 0, 1, 'no'],
#             [1, 1, 1, 1, 'yes'],
#             [1, 0, 1, 2, 'yes'],
#             [1, 0, 1, 2, 'yes'],
#             [2, 0, 1, 2, 'yes'],
#             [2, 0, 1, 1, 'yes'],
#             [2, 1, 0, 1, 'yes'],
#             [2, 1, 0, 2, 'yes'],
#             [2, 0, 0, 0, 'no']]
#     labels = ['不放贷', '放贷']             #分类属性
#     return dataSet, labels
#
# dat, lab = crea()
# print(type(dat))
# print(type(lab))
#
# ## how to take out the last colum of dat???
# res = [em[-1] for em in dat]
# print(res)
#
# from collections import Counter
# rescount = Counter(res)
# print(rescount.keys())
# print(rescount.values())
#
# breakpoint()

#  PRACTICE1: find the prime number between 1:100;
#  PRACTICE2: find the factor decomposition of a number and print;
