#####Python file handler
#####Write a file
# wf = open("sources/file_handler.txt", "w")
# wf.write("Phùng Liên Thằng\n")
# wf.write("Nguyễn Đình Vân Hà\n")
# wf.close()



#####Read a file
# rf = open("sources/copyright.txt", "r")
# content_file = rf.read()
# rf.close()
# print(content_file)



#####Appending data 
# af = open("sources/file_handler.txt", "a")
# af.write("Phùng Liên Huy")
# af.close()



#####Looping through the data using for loop
# lf = open("sources/file_handler.txt", "r")
# for l in lf:
#     print(l)
# lf.close()



#####Writing binary data
# import pickle
# wbf = open("sources/file_handler.dat", "wb")
# pickle.dump(11, wbf)
# pickle.dump("This is a file binary", wbf)
# pickle.dump([1, 2, 3, 4], wbf)
# wbf.close()



#####Open binary data
import pickle
rbf = open("sources/file_handler.dat", "rb")
print(pickle.load(rbf))
print(pickle.load(rbf))
print(pickle.load(rbf))
rbf.close()
