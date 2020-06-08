import turtle
turtle.pencolor('white')
turtle.bgcolor('black')

global c
c = 0
# PEN COLOR


def pen_color():
    turtle.pencolor('black')

# LINEAR MAKING


def linear():
    k = 5
    k1 = 10
    x = turtle.xcor()
    y = turtle.ycor()
    print(x, y)
    turtle.pencolor('maroon')
    for j in range(70):
        turtle.left(k1)
        k1 += 12
        turtle.forward(25)
        turtle.setpos(x, y)
    turtle.pencolor('yellow')
    for j in range(72):
        turtle.left(k)
        k += 5
        turtle.forward(70)
        turtle.setpos(x, y)

# FLOWER MAKING


def flower():
    turtle.speed('fastest')
    turtle.pencolor('red')
    k = 12
    for j in range(50):
        turtle.left(45)
        turtle.forward(30)
        turtle.circle(25, 180)
        turtle.home()
        turtle.right(k)
        k += 7

# CIRCLE MAKING


def circle():
    turtle.pencolor('lime')
    for j in range(45):
        turtle.speed('fastest')
        turtle.right(13)
        turtle.circle(20)


# TRIANGLE MAKING


def triangle():
    turtle.pencolor('yellow')
    turtle.speed('fastest')
    for j in range(40):
        turtle.forward(100)
        turtle.left(120)
        turtle.forward(100)
        turtle.left(120)
        turtle.forward(100)
        turtle.left(120)
        turtle.right(10)


# triangle()

# DIAMOND


def diamond():
    turtle.pencolor('navy')
    turtle.speed('fastest')
    for j in range(18):
        turtle.forward(70)
        turtle.right(60)
        turtle.forward(50)
        turtle.right(144)
        turtle.forward(102)
        turtle.right(130)
        turtle.left(15)


def main():

    k = 0
    turtle.speed('fastest')
    for i in range(8):  # 8
        turtle.left(k)
        turtle.forward(100)
        circle()
        pen_color()
        turtle.home()
        turtle.right(k)
        k += 45
        pen_color()
        turtle.home()
    # diamond
    k = 0
    for i in range(12):  # 12
        turtle.left(k)
        turtle.forward(400)
        diamond()
        k += 30
        pen_color()
        turtle.home()
    k = 0
    for i in range(12):
        turtle.right(k)
        turtle.forward(225)
        linear()
        turtle.home()
        k += 30

    flower()
    triangle()


main()

turtle.done()
