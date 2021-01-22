#####Python Loops
#####For Loops
# tmp_list = [1, 2, 3, 5, 12]
# for i in tmp_list:
#     print(i)



#####range(a, b) Function
# for i in range(1, 10):
#     print(i)

# for i in range(10):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)



#####While loop
# count = 0
# while count < 10:
#     print(count)
#     count += 1



#####While loop + break statement
# count = 0
# while count < 10:
#     count += 1
#     if count == 5:
#         break
#     print("inside loop", count)
# print("out of while loop")



#####While loop + continue statement
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)
print("out of while loop")