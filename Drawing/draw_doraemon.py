from turtle import *


# Doraemon with Python Turtle
def main(x, y):
    penup()
    goto(x, y)
    pendown()


def eye():
    fillcolor("#ffffff")
    begin_fill()

    tracer(False)
    a = 2.5
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            lt(3)
            fd(a)
        else:
            a += 0.05
            lt(3)
            fd(a)
    tracer(True)
    end_fill()


def hair():
    main(-32, 135)
    seth(165)
    fd(60)

    main(-32, 125)
    seth(180)
    fd(60)

    main(-32, 115)
    seth(193)
    fd(60)

    main(37, 135)
    seth(15)
    fd(60)

    main(37, 125)
    seth(0)
    fd(60)

    main(37, 115)
    seth(-13)
    fd(60)


def mouth():
    main(5, 148)
    seth(270)
    fd(100)
    seth(0)
    circle(120, 50)
    seth(230)
    circle(-120, 100)


def colar():
    fillcolor('#e70010')
    begin_fill()
    seth(0)
    fd(200)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    fd(207)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    end_fill()


def nose():
    main(-10, 158)
    seth(315)
    fillcolor('#e70010')
    begin_fill()
    circle(20)
    end_fill()


def black_eye():
    seth(0)
    main(-20, 195)
    fillcolor('#000000')
    begin_fill()
    circle(13)
    end_fill()

    pensize(6)
    main(20, 205)
    seth(75)
    circle(-10, 150)
    pensize(3)

    main(-17, 200)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    circle(5)
    end_fill()
    main(0, 0)


def face():
    fd(183)
    lt(45)
    fillcolor('#ffffff')
    begin_fill()
    circle(120, 100)
    seth(180)
    # print(pos())
    fd(121)
    pendown()
    seth(215)
    circle(120, 100)
    end_fill()
    main(63.56, 218.24)
    seth(90)
    eye()
    seth(180)
    penup()
    fd(60)
    pendown()
    seth(90)
    eye()
    penup()
    seth(180)
    fd(64)


def bottom():
    penup()
    circle(150, 40)
    pendown()
    fillcolor('#00a0de')
    begin_fill()
    circle(150, 280)
    end_fill()


def Doraemon():
    bottom()

    colar()

    face()

    nose()

    mouth()

    hair()

    main(0, 0)

    seth(0)
    penup()
    circle(150, 50)
    pendown()
    seth(30)
    fd(40)
    seth(70)
    circle(-30, 270)

    fillcolor('#00a0de')
    begin_fill()

    seth(230)
    fd(80)
    seth(90)
    circle(1000, 1)
    seth(-89)
    circle(-1000, 10)

    # print(pos())

    seth(180)
    fd(70)
    seth(90)
    circle(30, 180)
    seth(180)
    fd(70)

    # print(pos())
    seth(100)
    circle(-1000, 9)

    seth(-86)
    circle(1000, 2)
    seth(230)
    fd(40)

    # print(pos())

    circle(-30, 230)
    seth(45)
    fd(81)
    seth(0)
    fd(203)
    circle(5, 90)
    fd(10)
    circle(5, 90)
    fd(7)
    seth(40)
    circle(150, 10)
    seth(30)
    fd(40)
    end_fill()

    seth(70)
    fillcolor('#ffffff')
    begin_fill()
    circle(-30)
    end_fill()

    main(103.74, -182.59)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(-15, 180)
    fd(90)
    circle(-15, 180)
    fd(10)
    end_fill()

    main(-96.26, -182.59)
    seth(180)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(15, 180)
    fd(90)
    circle(15, 180)
    fd(10)
    end_fill()

    main(-133.97, -91.81)
    seth(50)
    fillcolor('#ffffff')
    begin_fill()
    circle(30)
    end_fill()
    # Doraemon with Python Turtle

    main(-103.42, 15.09)
    seth(0)
    fd(38)
    seth(230)
    begin_fill()
    circle(90, 260)
    end_fill()

    main(5, -40)
    seth(0)
    fd(70)
    seth(-90)
    circle(-70, 180)
    seth(0)
    fd(70)

    main(-103.42, 15.09)
    fd(90)
    seth(70)
    fillcolor('#ffd200')
    # print(pos())
    begin_fill()
    circle(-20)
    end_fill()
    seth(170)
    fillcolor('#ffd200')
    begin_fill()
    circle(-2, 180)
    seth(10)
    circle(-100, 22)
    circle(-2, 180)
    seth(180 - 10)
    circle(100, 22)
    end_fill()
    goto(-13.42, 15.09)
    seth(250)
    circle(20, 110)
    seth(90)
    fd(15)
    dot(10)
    main(0, -150)

    black_eye()


if __name__ == '__main__':
    screensize(800, 600, "#f0f0f0")
    pensize(3)
    speed(9)
    Doraemon()
    main(100, -300)
    write('Doraemon', font=("Bradley Hand ITC", 30, "bold"))
    mainloop()
