#####Python Dictionaries
#Dictionaries are mutable
# tmp_dict = {"a": "Apple", "b": "Banana"}
# tmp_empty_dict = {}
# print(tmp_dict)
# print(tmp_empty_dict)



#####Retrieving, modifying and adding elements in the dictionary
# tmp_dict = {"a": "Apples", "b": "Bananas"}
# tmp_dict["c"] = "Cherries"
# print(tmp_dict)
# print(tmp_dict["a"])



#####Deleting Items from the dictionary.
# tmp_dict = {"a": "Apples", "b": "Bananas", "c": "Cherries", "d": "Dragon fruit"}
# del tmp_dict["d"]
# print(tmp_dict)



#####Looping items in the dictionary
# tmp_dict = {"a": "Apples", "b": "Bananas", "c": "Cherries", "d": "Dragon fruit"}
# for k in tmp_dict:
#     print(k, ":", tmp_dict[k])



#####Find the length of the dictionary
# tmp_dict = {"a": "Apples", "b": "Bananas", "c": "Cherries", "d": "Dragon fruit"}
# print(len(tmp_dict))



#####Equality Tests in dictionary
#You can't use other relational operators like <, >, >=, <= to compare dictionaries
# tmp_dict = {"a": "Apples", "b": "Bananas", "c": "Cherries", "d": "Dragon fruit"}
# tmp_dict_2 = {"a": "Apples", "b": "Bananas", "c": "Cherries"}
# tmp_dict_3 = {"b": "Bananas", "a": "Apples", "d": "Dragon fruit", "c": "Cherries"}
# print(tmp_dict != tmp_dict_2)
# print(tmp_dict == tmp_dict_3)



#####Dictionary methods
# tmp_dict = {"a": "Apples", "b": "Bananas", "c": "Cherries", "d": "Dragon fruit"}
# pop_value = tmp_dict.popitem()
# print(pop_value)
# print(tmp_dict)
# print(tmp_dict.keys())
# print(tmp_dict.values())
# print(tmp_dict.get("a"))
# pop_key_value = tmp_dict.pop("a")
# print(pop_key_value)
# print(tmp_dict)
# tmp_dict.clear()
# print(tmp_dict)