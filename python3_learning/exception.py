#####Python Exception Handling

# try:
#     f = open("somefile.txt", "r")
#     print(f.read())
#     f.close()
# except IOError:
#     print("File not found")



#####Full try statement

# try:
#     num1, num2 = eval(input("Enter two number, separated by a comma: "))
#     rs = num1/num2
#     print("Result is ", rs)
# except ZeroDivisionError:
#     print("Division by zero is error !!")
# except SyntaxError:
#     print("Comma is missing. Enter numbers separated by comma like this 1, 2")
# except:
#     print("Wrong input")
# else:
#     print("No exceptions")
# finally:
#     print("This will execute no matter what")



#####Raising exceptions

# def enterage(age):
#     if age < 0:
#         raise ValueError("Only positive integers are allowed")

#     if age % 2 == 0:
#         print("Age is even")
#     else:
#         print("Age is odd")

# try:
#     num = int(input("Enter your age: "))
#     enterage(num)
# except ValueError:
#     print("Only positive integers are allowed")
# except:
#     print("Something is wrong")



#####Using Exception objects

# try:
#     number = eval(input("Enter your age: "))
#     print("The number entered is", number)
# except NameError as ex:
#     print("Exception:", ex)



#####Creating custom exception class

class NegativeAgeException(RuntimeError):
    def __init__(self, age):
        super().__init__()
        self.age = age
    
def enterage(age):
    if age < 0:
        raise NegativeAgeException(age)

    if age % 2 == 0:
        print("Age is even")
    else:
        print("Age is odd")

try:
    num = int(input("Enter your age: "))
    enterage(num)
except NegativeAgeException:
    print("Only positive integers are allowed")
except:
    print("Something is wrong")
else:
    print("No except")