from geometry import rectangle as rect
from geometry.circle import area, circumference as cfr
from display import display

while True:
    HomeMenuChoice = display.homeMenu()
    if HomeMenuChoice == 1:
        CircleMenuChoice, radius = display.circleMenu()

        if CircleMenuChoice == 1:
            areaOfCircle = area(radius)
            print("area of circle is", areaOfCircle)

        elif CircleMenuChoice == 2:
            cfcOfCircle = cfr(radius)
            print("circumference of circle is", cfcOfCircle)

        else:
            print("wrong choice")

    elif HomeMenuChoice == 2:
        RectMenuChoice, l, b = display.RectMenu()

        if RectMenuChoice == 1:
            areaOfRect = rect.area(l, b)
            print("area of rectangle is", areaOfRect)

        elif RectMenuChoice == 2:
            pmOfRect = rect.perimeter(l, b)
            print("perimeter of rectangle is", pmOfRect)

        else:
            print("wrong choice")

    elif HomeMenuChoice == 3:
        exit()

    else:
        print("wrong choice")

