def main():
    scores={'打开':90,'快点':100,"啥的":93}
    #通过键可以获取字典中对应的值
    print(scores['打开'])
    print(scores['快点'])

    #对字典进行遍历（遍历的其实是键，再通过键取对应的值）
    for elem in scores:
        print(elem,scores[elem])

    #更新字典中的元素
    scores['打开']=000
    scores['时间']=111
    scores.update(冷面=670,放=85)
    print(scores)

    if 'jdj ' in scores:
        print(scores['jdj'])
    print(scores.get('快点'))

    #get方法也是通过键获取对应的值但是可以设置默认值

    print(scores.get('解决',90))
    print(scores)

    #删除字典中的元素
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('时间',100))

    #清空字典
    scores.clear()
    print(scores)


if __name__=="__main__":
    main()