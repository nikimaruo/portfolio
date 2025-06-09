foods = []
prices = []
total = 0
ids = 0

while True:
    food = input("Enter a food to buy and the amount (exemple 2banana) (q to quit): ")
    if food.lower() == 'q':
        break
    else:
        try:
            price = float(input(f"Enter the price of one singular {food} : $"))
        except ValueError:
            print("Entre a price !")
            continue
        if float(food[0]) <= 0:
            print('Zero of something mean there nothing !')
        else:
            price_t = float(food[0]) * price
        foods.append(food)
        prices.append(price_t)

print("----YOUR CART----\n")
for food, price_t in zip(foods, prices):
    ids += 1
    print(f"{ids}: {food}, {price_t}$ ")

        
    
