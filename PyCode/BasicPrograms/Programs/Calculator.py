num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

operation = int(input('''Select operation
1. Add
2. Subtract
3. Multiply
4. Devide
'''))

if operation == 1:
    result = num1+num2
elif operation == 2:
    result = num1-num2
elif operation == 3:
    result = num1*num2
elif operation == 4:
    result = num1/num2
else:
    result = "Invalid Selection, Try Again"

print(result)


