from geometry import rectangle as rect
from geometry.circle import area, circumference as cfr

print("1. circle")
print("2. rectangle")
choice = int(input("enter your choice: "))

if choice == 1:
    radius = eval(input("enter the radius of circle: "))
    print("1. area")
    print("2. circumference")
    choice = int(input("enter your choice: "))

    if choice == 1:
        areaOfCircle = area(radius)
        print("area of circle is", areaOfCircle)

    elif choice == 2:
        cfcOfCircle = cfr(radius)
        print("circumference of circle is", cfcOfCircle)

    else:
        print("wrong choice")

elif choice == 2:
    l = eval(input("enter the length: "))
    b = eval(input("enter the breadth: "))
    print("1. area")
    print("2. perimeter")
    choice = int(input("enter your choice: "))

    if choice == 1:
        areaOfRect = rect.area(l, b)
        print("area of rectangle is", areaOfRect)

    elif choice == 2:
        pmOfRect = rect.perimeter(l, b)
        print("perimeter of rectangle is", pmOfRect)

    else:
        print("wrong choice")

else:
    print("wrong choice")