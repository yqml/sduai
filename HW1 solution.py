import math

# 第一次作业

# 第一题，判断一个数是奇数还是偶数
num = int(input("请输入一个整数："))  # input()的作用是让用户输入一个字符串，int()函数的作用是把字符串转换为整数
if num % 2 == 0:  # %是取余数的意思
    print("是偶数")  # 如果余数是0，则print是偶数
else:
    print("是奇数")


# 第二题，定义一个“函数”，判断一个数字是否为质数（只能被1和自己整除）

def is_prime(n):
    isprime = True  # 我们先认为n是质数
    if n < 2:       # 如果小于2，肯定不是质数，pass
        return False
    elif n == 2:    # 如果是2，肯定是质数
        return True
    elif n % 2 == 0:    # 除了2以外的偶数，全不是质数
        return False
    else:
        for j in range(3, int(math.sqrt(n))+1, 2):  # 从3开始，3、5、7、9慢慢验证
            if n % j == 0:
                isprime = False  # 如果能被整除，假设不成立，把isprime赋值为假的
        return isprime  # 返回isprime


if is_prime(num):
    print("您输入的数字是素数")
else:
    print("您输入的数字不是素数")


# 第三题，输出1-100的质数
print("1-100中的素数有：")
for i in range(101):
    if is_prime(i):
        print(i)
