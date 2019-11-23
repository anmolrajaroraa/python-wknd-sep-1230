import turtle, random

screen = turtle.Screen()
screen.bgcolor('black')
fred = turtle.Pen()
fred.shape('turtle')
fred.turtlesize(3,3)
fred.width(3)
fred.speed(0)

colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 'turquoise']

shapes = ['square', 'circle', 'dot', 'triangle', 'hexagon']

coordinates = list(range(-300,301))

for i in range(100):
    selectedColor = random.choice(colors)
    fred.color(selectedColor)

    fred.penup()
    x = random.choice(coordinates)
    y = random.choice(coordinates)
    fred.setposition(x,y)
    fred.pendown()

    selectedShape = random.choice(shapes)
    print(selectedShape)

    if selectedShape == "square":
        for i in range(4):
            fred.forward(100)
            fred.left(90)
    elif selectedShape == "circle":
        fred.circle(50)
    elif selectedShape == "dot":
        fred.dot(50)
    elif selectedShape == "triangle":
        for j in range(3):
            fred.forward(100)
            fred.left(120)
    else:
        for i in range(6):
            fred.forward(100)
            fred.left(60)