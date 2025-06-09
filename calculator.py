#ASK FOR USER INPUUT
posible_operator = ['+', '-', '/', '*']
while True:
    try:
        print("Welcom to the Calculator ! \n")
        operator = input('Chose a operator (+, -, /, *) : ')
        if operator not in posible_operator:
            print("This operator is not disponible")
            continue
        number_1 = float(input("Enter the first number : "))
        number_2 = float(input("Enter the second number : "))
        break
    except ValueError:
            print("Enter a number !")
            continue
#DO THE CALCULATIONS
def calculation(operator, number_1, number_2):
    if operator == "/" and number_2 == 0:
        print("The result is indefined")
    elif operator == '+':
        print(f"{number_1 + number_2} \n")
    elif operator == '-':
        print(f"{number_1 - number_2} \n")
    elif operator == '/':
        print(f"{number_1 / number_2} \n")
    elif operator == '*':
        print(f"{number_1 * number_2} \n")

calculation(operator, number_1, number_2)
