#list
int_list = [1,2,3,4]
print(int_list)
int_list.append(5)
print(int_list)

str_list = ["a","b","c"]
print(str_list)
print(len(str_list))
print(str_list[0]+" "+str_list[1])
print(str_list[0:2])

rand_list = [1,2,3,"a","b"]
print(rand_list)
rand_list.remove(2)
print(rand_list)
a = rand_list.count("a")
print("Count is:", a)

#tuples
ran_tup = (1,2,3,"a","b")
print("Tuples",ran_tup)

#ran_tup.append(5) # This won't work as we can't increase the size of tuples