from metro import *
import math

a = "4.33"

a = float(a)

print(a)
print((a - math.floor(a)) * 100 * 60 + 3600 * math.floor(a) )