import math

x1 = int(input("Skriv in x värdet för ett tal: "))
y1 = int(input("Skriv in y värdet för samma tal : "))
x2 = int(input("Skriv in x värdet för ett annat tal: "))
y2 = int(input("Skriv in y värdet för det nya värdet: "))

def pythagoras(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

print(f"The distance between the point {(x1,y1)} and the point {(x2,y2)} is {pythagoras(x1, y1, x2, y2)}")