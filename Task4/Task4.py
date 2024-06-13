import random

choices = ['rock', 'paper', 'scissors']
my_store = 0
computer_score = 0

while True:
    my_choice = input("Choose rock, paper, or scissors: ").lower()
    while my_choice not in choices:
        my_choice = input("Invalid choice. Choose rock, paper, or scissors: ").lower()

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if my_choice == computer_choice:
        print("It's a tie!")
        
    elif (my_choice == 'rock' and computer_choice == 'scissors') or \
         (my_choice == 'scissors' and computer_choice == 'paper') or \
         (my_choice == 'paper' and computer_choice == 'rock'):
        print("User Winner,Congratulations!")
        my_store += 1
        
    else:
        print("User Lost,Bad luck!")
        computer_score += 1

    print(f"Scores: You - {my_store}, Computer - {computer_score}")

    play_again = input("play again? (yes/no): ").lower()
    if play_again != 'yes':
        break
