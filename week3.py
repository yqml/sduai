## Review of week2.py: data type--number, string, list (tuple, dictionary)

# unicode: chr(97); ord('a')
# print(ord('啊'))
# string:
# print('H' in 'Hello')

# List
# lis = [] #creat a new list
# lis.append([4,5])
# print(lis)
# lis.extend([4,5])
# print(lis)
# for i in lis:
#     print(i)
# print(lis[-1]); print(lis[-2]); print(lis[-3])

# print(lis)
# lis.reverse()
# print(lis)

## week3.py

# .count and .index
# row = [1,2,'a','b','b']
# print(row.count('b'))
# print(row.count(2))
# print(row.count(3))

# row = [1,2,'a','b','b']
# print(row.index('a'))
# print(row.index('b'))

# .sort()
# row = [2,24,13,5]
# row.sort()
# print(row)

# row1 = ['a', 'Z', 'r', 'q']
# row1.sort()
# print(row1)
#
# for item in row1:  # item 遍历排序后的row1
#     print(ord(item))

# mixture of number and string(character)
# row2 = [5,3,'a','Z']
# row2.sort()

## tuples: (); # list: [];  # Dictionary: {}
# tup1 = ('physics', ' chemistry', 1997, 2000)
# tup2 = (1,2,3)
# print(tup1 + tup2)
# del tup1

# difference between tuple and list
# row     = [2,3]
# row[1]  = 5
# tup1[2] = 5

# Dictionary:{}
# dict = {'a': 1, 'b': 3}
# print(dict)
# print(dict.values())
# print(dict.keys())

# for i in dict: # i 遍历 dict的keys
#     print(i)
#     print(dict[i])

## 关于dictionary and list的一个综合应用
def crea():
    dataSet = [ [0, 0, 0, 0, 'no'],         #数据集
                [0, 0, 0, 1, 'no'],
                [0, 1, 0, 1, 'yes'],
                [0, 1, 1, 0, 'yes'],
                [0, 0, 0, 0, 'no'],
                [1, 0, 0, 0, 'no'],
                [1, 0, 0, 1, 'no'],
                [1, 1, 1, 1, 'yes'],
                [1, 0, 1, 2, 'yes'],
                [1, 0, 1, 2, 'yes'],
                [2, 0, 1, 2, 'yes'],
                [2, 0, 1, 1, 'yes'],
                [2, 1, 0, 1, 'yes'],
                [2, 1, 0, 2, 'yes'],
                [2, 0, 0, 0, 'no']  ]
    labels = ['不放贷', '放贷']             #分类属性
    return dataSet, labels

dat, lab = crea()
# print(type(dat))
# print(type(lab))

res = [em[-1] for em in dat] # em遍历 dat,按元素遍历;;; em 第一个遍历的就是dat[0]
# print(res)

# 对一个list进行简单的统计
from collections import Counter
rescnt = Counter(res)
print(rescnt)
print(rescnt.keys())
print(rescnt.values())


breakpoint()

### 如何将字典中的元素，按照所对应数字的大小重新排序。
