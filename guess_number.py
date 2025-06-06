import random
num_try = 0
pc_number = random.randint(1, 100)
while True:
    try:
        user_number = int(input('Devine le Nombre : '))
        if user_number == pc_number:
          num_try = num_try + 1
          print(f"Tu as deviné le nombre en {num_try} essai !")
          break
        elif user_number < pc_number:
          num_try = num_try + 1
          print(f"Essaie encore c'est trop petit ")
        elif user_number > pc_number:
          num_try = num_try + 1
          print(f"Essaie encore c'est trop grand ")
    except ValueError:
        print("Entre un chiffre Gros bouffon!")
            
