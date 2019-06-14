import turtle
edge = 5
turtle.setup(500,500,0,0)
turtle.penup()
for i in range(8):
    turtle.fd(edge)
    turtle.pendown()    
    turtle.left(90)
    
    turtle.fd(edge)
    turtle.left(90)
    
    edge = edge + 5
    
    turtle.fd(edge)    
    turtle.left(90)
    
    turtle.fd(edge)
    turtle.left(90)
    
    edge = edge + 5
