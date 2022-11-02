#_*_ coding: utf-8 _*_
import numpy as np
import pandas as pd

## Data reading YANG QI
# df = pd.DataFrame(pd.read_csv('C:\\Users\\Administrator\\Desktop\\pbc.csv', header=0))
# df1 = df[['id', 'time', 'status', 'trt', 'sex']]
# df1 = df1[(df1['id'] % 20 == 0)]
# df1 = df1.reset_index() # drop = True

## Summary statistics
# print(df1.describe())
# print(df1.info())
# print(df1.shape)
# print(df1.head())
# print(df1.head(3))
# print(df1.tail())
# print(df1.isna())
# print(df1.isnull())
# print(df1['status'].unique())

## 截取子集: 筛选id大于10的; 筛选女性; 筛选女性且id大于30; 筛选trig列非na的行
# df1 = df[['id', 'time', 'status', 'trt']]
# print(type(df['id']))
# df2 = df[df['id'] > 10]
# df3 = df[df['sex'].isin(['f'])]
# df4 = df[(df['sex']=='f') & (df['id']>30)]
# df5 = df[df['trig'].notna()]


# breakpoint()

## 删除或填充NA
# df6 = df.dropna(how = 'any')
# df7 = df.dropna(subset=['trt', 'trig'], how = 'any')
# df8 = df1['trt'].fillna(df1['trt'].mean())
# df9 = df.fillna(value=0)


## 修改某一列变量类型; 调整大小写字母; 删除重复值
# df['id'] = df['id'].astype('float')
# temp = df1['sex']
# df1['sex'] = df1['sex'].str.upper()
# df1['status'].drop_duplicates(keep = 'last')


##列名字
# colname0 = df.columns
# colname1 = df.columns.to_list()
# colname2 = df.columns.values
# colname3 = [col for col in df]
# colname4 = list(df)
# print(colname0)
# print(colname1)
# print(colname2)
# print(type(colname0))
# print(type(colname1))
# print(type(colname2))

# df1 = df[['id', 'time', 'status', 'trt']]
# df1.columns = [list('ABCD')]
# df.rename(columns={'id' : 'id1'}, inplace=True)


## 排序
# df1 = df1.sort_values(by = 'time')# , ascending=True
# print(df1.head())
# df1 = df1.reset_index(drop = True)
# print(df1.head())


## loc, iloc, ix
# ddf1 = pd.DataFrame(data = [[1,2,3],[4,5,6],[7,8,9]], index = [0,1,2], columns=['a','b','c'])
# ddf2 = pd.DataFrame(data = [[1,2,3],[4,5,6],[7,8,9]], index = ['e','f','g'], columns=['a','b','c'])
# print(ddf1)
# print(ddf2)

## loc function: loc 找的是行列名的label~！！！
# print(ddf1.loc[0])
# print(ddf2.loc['e'])
# print(ddf1.loc[1:])
# print(ddf1.loc[:,['a','b']])
# print(ddf1.loc[0:1,['a','b']])

## iloc function: iloc 找的是行列的整数值！！！
# print(ddf1.iloc[0])
# print(ddf2.iloc[0])
# print(ddf1.iloc[1:])
# print(ddf2.iloc[:,0:2])
# print(ddf2.iloc[0:2,0:1])

## ix function; not available in future use loc or iloc
# s = pd.Series(np.nan, index=[12,13,14,1,2,3])
# print(s.iloc[:3])
# print(s.loc[:3])
# print(s.ix[:3])
