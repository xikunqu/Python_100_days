'''
生成‘斐波拉切数列’
'''

def fblq(n):
    if n==1 or n==2:
        return 1
    else:
        f=fblq(n-1)+fblq(n-2)
        return f

print(fblq(5))