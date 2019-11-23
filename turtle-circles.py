import turtle, random

freddy = turtle.Pen()
freddy.shape('turtle')
freddy.turtlesize(2,2)
freddy.width(3)
# freddy.color('red')
freddy.speed(0)
#freddy.penup()
#freddy.setposition(0,-250)
#freddy.pendown()

colors = ['Medium Blue', 'Medium Turquoise', 'Chartreuse', 'Yellow', 'Deep Pink', 'red', 'blue', 'gold', 'dark green', 'black']
colorIndex = 0

for i in range(100):
    # selectedColor = colors[colorIndex]
    # print(selectedColor)
    # freddy.color(selectedColor)
    # colorIndex += 1     #colorIndex = colorIndex + 1
    # if colorIndex > 4:
    #     colorIndex = 0

    selectedColor = random.choice(colors)
    freddy.color(selectedColor)

    freddy.circle(i * 5)
    freddy.left(10)
    freddy.penup()
    freddy.right(90)
    freddy.forward(5)
    freddy.left(90)
    freddy.pendown()
