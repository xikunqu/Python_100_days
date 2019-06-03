'''
一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
'''

import random

allstr="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def random_num(len=4):
    '''长度为len的字符串'''
    return ''.join(random.choice(allstr) for _ in range(len))

a=random_num()
print(a)
print(type(a))