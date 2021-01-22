#####Python Object and Classes
#####Create class
# class Person:
#     #contructor or init
#     def __init__(self, name):
#         self.name = name

#     def sayHello(self):
#         return "Hello " + self.name

# p1 = Person(name="Thang Phung")
# print(p1.sayHello())
# print(p1.name)

# p1.name = "Van Ha"
# print(p1.sayHello())



#####Hiding data fields
class BankAccount:
    #contructor or init
    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance

    def sayHello(self):
        return "Hello " + self.__name

    def deposit(self, money):
        self.__balance += money

    def withdraw(self, money):
        if self.__balance >= money:
            self.__balance -= money
            return money
        else:
            return "Insufficient funds"
    
    def checkbalance(self):
        return self.__balance

p1 = BankAccount(name="Thang Phung", balance=1000000)
print(p1.sayHello())

p1.deposit(money=1000000)
print(p1.checkbalance())
print(p1.withdraw(money=500000))
print(p1.checkbalance())