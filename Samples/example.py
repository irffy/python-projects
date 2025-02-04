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

# import os
# import sys

# a = os.getenv("a")
# b= os.getenv("b")
# print(a,b)
# c= sys.argv[1]
# d= sys.argv[2]
# print(c,d)
# e= int(input("Enter 1st numb:"))
# f = int(input("Enter 2nd num:"))
# g= str(f)
# print(type(g))
# print(e+f)

# n = 10
# for i in range(1,n+1):
#     print(i)

# st = "Irfan"
# # for i in st:
# #     print(i)

# for i in st:
#     if i == "f":
#         continue
#     print(i)    
# Open file in write mode and write content

# with open("test.txt", "w") as f:
#   f.write("Hello Irfan!")

# with open("test.txt", "r") as f:
#     t = f.read()
#     print(t)

# with open("test.txt", "a") as f:
#     f.write("\nHello Ahmed!!")

# data = [
#     {"timeline": 1, "name": "Alice"},
#     {"timeline": 3, "name": "Bob"},
#     {"timeline": 9, "name": "Charlie"},
#     {"timeline": 11, "name": "David"},
#     {"timeline": 18, "name": "Eve"}
# ]
# for i in data:
#     # print(i)
#     print(i["timeline"])
#     print(i["name"])

# def decor(a):
#     print("Hello Ahmed!!")
#     return a

# @decor
# def test():
#   print("Hello Irfan!!")

# test()  

# str = "Irfan"
# rev = str[::-1]
# print(rev)

# arr = [2, 3, 6, 6, 5]
# du = list(set(arr)) #Removes duplicates using set and then converts to list
# du.sort(reverse=True)
# print(du)
# print(du[2])

# def isprime(n):
#     if n <2:
#       return False

#     for i in range(2, int(n**0.5)+1) :
#         if n%i ==0:
#             return False
#     return True        

# txt = "Hello World Python"
# print(txt)
# a = txt.split()
# print(a)
# print(" ".join(a[::-1]))

# def is_anagram(str1, str2):
#     return sorted(str1) == sorted(str2)

# # Example usage
# print(is_anagram("listen", "silent"))  # Output: True
# print(is_anagram("hello", "world"))    # Output: False


# def is_anagram(str1, str2):
#     return sorted(str1) == sorted(str2)

# i = "Irfan"
# j = "nafri"
# # x = is_anagram(i,j)    
# # print(x)
# m  = i.lower()
# print(m)
# k= (sorted(i))
# print(k)
# l= (sorted(j))
# print(l)

# if sorted(i) == sorted(j):
#     print("hi")
# else:
#     print("bye")    

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i == 0:
#             return False
#     return True        

# n = int(input("Enter a number:"))
# x= is_prime(n)   
# if x :
#     print("this is prime")
# else:
#  print("this is not prime")    

# word = input("Enter a word: ").lower()
# print(word)
# pattern = "aeiou"

# def count_vowels(word, pattern):
#     count = 0
#     for char in word:  # Iterate through each character in the input
#         if char in pattern:
#             count += 1
#     return count

# x = count_vowels(word, pattern)
# print(x)

# n = int(input("Enter a number: "))

# def snap_pop(n):
#     for i in range(1, n + 1):
#         if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
#             print("SnapCracklePop")  # Fixed: It should print all three
#         elif i % 3 == 0 and i % 5 == 0:
#             print("SnapCrackle")  # Handles multiples of 3 and 5
#         elif i % 3 == 0 and i % 7 == 0:
#             print("SnapPop")  # Handles multiples of 3 and 7
#         elif i % 5 == 0 and i % 7 == 0:
#             print("CracklePop")  # Handles multiples of 5 and 7
#         elif i % 3 == 0:
#             print("Snap")
#         elif i % 5 == 0:
#             print("Crackle")    
#         elif i % 7 == 0:
#             print("Pop")       
#         else:
#             print(i)  

# snap_pop(n)

n = int(input("Enter a number:"))

def snap_pop(n):
    
    for i in range(1,n+1):
        # print(i)
        j=""
        # print(j)
        if i%3 ==0:
            j = j +"Snap"
        if i%5 ==0:
            j = j +"Crackle"
        if i%5 ==0:
            j = j +"Pop"    
           
        print(j if j else i)


snap_pop(n)
