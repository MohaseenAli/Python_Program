'''import math
print (math.pi)

from math import pi
print(pi)

from math import *
print (pi)
print(factorial(5))'''

# Import User define Module

import UDModule

UDModule.add(12,5)
UDModule.mul(12,5)

from UDModule import sub
sub(7,9)

from UDModule import *

add(12,5)
mul(12,5)
sub(12,5)
div(13,3)