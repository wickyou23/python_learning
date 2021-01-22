#####Python Strings
# name = "Thang Phung"    #as a String
# myChar = 'T'            #as a Character
# emptyStr = str()
# newStr = str("Declare new string")
# print(name, emptyStr, myChar, newStr)



#####Strings in Python are Immutable.
# tmpStr1 = "ThangPhung"      #id() to get that memory address
# tmpStr2 = "ThangPhung"
# print(id(tmpStr1), id(tmpStr2))
# tmpStr1 += "VanHa"
# print(id(tmpStr1))



#####Operations on string
# name = "ThangPhung"
# name2 = "Welcome to " + "ThangPhung"
# name3 = "Noma " * 3
# print(name[0])
# print(name[1])
# print(name2)
# print(name3)



#####Slicing string
#The start index and end index are optional. If omitted then the default value of start index is 0 and that of end is the last index of the string.
# name = "Welcome to Python 3"
# print(name[1:3])
# print(name[:5])
# print(name[3:])
# print(name[1:-3])



#####ord() and chr() Functions
# chr_to_ASCII = ord('a')
# ASCII_to_char = chr(100) 
# print(chr_to_ASCII, ASCII_to_char)



#####String Functions in Python
# tmpStr = 'Welcome_to_Python3'
# print(len(tmpStr))      
# print(max(tmpStr))      #returns character having highest ASCII value
# print(min(tmpStr))      #returns character having lowest ASCII value



#####in and not in operators
# tmp = "Welcome to Python3"
# tmpToCompare = "to"
# print(tmpToCompare in tmp)
# print(tmpToCompare not in tmp)



#####String comparison
#Python compares string lexicographically i.e using ASCII value of the characters
# name = "Thangphung"
# name_2 = "VanHa"
# print(name >= name_2)



#####Iterating string using for loop
#By default, print() function prints string with a newline, we change this behavior by passing named keyword argument called end as follows.
# name = "ThangPhung"
# for i in name:
#     print(i, end=' ')



#####Testing strings
#isalnum()	Returns True if string is alphanumeric
#isalpha()	Returns True if string contains only alphabets
#isdigit()	Returns True if string contains only digits
#isidentifier()	Return True is string is valid identifier
#islower()	Returns True if string is in lowercase
#isupper()	Returns True if string is in uppercase
#isspace()	Returns True if string contains only whitespace
# print("Welcome".isdigit())
# print("2012".isdigit())
# print("Welcome".isalpha())



#####Searching for Substrings
# s = "Welcome to python"
# print(s.startswith("wel"))
# print(s.endswith("on"))
# print(s.find("come"))
# print(s.rfind("thon"))
# print(s.count("o"))



#####Converting Strings
# s = "Converting Strings in Python3"
# print(s.capitalize())
# print(s.upper())
# print(s.title())
# print(s.swapcase())
# print(s.replace("Python3", "Python"))


import re

def strStr(haystack, needle):
    n = len(haystack)
    m = len(needle)
    if m == 0:
        return 0
    elif m > n:
        return -1
    else:
        pass

    # txt = "The rain in Spain {0}".format(1)
    
    # x = re.search(r"\b\b", haystack)

    # return f

haystack = "aaaaa"
regex = r"({0})".format("bba")
x = re.search(regex, haystack)
print(x.span())