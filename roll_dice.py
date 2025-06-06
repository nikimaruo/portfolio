import random
While True:
  choice = input("Roll the Dice? (y/n) : ").lower()
  if choice == "y":
    dice = (random.randint(1, 6), random.randint(1, 6))
    print(dice)
  elif choice == "n":
    print("Thank you for playing")
    break
  else:
    print("Invalide Choice")
