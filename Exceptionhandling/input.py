
def div(a,b):
  try:
    d = a/b
    print(a)
    print(b)
    return d
  except ZeroDivisionError:
    print("Divide by zero exception")
    exit  
  

num1 = int(input("Pls enter first number:"))
num2 = int(input("Pls enter second number:"))
# print(num1,num2)
res= div(num1,num2)
print(f"Division of {num1} and {num2} is: {res}")
