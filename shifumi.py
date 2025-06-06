user_choice = input("Make a choice (r/p/s) : ").lower()
if user_choice != 'r' and user_choice != 'p' and user_choice != 'r':
  print('Invalide Enter')
#MAKE A CHOICE FOR THE COMPUTER
computer_choice = ['r', 'p', 's']
computer_choice = random.choice(computer_choice)
#MAKE THE COMPUTER CHOICE INTO EMOJI
if computer_choice == 'r':
  print('🪨')
elif computer_choice == 'p':
  print('📄')
elif computer_choice == 's':
  print('✂')
if player_choice == computer_choice:
        print("It's a tie")
    elif (user_choice == "r" and computer_choice == "s") or \
         (user_choice == "p" and computer_choice == "r") or \
         (user_choice == "s" and computer_choice == "p"):
        print("Player wins")
    else:
        print("Computer wins")
