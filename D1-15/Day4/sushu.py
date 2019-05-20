"""
输入一个正整数判断它是不是素数
"""

sushu=int(input("请输入一个正整数："))

if sushu<=2:
    print("yes")
else:
    for i in range(2,sushu):
        if sushu%i==0:
            print("no")
        else:
            continue
    print("yes")

