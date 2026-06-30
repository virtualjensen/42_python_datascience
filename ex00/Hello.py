ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#list, modifiable 
ft_list[1] = "World!"

#tuple, immutable, but can be reassigned
ft_tuple = ("Hello", "United Arab Emirates!")

#set, LIFO
ft_set.remove("tutu!")
ft_set.add("Abu Dhabi!")

#dict, modifiable, key-value pairs
ft_dict["Hello"] = "42AbuDhabi!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)