#coding:utf-8
'''
将华氏温度转换为摄氏温度
F。8C_32
'''

def zhuanhua():
    f=int(input("请输入华氏温度"))
    c=(f-32)/1.8
    return c

print(zhuanhua())