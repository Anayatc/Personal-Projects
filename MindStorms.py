import turtle

def draw_sqaure(some_turtle):
    for i in range(1,5):
        some_turtle.forward(150)
        some_turtle.right(90)

def draw_triangle(turt):
    for i in range(1,4):
        turt.forward(200)
        turt.right(120)

def circ_square():
    window = turtle.Screen()
    window.bgcolor('white')
    james = turtle.Turtle()
    james.speed(10)
    for i in range(1,73):
        draw_triangle(james)
        james.right(5)
    window.exitonclick()


"""def draw_art():
    window = turtle.Screen()
    window.bgcolor('white')

    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.speed(2)
    draw_sqaure(brad)

    angie = turtle.Turtle()
    angie.shape('turtle')
    angie.circle(100)

    ben = turtle.Turtle()
    ben.shape('turtle')
    draw_triangle(ben)


    window.exitonclick()
"""

circ_square()
