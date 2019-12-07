#Get number from user and print final count of even odd numbers
even_number = odd_number = 0

number = int(input("Enter number, or enter 0 to exit: "))
while number !=0:
    if(number % 2 ==0):
        even_number = even_number +1
        number = int(input("Enter number, or enter 0 to exit: "))
    else:
        odd_number = odd_number + 1
        number = int(input("Enter number, or enter 0 to exit: "))


print(f"Even number count : ", even_number)
print("Odd number count : ", odd_number)

