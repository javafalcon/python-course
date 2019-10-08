import turtle as t
from math import *
def DrawStar(x, y, r, arcbegin):
    px,py = [],[]
    for i in range(5):
        a = arcbegin + i * radians(72)
        px.append(x + r*cos(a))
        py.append(y + r*sin(a))
    t.color('yellow','yellow')
    t.begin_fill()
    j = 0
    t.pu()
    t.goto(px[j],py[j])
    t.pd()
    
    for i in range(5):
        j = (j+2)%5
        t.goto(px[j],py[j])
    t.end_fill()
    
# Draw rectangle as 3:2 and fill with red
t.setup(600,400)
t.pu()
t.goto(-150,100)
t.pd()
t.color('red','red')
t.begin_fill()
t.seth(0)
t.fd(300)
t.right(90)
t.fd(200)
t.right(90)
t.fd(300)
t.right(90)
t.fd(200)
t.end_fill()

# Draw the largest five star
DrawStar(-100,50,30,radians(162))

# Draw other four five stars
arcbegin = -pi + atan(3/5)
DrawStar(-50,80,10,arcbegin)

arcbegin = -pi + atan(1/7)
DrawStar(-30,60,10,arcbegin)

arcbegin = -pi + atan(2/7)
DrawStar(-30,30,10,arcbegin)

arcbegin = -pi + atan(4/5)
DrawStar(-50,10,10,arcbegin)

t.hideturtle()# make the turtle be invisible
t.done()
    
