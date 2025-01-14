num1 = 10
num2 = 2
num3 = -7
num4 = 4.6244

def sum(num1, num2):
    return num1+num2

def sub(num1, num2):
    return num1-num2

def mul(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2

def mod(num1, num2):
    return num1%num2

def absol(num3):
    return abs(num3)

def roundoff(num4):
    return round(num4)

print("Sum of two numbers:",sum(num1,num2))
print("Substract of two numbers:",sub(num1,num2))
print("Multiplication of two numbers:",mul(num1,num2))
print("Division of two numbers:",div(num1,num2))
print("Division reminder(modulus) of two numbers:",mod(num1,num2))
print(f"Absolute value of {num3}: {absol(num3)}")
print(f"Round value of {num4}: {roundoff(num4)}")
