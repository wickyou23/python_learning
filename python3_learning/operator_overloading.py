#####Python Operator Overloading
# +	        __add__(self, other)
# *	        __mul__(self, other)
# -	        __sub__(self, other)
# %	        __mod__(self, other)
# /	        __truediv__(self, other)
# <	        __lt__(self, other)
# <=	    __le__(self, other)
# ==        __eq__(self, other)
# !=        __ne__(self, other)
# >	        __gt__(self, other)
# >=        __ge__(self, other)

#####
#[index]    __getitem__(self, index)
#in         __contains__(self, value)
#len        __len__(self)
#str        __str__(self)

import math

class Circle:

    def __init__(self, radius):
        self.__radius = radius
    
    def setRadius(self, radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def area(self):
        return math.pi * self.__radius ** 2
    
    def __add__(self, another_circle):
        return Circle(self.__radius + another_circle.__radius)
    
    def __gt__(self, another_circle):
        return self.__radius > another_circle.__radius
    
    def __lt__(self, another_circle):
        return self.__radius < another_circle.__radius

    def __str__(self):
        return "Circle with radius: " + str(self.__radius)

c1 = Circle(4)
print(c1.getRadius())
c2 = Circle(5)
print(c2.getRadius())
c3 = c1 + c2
print(c3.getRadius())
print(c1 > c2)
print(c1 < c2)
print(c1.__str__())