'''
百钱百鸡问题
百钱买百鸡的问题算是一套非常经典的不定方程的问题，题目很简单：公鸡5文钱一只，母鸡3文钱一只，
小鸡3只一文钱， 用100文钱买一百只鸡,其中公鸡，母鸡，小鸡都必须要有，问公鸡，母鸡，小鸡要买多少只刚好凑足100文钱？
'''

for i in range(1,15):
    for j in range(1,25):
        k=100-i-j
        if 5*i+3*j+k/3==100:
            print(i,j,k)
