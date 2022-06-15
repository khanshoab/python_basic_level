# We are using in our calculator +add, -subtract, *multiply, /divide.

num1 = int(input("please Enter the value1::"))
num2 = int(input("please Enter the value2::"))
opr = input("Please Enter the operator only four types operator (+, -, *, /)::")

if opr == "+":
    print(num1 + num2)
elif opr == "-":
    print(num1 - num2)
elif opr == "*":
    print(num1 * num2)
elif opr == "/":
    print(num1 / num2)
else:
    print("Please Enter the valid operator")
