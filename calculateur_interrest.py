principal = 0
rate = 0
time = 0

while True:
    try:
        principal = float(input("Enter your principal : "))
        if principal <= 0:
            print("Your Princiapl can't be equal or less than zero")
            continue
        rate = float(input("Enter your interrest rates in percent : "))
        if principal <= 0:
            print("Your Interrest rates can't be equal or less than zero")
            continue
        time = int(input("Enter your time in years : "))
        if principal <= 0:
            print("Your Time can't be equal or less than zero")
            continue
        break
    except ValueError:
        print("Enter a number !")
final_amount = principal * pow((1 + rate / 100 ), time)

print(f"Your final amount after {time} years of a {rate}% interrest is : {final_amount}")
