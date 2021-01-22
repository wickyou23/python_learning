#####Python inheritance and polymorphism

# class Vehicle:

#     def __init__(self, name, color):
#         self.__name = name
#         self.__color = color

#     def getColor(self):
#         return self.__color

#     def setColor(self, color):
#         self.__color = color

#     def getName(self):
#         return self.__name

# class Car(Vehicle):

#     def __init__(self, name, color, model):
#         super().__init__(name, color)
#         self.__model = model
    
#     def __str__(self):
#         return self.getName() + self.__model + " in " + self.getColor() + " color"

# c = Car("Ford Mustang", "Red", "GT350")
# print(c.__str__())
# print(c.getName())



#####Multiple inheritance

class SuperClass1:
    
    def method_super1(self):
        print("This is a SuperClass1")

class SuperClass2:

    def method_super2(self):
        print("This is a SuperClass2")

class SubClass(SuperClass1, SuperClass2):

    def child_method(self):
        print("This is a SubClass")

s = SubClass()
s.method_super1()
s.method_super2()
s.child_method()



#####Overriding methods

class A:

    def __init__(self):
        self.__x = 1

    def m1(self):
        print("m1 from A")

class B(A):

    def __init__(self):
        self.__y = 2

    def m1(self):
        print("m1 from B")

c = B()
c.m1()



#####isinstance() function

print(isinstance(c, B))
print(isinstance(1.2, int))
print(isinstance([1, 2, 3, 4], list))