"""
输入两个正整数计算最大公约数和最小公倍数

"""
import math

a=int(input("请输入a:"))
b=int(input("请输入b:"))

if a > b:
    a, b = b, a
for factor in range(a, 0, -1):
    if a % factor == 0 and b % factor == 0:
        print('%d和%d的最大公约数是%d' % (a, b, factor))
        print('%d和%d的最小公倍数是%d' % (a, b, a * b // factor))
        break

