
a =  float(input("Enter the number A:  "))
b =  float(input("Enter the number B: "))

operation = input("Enter operation you want to do (+, -, *, /)\n")


if  operation == "+":
    addation = a + b
    print("{} + {} = ".format(a,b),a + b)

elif operation == "-":
    subtraction = a - b    
    print("{} - {} = ".format(a, b),a - b)

elif operation == "/":
    division = a / b
    print("{} / {} = ".format(a, b),a / b)

elif operation == "*":
    if b == 0:
        print("Error! can't divide by zero")
    else:    
        multi = a * b
        print("{} * {} = ".format(a, b),a * b)
else:
    print("invaild input")
