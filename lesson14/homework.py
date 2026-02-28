import turtle

# Create a turtle object
pen = turtle.Turtle()

# Draw a square using while loop
count = 0
while count < 4:
    pen.forward(100)   # Move forward by 100 units
    pen.right(90)      # Turn right 90 degrees
    count+1

