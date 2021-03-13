import cmath
import math
a = float(input("podaj współczynnik a"))
b = float(input("podaj współczynnik b"))
c = float(input("podaj współczynnik c"))
delta =float( b**2 - 4*a*c)
if delta > 0:
    x1 = ((-b + math.sqrt(delta))/(2*a))
    x2 = ((-b - math.sqrt(delta))/(2*a))
elif delta == 0:
    x1=x2 = (-b/(2*a))
elif delta < 0:
    x1 = ((-b + cmath.sqrt(delta))/(2*a))
    x2 = ((-b - cmath.sqrt(delta))/(2*a))
if x1 == x2:
    print(x1)
else:
    print(x1," ",x2)
