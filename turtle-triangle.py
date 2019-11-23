import turtle, random
# screen = turtle.Screen()
fred = turtle.Pen()
fred.shape('turtle')
fred.turtlesize(3,3)
# fred.color('red')
fred.width(3)
fred.speed(10)

colors = ['Medium Blue', 'Medium Turquoise', 'Chartreuse', 'Yellow', 'Deep Pink', 'red', 'blue', 'gold', 'dark green', 'black']

# fred.penup()
# fred.setposition(0,-200)
# fred.pendown()
for i in range(50):
    selectedColor = random.choice(colors)
    fred.color(selectedColor)


    for j in range(3):
        fred.forward(15 * i)
        fred.left(120)
    fred.penup()
    fred.backward(7.5)
    fred.right(90)
    fred.forward(5)
    fred.left(90)
    fred.pendown()
