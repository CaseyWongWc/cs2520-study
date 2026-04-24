"""4/21 ~1:41-1:48 PM - import / import as / from import."""
import math, random, os
print("math.sqrt(16) =", math.sqrt(16))
print("math.pi       =", math.pi)
print("random.randint(1,10) =", random.randint(1, 10))
print("os.getcwd()   =", os.getcwd())

import math as m
print("m.sqrt(25)    =", m.sqrt(25))

from math import sqrt, pi, pow
print("sqrt(36)      =", sqrt(36))
print("pow(2, 3)     =", pow(2, 3))

from datetime import datetime as dt
print("today         =", dt.now())
