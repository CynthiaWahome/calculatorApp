#ask the user what they want to do
#ask the user to input first number
#ask the user to input second number
#print your answer


greeting = print("Hello there!")
print(input("Are you ready to do some calculations? "))

if "Yes":
    calculation = input('Addition, Subraction, Multiplication or Division?' '')

    if calculation == "Addition":
        num1 = int(input("Input First Number: "))
        num2 = int(input("Input Second Number: "))

    print (f"The sum of the two numbers: {num1} and {num2} is: {sum}")
    print("**********************")

