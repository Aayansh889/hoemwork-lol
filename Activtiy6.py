import turtle
square=turtle.Turtle()
forward=int(input("Enter number of steps"))
shape=int(input("Enter how many sides"))
for i in range(shape):
    turtle.forward(forward)
    turtle.right(90)

turtle.done()