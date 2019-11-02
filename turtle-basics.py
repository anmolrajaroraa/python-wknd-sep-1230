import turtle

'''turtle

#member variables
shape
color
#member functions
setposition()
penup()'''

freddy = turtle.Pen()
freddy.shape('turtle')
freddy.turtlesize(2,2)
freddy.width(3)
freddy.color('red')
freddy.fillcolor('blue')
'''freddy.begin_fill()
for i in range(4):
    freddy.forward(100)
    freddy.left(90)
freddy.end_fill()
freddy.left(90)
freddy.forward(100)
freddy.right(90)
freddy.write("Square", False, font=("Arial", 16, "normal"))
#freddy.hideturtle()
freddy.circle(50)
freddy.dot(50)'''
for i in range(3):
    freddy.forward(100)
    freddy.left(120)

for i in range(6):
    freddy.forward(100)
    freddy.left(60)
