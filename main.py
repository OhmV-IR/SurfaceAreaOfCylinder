# only import pi from math library
from math import pi
# Variable init
running = True
while(running):
    # Gets user input
    height = input("What is the height of the cylinder: ")
    r = input("What is the radius of the circle: ")
    # try to convert r and height to float types
    try:
        r = float(r)
        height = float(height)
    # if it fails, print error and exit the program
    except:
        print("input is not an integer please retry")
        exit()
    # calculation
    C = float(2 * r) * pi
    RectangleA = round(C * height)
    CircleA = round(r**2.0 * pi)
    # output and convert values to strings
    print("Surface area of the cylinder: " + str(RectangleA) + str(CircleA))
    running = False;