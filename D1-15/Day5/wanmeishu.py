'''
寻找完美数
如果一个数恰好等于它的因子之和，则称该数为“完全数”
'''

num=int(input("请输入一个整数："))
sum=0

for i in range(1,num):
    if num%i==0:
        sum+=i
    else:
        continue

if num ==sum:
    print("yes")
else:
    print("no")