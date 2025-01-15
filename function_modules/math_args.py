import sys
def sum(num1, num2):
    return num1+num2

def sub(num1, num2):
    return num1-num2

def mul(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

a=sum(num1,num2)
b=sub(num1,num2)
c=mul(num1,num2)
d=div(num1,num2)
print(a,b,c,d)