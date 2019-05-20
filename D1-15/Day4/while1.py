"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""

import random

a=random.randint(1,100)
Flag=False

while Flag:
    usernum=int(input("请输入一个整数："))
    if usernum==a:
        Flag=True
    else:
        continue

