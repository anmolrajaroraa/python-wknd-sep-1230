import turtle

freddy = turtle.Pen()
freddy.shape('turtle')
freddy.turtlesize(2,2)
freddy.width(3)
freddy.color('red')
freddy.speed(0)
#freddy.penup()
#freddy.setposition(0,-250)
#freddy.pendown()

for i in range(100):
    freddy.circle(i * 5)
    #freddy.left(10)
    freddy.penup()
    freddy.right(90)
    freddy.forward(5)
    freddy.left(90)
    freddy.pendown()
