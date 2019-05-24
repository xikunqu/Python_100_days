'''
计算c(m,n)
'''


def jiecheng(num):
    print(num)
    if num==1:
        return 1
    else:
        ji=num*jiecheng(num-1)
        return ji

m=int(input("请输入m:"))
n=int(input("请输入n:"))

jieguo=jiecheng(m)/(jiecheng(n)*jiecheng(m-n))
print(jieguo)
