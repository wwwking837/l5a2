import turtle

turtle.Screen().bgcolor("Yellow")
board = turtle.Turtle()

# First triangle for star
board.forward(100) 


board.left(120)
board.Forward(100)

board.left(120)
board.forward(100)

board.penup()
board.right(150)
board.forward(50)

# Second triangle for star
board.pendown()
board.right(90)
board.forward(100)

board.right(120)
board.forward(100)

board.right(120)
board.forward(100)

turtle.done()