import random


user_move = input("What is your move: ")
moves = ["scissors", "rock", "paper"]
computer_move = random.choice(moves)

if user_move == computer_move:
    print("Draw")
elif user_move == 'rock' and computer_move == 'paper':
    print("Computer Wins")
elif user_move == 'paper' and computer_move == 'rock':
    print("User Wins")
elif user_move == 'scissors' and computer_move == 'paper':
    print("User Wins")
elif user_move == 'paper' and computer_move == 'scissors':
    print("Computer Wins")
elif user_move == 'rock' and computer_move == 'scissors':
    print("Computer Wins")
else:
    print("You Win")