def homeMenu():
    print("1. circle")
    print("2. rectangle")
    print("3. exit")
    choice = int(input("enter your choice: "))
    return choice


def circleMenu():
    radius = eval(input("enter the radius of circle: "))
    print("1. area")
    print("2. circumference")
    choice = int(input("enter your choice: "))
    return choice, radius

def RectMenu():
    l = eval(input("enter the length: "))
    b = eval(input("enter the breadth: "))
    print("1. area")
    print("2. perimeter")
    choice = int(input("enter your choice: "))
    return choice, l, b
