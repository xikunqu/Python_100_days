#coding:utf-8
'''
判断是否是闰年
'''

def run_nian():
    year=int(input("请输入年份："))
    if year%400==0 or year%100!=0 and year%4==0:
        return True
    else:
        return False

print(run_nian())
