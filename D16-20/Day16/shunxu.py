# 最基本的查找算法，
# 基本原理：
# 对于任意一个序列以及一个给定元素，将给定元素与序列中元素依次比较，直到找出与给定关键字相同的数为止

import random
Range = 10
Length = 5
flag = 0
pos = -1

list = random.sample(range(Range),Length)
goal = random.randint(0,Range)
print('search ',goal,', in list:',list)

for i in range(Length):
    if list[i] == goal:
        flag = 1
        pos = i
        break

if flag:
    print('find in ',pos+1,'th place')
else:
    print('not found')
