def add(x,y):
    return x+y
    
def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y
    
def divide(x,y):
    return x/y
    
def remainder(x,y):
    return x%y

title = print("Calculator!")    
operator = input("Enter: +,-,*,/,% :")
num1 = float(input("Enter first number :"))
num2 = float(input("Enter second number :"))

if(operator == "+"):
    print(str(num1) + " + " + str(num2) + " = " + str(add(num1, num2)))
elif(operator == "-"):
    print(str(num1) + " - " + str(num2) + " = " + str(subtract(num1, num2)))
elif(operator == "*"):
    print(str(num1) + " * " + str(num2) + " = " + str(multiply(num1, num2)))
elif(operator == "/"):
    if(num2 == 0):
        print("Can't divide by 0")
    else:
        print(str(num1) + " / " + str(num2) + " = " +str(divide(num1, num2)))
elif(operator == "%"):
    print(str(num1) + " % " + str(num2)+ " = " + str(remainder(num1, num2)))
else:
    print("Invalid operator")
    
