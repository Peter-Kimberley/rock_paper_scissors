# Rock paper scissors game


# Imports extra python functions in standard libraries
import random
import time

rock = 1 
paper = 2 
scissors = 3

# These ar the initial rules of the game
names = {rock: "Rock", paper: "paper", scissors: "Scissors"}
rules = {rock: scissors, paper: rock, scissors: paper}

player_score = 0
computer_score = 0

# Defining the start function
def start():
    print("Let's play a game ofrock, paper, scissors")
    while game():
        pass
    scores()

# Defining the the game function
def game():
    player = move()
    computer = random.randint(1, 3)
    result (playe, computer)
    return play_again()

# Defining the move function
def move():
    while True:
        print()
        player = raw_input("Rock = 1\nPaper = 2\nScissors =3\nMake a move: " )
        try:
            player = int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print("Oops! I didn't understand that. Please enter 1, 2, or 3.")