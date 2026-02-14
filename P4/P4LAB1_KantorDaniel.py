# Daniel Kantor
# February 14, 2026
# P4LAB1
# Import turtle library to draw images


import turtle

# Allows while loop to run until declared False in the function
house_built = True

# Name our Turtle 'Bob'
bob = turtle.Turtle()
bob.shape("turtle")
bob.speed(6)

# Create the window GUI
window = turtle.Screen()
window.setup(width=1000, height=1000)
window.bgcolor("black")

# Function for our while and for loops
def house(bob):
    # Orange Square
    bob.fillcolor("orange")
    bob.begin_fill()
    for _ in range(4):
        bob.forward(300)
        bob.right(90)
    bob.end_fill()

    # Position bob 45 degrees so he can draw the triangle roof
    bob.setheading(45)

    # Blue Triangle
    bob.fillcolor("blue")
    bob.begin_fill()
    bob.forward(212.13)
    bob.right(90)
    bob.forward(212.13)
    bob.right(135)
    bob.forward(300)
    bob.end_fill()

    house_built = False


while house_built:
    house(bob)
    break

# Wait for user to 'X' out
window.mainloop()