#####Creating list in python
#Lists are mutable
# a = [1, 2, 3, 4, 5]
# print(a)
# b = ["welcome", 12, 1.5]
# print(b)
# c = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(c)
# d = list("welcome to")
# print(d)



#####Common List Operations
# tmp_list = list([1, 12, 32, 12, 3, 4])
# print(2 in tmp_list)
# print(0 not in tmp_list)
# print(sum(tmp_list))
# print(len(tmp_list))
# print(min(tmp_list))
# print(max(tmp_list))
# print(tmp_list * 2)



#####List slicing
# tmp_list = list([1, 2, 31, 12, 5, 78, 43])
# print(tmp_list[2: 5])
# print(tmp_list[:3])
# print(tmp_list[2:])



#####+ and * operators in list
# tmp_list = list([1, 2, 31, 12, 5, 78, 43])
# tmp_list_2 = list([1, 78, 100])
# print(tmp_list + tmp_list_2)
# print(tmp_list_2 * 3)



#####in or not in operato
# tmp_list = list([1, 2, 31, 12, 5, 78, 43])
# print(1 in tmp_list)
# print(12 not in tmp_list)



#####Traversing list using for loop
# tmp_list = list([1, 2, 31, 12, 5, 78, 43])
# for i in tmp_list:
#     print(i) 



#####Commonly used list methods with return type
# tmp_list = list([1, 2, 31, 12, 5, 78, 43, 1, 2, 3])
# tmp_list_2 = list([1, 2, 3, 101, 2])
# tmp_list.append(1000)
# print(tmp_list)
# print(tmp_list.count(1))
# tmp_list_2.extend(tmp_list)
# print(tmp_list_2)
# tmp_list_2.insert(0, 1991)
# print(tmp_list_2)
# tmp_list_2.remove(101)
# print(tmp_list_2)
# tmp_list_2.sort()
# print(tmp_list_2)
# tmp_list_2.reverse()
# print(tmp_list_2)
# pop_value = tmp_list_2.pop()
# print(pop_value)
# print(tmp_list_2)



#####List Comprehension
tmp_list = [x for x in range(10)]
tmp_list_2 = [x + 1 for x in range(10)]
tmp_list_3 = [x for x in range(10) if x % 2 == 0]
tmp_list_4 = [x * 2 for x in range(10) if x % 2 == 0]
print(tmp_list)
print(tmp_list_2)
print(tmp_list_3)
print(tmp_list_4)