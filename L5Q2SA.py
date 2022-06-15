#---------------------------------------
# Integrity Pledge: All work being 
# submitted is mine and mine alone: A.S
#---------------------------------------
# Name: Ahmed Sajid
# Program: L5Q1SA.py
#---------------------------------------
# Purpose: This Program will play rock 
# paper scissors with the user
#---------------------------------------

# Display the title and the rules

def show_rules():
    print('*** Rock-Paper-Scissors ***')
    print()
    print('Rules:\tEach player chooses either rock, paper\t, or scissors.\n\tThe winner is determined by the following rules: ')
    print('\t\trock smashes scissors \t-> rock wins\n\t\tscissors cuts paper\t-> scissors wins\n\t\tpaper covers rock\t -> paper wins')
    print()
    return


# Ask the player for a selection and save it
def get_player_choice():
    player = input('Player choice: ').lower()
    return player

def get_computer_choice():
    import random
    computer = random.randint(1,3)
    if (int(computer) == int(1)):
        computer = 'rock'
    elif (int(computer) == int(2)):
        computer = 'paper'
    elif (int(computer) == int(3)):
        computer = 'scissors'
    print('Computer choice:', computer)
    print()
    return computer 

# Randomly generates a number and assigning it a value for the computer 

def declare_winner(player,computer):
    if (player == 'rock') and (computer == 'rock'):
        print('Winner: Draw')
    elif (player == 'rock') and (computer == 'paper'):
            print('Winner: computer')
    elif (player == 'rock') and (computer == 'scissors'):
            print('Winner: player') 
    elif (player == 'paper') and (computer == 'rock'):
            print('Winner: player')
    elif (player == 'paper') and (computer == 'paper'):
            print('Winner: Draw ')
    elif (player == 'paper') and (computer == 'scissors'):
            print('Winner: computer')
    elif (player == 'scissors') and (computer == 'rock'):
            print('Winner: computer')
    elif (player == 'scissors') and (computer == 'paper'):
            print('Winner: player')
    elif (player == 'scissors') and (computer == 'scissors'):
            print('Winner: Draw')
    
# play_game puts it all together. The above helper functions are used to play
# rock paper scissors with the player

def play_game():
    show_rules()
    player = get_player_choice()
    computer = get_computer_choice()
    declare_winner(player,computer)

    
    






