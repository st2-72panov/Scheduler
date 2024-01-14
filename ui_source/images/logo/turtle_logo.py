import turtle
from math import sqrt


def paint_spiral():
    t.color(blue)
    t.width(4)
    t.forward(s12)


def paint_square():
    if i < 35:
        t.width(side * 2.2 / side0)
        t.color(light_blue)
        t.forward(s12 * 11)
    else:
        t.up()
        t.forward(s12 * 11)
        t.down()
    t.right(90)


t = turtle.Pen()
t.up()
t.goto(-450, 450)
t.down()
t.speed(0)

side = side0 = 24 * 37.938105
blue = '#42aaff'
light_blue = '#75c1ff'

#Основной квадрат
t.width(side * 4 / side0)
t.color(blue)
for i in range(4):
    t.forward(side)
    t.right(90)
t.forward(side / 12)
t.right(5.194428908)

for i in range(70):
    side *= sqrt(122) / 12
    s12 = side / 12
    for j in range(4):
        paint_spiral()
        paint_square()
    paint_spiral()

    t.right(5.194428908)

t.ht()



    
        
