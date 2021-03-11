import math
import cmath
a = float(input("\ta = ".expandtabs(3)))
b = float(input("\tb = ".expandtabs(3)))
c = float(input("\tc = ".expandtabs(3)))
print()
delata = (b**2)-(4*a*c)
if delta == 0:
    x0 = -b / (2*a)
    print("Rozwiązanie: \n\tx0 = {:.2f}".format(x0).expandtabs(3))
    elif delta > 0:
        x1 = (-b - math.sqrt(delta))/(2*a)
    