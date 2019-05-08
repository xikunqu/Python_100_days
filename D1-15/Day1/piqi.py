#coding:utf-8
import turtle as t
import time
'''
turtle 学习地址：https://docs.python.org/zh-cn/3.6/library/turtle.html
'''

def  nose(x,y):
    '''鼻子'''
    t.penup()
    #将海归移动到指定的位置
    t.goto(x,y)
    t.pendown()
    #设置海龟的方向
    t.setheading(-30)
    t.begin_fill()
    a=0.4
    for i in range(120):
        if 0<=i<30 or 60<=i<90:
            a=a+0.08
            #向左转3度
            t.left(3)
            #向前走
            t.fd(a)
        else:
            a=a-0.08
            t.lt(3)
            t.fd(a)
    t.end_fill()
    t.penup()
    t.setheading(90)
    t.fd(25)
    t.setheading(0)
    t.fd(10)
    t.pendown()

    #设置画笔暗色（红，绿，蓝）
    t.colormode(255)
    t.pencolor(255,155,192)
    t.setheading(10)
    t.begin_fill()
    t.circle(5)
    t.color(160,82,45)
    t.end_fill()
    t.penup()
    t.setheading(0)
    t.fd(20)
    t.pendown()
    t.pencolor(255,155,192)
    t.setheading(10)
    t.begin_fill()
    t.circle(5)
    t.color(160,82,45)
    t.end_fill()
    print(t.pos())
    time.sleep(1)

def head(x,y):
    '''头'''
    t.colormode(255)
    t.color((255,155,192),'pink')
    t.penup()
    t.goto(x,y)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.setheading(180)
    t.circle(300,-30)
    t.circle(100,-60)
    t.circle(80,-100)
    t.circle(150,-20)
    t.circle(60,-95)
    t.setheading(161)
    t.circle(-300,15)
    t.penup()
    t.goto(-100,100)
    t.pendown()
    t.setheading(-30)
    a=0.4
    for i in range(60):
        if 0<=i<30 or 60<=i<90:
            a=a+0.08
            t.lt(3)
            t.fd(a)
        else:
            a=a-0.08
            t.lt(3)
            t.fd(a)
    t.end_fill()
    time.sleep(1)

def ears(x,y):
    '''耳朵'''
    t.colormode(255)
    t.color((255,155,192),"pink")
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.setheading(100)
    t.circle(-50,50)
    t.circle(-10,120)
    t.circle(-50,54)
    t.end_fill()
    t.penup()
    t.setheading(90)
    t.fd(-12)
    t.setheading(0)
    t.fd(30)
    t.pendown()
    t.begin_fill()
    t.setheading(100)
    t.circle(-50,50)
    t.circle(-10,120)
    t.circle(-50,56)
    t.end_fill()
    time.sleep(2)

def eyes(x,y):
    '''眼睛'''
    t.colormode(255)
    t.color((255,155,192),"white")
    t.penup()
    t.setheading(90)
    t.fd(-20)
    t.setheading(0)
    t.fd(-95)
    t.pendown()
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.color("black")
    t.penup()
    t.setheading(90)
    t.fd(12)
    t.setheading(0)
    t.fd(-3)
    t.pendown()
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    t.color((255,155,192),"white")
    t.penup()
    t.seth(90)
    t.fd(-25)
    t.seth(0)
    t.fd(40)
    t.pendown()
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.color("black")
    t.penup()
    t.setheading(90)
    t.fd(12)
    t.seth(0)
    t.fd(-3)
    t.pendown()
    t.begin_fill()
    t.circle(3)
    t.end_fill()
    time.sleep(3)

def cheek(x,y):
    '''脸颊'''
    t.colormode(255)
    t.color((255,155,192))
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.seth(0)
    t.begin_fill()
    t.circle(30)
    t.end_fill()
    time.sleep(1)


def mouth(x,y):
    '''嘴巴'''
    t.colormode(255)
    t.color(239,69,19)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.setheading(-80)
    t.circle(30,40)
    t.circle(40,80)
    time.sleep(2)

def setting():
    '''设置参数'''
    t.pensize(4)
    #隐藏海归
    t.hideturtle()
    t.colormode(255)
    t.color((255,155,192),'pink')
    t.setup(840,500)
    t.speed(10)

def main():
    '''
    主函数
    :return:
    '''
    setting()
    nose(-100,100)
    head(-69,167)
    ears(0,160)
    eyes(0,140)
    cheek(80,10)
    mouth(-20,30)
    t.done()

if __name__=='__main__':
    main()



#cheek(20,30)


#eyes(90,90)

#ears(50,60)

# head(50,60)
#nose(50,60)
# t.pensize(4)
# t.pencolor('red')
# t.forward(100)
# t.right(90)
# t.fd(100)
# t.right(90)
# t.forward(100)
# t.rt(90)
# t.fd(100)
# t.mainloop()

# print(t.position())
# t.fd(25)
# print(t.position())
# t.forward(-75)
# print(t.position())

# print(t.position())
# t.bk(30)
# print(t.position())

# print(t.heading())
# t.right(45)
# print(t.heading())


# tp=t.pos()
# print(tp)
# t.setpos(60,30)
# print(t.pos())
# t.setpos(20,80)
# print(t.pos())
# t.setpos(tp)
# print(t.pos())

# print(t.pos())
# t.setx(10)
# print(t.pos())

# print(t.pos())
# t.sety(-10)
# print(t.pos())

# print(t.heading())
# t.seth(90)
# print(t.heading())
# t.home()
# print(t.heading())

# t.home()
# print(t.pos())
# print(t.heading())
#
# t.circle(50)
# print(t.pos())
# print(t.heading())
#
# t.circle(120,180)
# print(t.pos())
# print(t.heading())

# t.home()
# time.sleep(1)
# t.dot()
# time.sleep(2)
# t.fd(50)
# time.sleep(3)
# t.dot(20,'blue')
# time.sleep(4)
# t.fd(50)
# print(t.pos())
# print(t.heading())

# t.color("blue")
# astamp=t.stamp()
# t.fd(50)
# print(t.pos())
# t.clearstamp(astamp)
# print(t.pos())


# for i in range(4):
#     t.fd(50)
#     t.lt(80)
#
# for i in range(8):
#     t.undo()


# print(t.speed())
#
# t.speed('normal')
# print(t.speed())
# t.speed(9)
# print(t.speed())


# t.goto(10,10)
# print(t.towards(0,0))

# t.home()
# t.left(50)
# t.forward(100)
# print(t.pos())
# print(t.xcor())
# print(t.ycor())
# print(t.heading())

# t.home()
# print(t.distance(30,40))

# t.pen(fillcolor="black",pencolor='red',pensize=10)
# print(sorted(t.pen().items()))
# penstate=t.pen()
# t.color("yellow","")
# t.penup()
# print(sorted(t.pen().items())[:3])
# t.pen(penstate,fillcolor='green')
# print(sorted(t.pen().items())[:3])


# print(t.colormode())
# print(t.pencolor())
# t.pencolor('brown')
# print(t.pencolor())
# tup=(0.2,0.8,0.55)
# t.pencolor(tup)
# print(t.pencolor)
# t.colormode(255)
# print(t.pencolor())


