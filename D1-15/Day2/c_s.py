#coding:utf-8
'''
输入半径计算圆的周长和面积
'''

import math

def c_s():
    r=int(input("请输入半径:"))
    c=2*math.pi*r
    s=math.pi*r**2
    return c,s

print(c_s())
