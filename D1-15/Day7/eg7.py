def main():
    #定义元组
    t=('安静的',38,True,'四川成都')
    print(t)
    #获取元组中得元素
    print(t[0])
    print(t[3])
    #遍历元组中得值
    for member in t:
        print(member)

    #重新给元组赋值
    #t[0]='我忘记' #TypeError
    #变量t重新引起了新得元组原来得元组将被垃圾回收
    t=('数据均',20,True,"云南")
    print(t)
    #将元组转换成列表
    person=list(t)
    print(person)

    #列表是可以修改它得元素得
    person[0]="经决定"
    person[1]=25
    print(person)

    #将列表转换成元组
    fruits_list=['apple','banana','orange']
    fruits_tuple=tuple(fruits_list)
    print(fruits_tuple)


if __name__=='__main__':
    main()