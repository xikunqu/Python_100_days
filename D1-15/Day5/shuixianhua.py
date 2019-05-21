'''
寻找水仙花数
所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身
'''

num=input("请输入一个整数：")
sum=0

for i in num:
    sum+=int(i)**3
    print(sum)

if int(num)==sum:
    print("yes")
else:
    print("no")