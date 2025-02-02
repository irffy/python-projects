# lis = [1,2,3,4]
# # print(lis)
# # lis.append(5)
# # lis.remove(2)
# # print(lis)
# # add = lis[0]+lis[2]
# # print(add)

# str = "Hello Irfan!"
# x= str.split(" ")
# print(x)
# y = str.count("l")
# print(y)
# z= str.strip("!")
# print(z)
# text = "___Some spaces around___"
# stripped_text = text.strip("_")
# print("Stripped text:", stripped_text)

# import re
# text = "apple,banana,orange,grape"
# pattern = "apple"
# res = re.search(pattern,text)
# print(res)
# if res:
#     print("Pattern found")
# else:
#     print("String not found")    

import os
import sys

a = os.getenv("a")
b= os.getenv("b")
print(a,b)
c= sys.argv[1]
d= sys.argv[2]
print(c,d)
e= int(input("Enter 1st numb:"))
f = int(input("Enter 2nd num:"))
print(e+f)