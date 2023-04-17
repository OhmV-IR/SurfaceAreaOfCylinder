from math import pi
running = True
while(running):
    height = input("What is the height of the cylinder: ")
    r = input("What is the radius of the circle: ")
    try:
        r = float(r)
        height = float(height)
    except:
        print("input is not an integer please retry")
        exit()
    C = float(2 * r) * pi
    RectangleA = round(C * height)
    CircleA = round(float(r**2) * pi)
    print("Surface area of the cylinder: " + str(RectangleA) + str(CircleA))
    running = False;