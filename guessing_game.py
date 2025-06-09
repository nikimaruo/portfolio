questions = ("What large animal is known for its trunk? :",
            'Which planet is known as the "Red Planet"? :', 
            "How many days are in a leap year? :", 
            "What is the capital city of France? :", 
            "What is 2 + 2 * 2? :")
options =(("A. Giraffe", "B. Elephant", "C. Rhinoceros", "D. Hippopotamus"),
         ("A. Jupiter", "B. Earth", "C. Venus", "D. Mars"),
         ("A. 360", "B. 365", "C. 366", "D. 367"),
         ("A. Rome", "B. Berlin", "C. Paris", "D. London"),
         ("A. 8", "B. 6", "C. 4", "D. 10"))
answers = ("B", "D", "C", "C", "B")
guess = []
score = 0
question_number = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_number]:
        print(option)
    guesss = input("Enter your guess (A/B/C/D) :").capitalize()
    if guesss == answers[question_number]:
        print("YOU GUESSED RIGHT ! +1")
        score += 1
    else:
        print(f"YOU GUESSED WRONG ! +0")
    guess.append(guesss)
    question_number += 1

print("SCORE \n")
print(f"Win : {score} \n")
lose = 5 - score 
print(f"Lost : {lose}")
