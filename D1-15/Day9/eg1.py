class Person(object):

    #限定Person对象只能绑定_name,_age,_gender属性
    __slots__=('_name','_age','_gender')

    def __init__(self,name,age):
        self._name=name
        self._age=age

    #访问器- getter方法
    @property
    def name(self):
        return self._name

    #访问器-setrer方法
    @property
    def age(self):
        return self._age

    #修改器-setter方法
    @name.setter
    def name(self,name):
        self._name=name

    #修改器-setter方法
    @age.setter
    def age(self,age):
        self._age=age

    def play(self):
        if self._age<=16:
            print("%s正在玩飞行器。"%self._name)
        else:
            print("%s正在玩斗地主"%self._name)


def main():
    person=Person('文件见',12)
    person.play()
    person.age=22
    person.play()
    person._is_gay=True


if __name__=='__main__':
    main()