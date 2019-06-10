from abc  import ABCMeta,abstractmethod
from random import randint,randrange

class Fighter(object,metaclass=ABCMeta):
    '''
    战斗者
    '''

    #通过__slots__魔法限定对象可以绑定的成员变量
    __slots__=('_name','_hp')

    def __init__(self,name,hp):
        '''
        初始化方法
        :param name:名字
        :param hp: 生命值
        :return:
        '''
        self._name=name
        self._hp=hp

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @name.setter
    def name(self,name):
        self._name=name

    @hp.setter
    def hp(self,hp):
        self._hp=hp

    @property
    def alive(self):
        return self._hp>0

    @abstractmethod
    def attack(self,other):
        '''
        攻击
        :param other: 被攻击的对象
        :return:
        '''
        pass


class Ultraman(Fighter):
    '''
    奥特曼
    '''

    __slots__ = ('_name','_hp','_mp')

    def __init__(self,name,hp,mp):
        '''
        初始化方法
        :param name: 名字
        :param hp: 生命值
        :param mp: 魔法值
        :return:
        '''
        super().__init__(name,hp)
        self._mp=mp


    def attack(self,other):
        other.hp-=randint(15,25)

    def huge_attack(self,other):
        '''
        终极必杀技（打掉对方至少50点或四分之三的血)
        :param other:被攻击的对象
        :return:使用成功则返回True 否则返回False
        '''
        if self._mp>=50:
            self._mp-=50
            injury=other.hp*3//4
            injury=injury if injury>=50 else 50
            other.hp-=injury
            return True
        else:
            self.attack(other)
            return False


    def magic_attack(self,others):
        '''
        魔法攻击
        :param others:被攻击的群体
        :return:使用魔法成功返回True 否则返回False
        '''

        if self._mp>=20:
            self._mp-=20
            for temp in others:
                if temp.alive:
                    temp.hp-=randint(10,15)
            return True
        else:
            return False

    def resume(self):
        '''
        恢复魔法值
        :return:
        '''

        incr_point=randint(1,10)
        self._mp+=incr_point
        return incr_point


    def __str__(self):
        return '~~~~~%s奥特曼~~~~~\n' %self._name + \
             '生命值： %d\n' %self._hp + \
            '魔法值：%d\n'%self._mp



class Monster(Fighter):
    '''
    小怪兽
    '''

    __slots__ = ('_name','_hp')

    def attack(self,other):
        other.hp-=randint(10,20)


    def __str__(self):
        return '~~~%s小怪兽~~~~\n' %self._name +\
            '生命值：%d\n' %self._hp

def is_any_alive(monsters):
    '''
    判断有没有小怪兽是活着的
    '''

    for monster in monsters:
        if monster.alive>0:
            return True
        else:
            return False


def select_alive_one(monsters):
    '''

    :param monsters:
    :return:
    '''

    monsters_len=len(monsters)
    while True:
        index=randrange(monsters_len)
        monster=monsters[index]
        if monster.alive>0:
            return monster

def display_info(ultraman,monsters):
    '''显示奥特曼和小怪兽的信息'''
    print(ultraman)
    for monster in monsters:
        print(monster,end='')


def main():
    u=Ultraman('嗷嗷',1000,120)
    m1=Monster('怪物1',250)
    m2=Monster('怪物2',500)
    m3=Monster('怪物3',750)

    ms=[m1,m2,m3]

    fight_round=1

    while u.alive and is_any_alive(ms):
        print("===========第%2d回合============"%fight_round)
        m=select_alive_one(ms)#选中一只小怪兽
        skill=randint(1,10)#通过随机数选择使用哪种技能
        if skill <=6: #60%的概率使用普通攻击
            print("%s使用普通攻击打了%s"%(u.name,m.name))
            u.attack(m)
            print("%s的魔法值恢复了%s点"%(u.name,u.resume()))
        elif skill<=9:  #30%的概率使用魔法攻击（可能因魔法值不足而失败）
            if u.magic_attack(ms):
                print("%s使用了魔法攻击",u.name)
            else:
                print("%s使用魔法攻击失败",u.name)

        else:  #10%的概率使用终极必杀技，如果魔法之不足则使用普通攻击
            if u.huge_attack(m):
                print("%s使用终极必杀技虐了%s"%(u.name,m.name))
            else:
                print("%s使用普通攻击攻打了%s"%(u.name,m.name))
                print('%s的魔法值恢复了%d点')%(u.name,u.resume())

        if m.alive>0:  #如果选中的小怪兽没有死就回击奥特曼
            print("%s回击了%s"%(m.name,u.name))
            m.attack(u)

        display_info(u,ms)  #每个回合接收后显示奥特曼和小怪兽的信息
        fight_round+=1
    print('\n==============战斗结束！===============\n')
    if u.alive>0:
        print("%s奥特曼胜利！"%u.name)
    else:
        print("小怪兽胜利！")



if __name__=='__main__':
    main()




