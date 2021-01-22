#####Python Functions
# def passFunction():
#     pass
# print(passFunction())

# def hellowordFunction():
#     print("Hello word")
# print(hellowordFunction())



#####Function with return value
# def sum(start, end):
#     if start >= end:
#         print("start should be less than end")
#         return

#     rs = 0
#     for i in range(start, end):
#         rs += i
#     return rs
# s = sum(10, 100)
# print(s)

# def test():
#     i = 100
# print(test())



#####Global variables vs local variables
# global_var = 12
# def func():
#     local_var = 10
#     print(global_var)
#     print(local_var)
# print(func())

# def increment():
#     global global_var
#     global_var += 1
#     print(global_var)
# increment()
# print(global_var)



#####Argument with default values
# def func(i, j = 100):
#     print(i, j)
# func(1)
# func(1, 200)



#####Keyword arguments
# def named_args(name, greeting):
#     print(greeting + " " + name)
# named_args(name="Thang", greeting="Goodbye")
# named_args(greeting="Good morning", name="Ha")



#####Mixing Positional and Keyword Arguments
# def func(a, b, c):
#     print(a, b, c)
# func(12, b=11, c=12)
# func(100, c=9, b=11)



#####Returning multiple values from Function
def bigger(a, b):
    if a > b:
        return (a, b)
    elif b > a:
        return (b, a)
    else:
        return
rs = bigger(101, 101)
print(type(rs))
