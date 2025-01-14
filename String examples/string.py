# print("Hello World!!")
hello = "Hello Irfan!!"
print(hello)
print(f"The total string is: {hello}")
first = hello.split(" ")[0]
second = hello.split(" ")[1]
print(first)
print(second)
third = second.split("!")[0]
print(third)
upper = print(f"Uppercase of first string: {first.upper()}")

str1 = "Irfan"
str2 = "Ahmed"
print(f"Fullname: {str1+" "+str2}")
length = len(str1+" "+str2)
print("Full string length:", len(str1+" "+str2))
# print("Full string length:", length)
print(f"Length of first name string is: {len(str1)}")
