'''
Craps赌博游戏
规则：玩家掷两个骰子，每个骰子点数为1-6，如果第一次点数和为7或11，则玩家胜；如果点数和为2、3或12，则玩家输庄家胜。
若和为其他点数，则记录第一次的点数和，玩家继续掷骰子，直至点数和等于第一次掷出的点数和则玩家胜；若掷出的点数和为7则庄家胜。
'''
import random
x=random.randint(1,6)
y=random.randint(1,6)
print(x,y)
z=x+y
if z==7 or z==11:
    print("玩家赢")
elif z==2 or z==3 or z==12:
    print("庄家赢")
else:
    while True:
        x=random.randint(1,6)
        y=random.randint(1,6)
        if x+y==z:
            print(x,y)
            print("玩家赢")
            break
        elif x+y==7:
            print(x,y)
            print("庄家赢")
            break
        else:
            continue
