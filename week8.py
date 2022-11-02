# import pandas as pd
# import matplotlib.pyplot as plt
#
# # Data reading
# sale = pd.DataFrame(pd.read_csv('C:\\Users\\Administrator\\Desktop\\朝阳数据.csv',  header = 0) )
# # print(sale.describe())
# # print(sale.info())
# # print(sale.shape)
# # print(sale.head(3))
# sale.rename(columns = {'购药时间': '销售时间'}, inplace = True)
# sale['应收金额'] = sale['应收金额'].astype('int')
#
# # 时间数据转化
# sep = sale['销售时间'].str.split()
# sale['销售时间'] = [em[0] for em in sep]
# sale['销售星期'] = [em[1] for em in sep]
#
# sale['销售时间'] = pd.to_datetime(sale['销售时间'], format = '%Y-%m-%d',
#                                         errors= 'coerce')
# # 重新排序
# sale = sale.sort_values(by = '社保卡号', ascending = True)
# sale = sale.reset_index(drop = True)
#
# # 处理异常值
# sale = sale[(sale['销售数量'] > 0) & (sale['应收金额'] > 0) & (sale['实收金额'] > 0)]
#
# # Analysis
# # 1. average consumption times in a month
# subsale = sale.drop_duplicates(subset = ['销售时间', '社保卡号'])
# total = subsale.shape[0]
# month = (subsale['销售时间'].max() - subsale['销售时间'].min()).days//30
# t1    = total/month
#
# # 2. average consumption values in a month
# total1 = sale['实收金额'].sum()
# t2 = total1/month
# # print('月均消费金额：', '%.2f' % t2)
#
# # 3. 客单价
# t3 = total1/total
#
# # 4. 消费趋势
# sale.index = pd.DatetimeIndex(sale['销售时间'])
# daysale = sale.resample('D').count()
# plt.plot_date(daysale.index, daysale['实收金额'].values, fmt = '-')
# plt.xlabel('Time')
# plt.ylabel('Money')
# plt.title('Sales Volume -- day')
# plt.show()
#
# breakpoint()

#Week9
import numpy as np
import random
from scipy import stats

speed = [1,2,3,4,5,6,7,8,9,10]

# s1 = np.mean(speed)
# s2 = np.median(speed)
# s3 = np.std(speed)
# s4 = np.var(speed)
# s25 = np.percentile(speed, 25)
# s90 = np.percentile(speed, 90)
# smode = stats.mode(speed)

# Some basic mathematical calculation
# a1 = pow(2, 3)
# a2 = round(1.126, 2)
# a3 = np.sqrt(4)

## random number
# b1 = random.choice(range(10))
# b2 = random.randrange(10,100,7)
# b3 = random.randint(1,6)
# b4 = random.uniform(1,6)
lis = [1,2,3,4,5]
c1  = random.choice(lis)
random.shuffle(lis)
c3  = random.sample(lis, 2)

breakpoint()