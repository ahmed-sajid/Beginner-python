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
    print('Rules:\tEach player chooses either rock, paper\t, or scissors.\t\n\tThe winner is determined by the following rules: ')
    print('\t\trock smashes scissors \t-> rock wins\n\t\tscissors cuts paper \t-> scissors win\n\t\tpaper covers rock\t -> paper wins')
    print()
    return


# Ask the player for a selection and save it

def get_computer_choice():
    player = input('Player choice: ').lower()
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
    return player,computer 

# Randomly generates a number and assings it a value for the computer 

def declare_winner(player,computer):
    if (player == 'rock') and (computer == 'rock'):
        print('Draw')
    elif (player == 'rock') and (computer == 'paper'):
            print('Winner: computer')
    elif (player == 'rock') and (computer == 'scissors'):
            print('Winner: rock') 
    elif (player == 'paper') and (computer == 'rock'):
            print('Winner: computer')
    elif (player == 'paper') and (computer == 'paper'):
            print('Winner: Draw ')
    elif (player == 'paper') and (computer == 'scissors'):
            print('Winner: computer')
    elif (player == 'scissors') and (computer == 'rock'):
            print('Winner: computer')
    elif (player == 'scissors') and (computer == 'paper'):
            print('Winner: scissors')
    elif (player == 'scissors') and (computer == 'scissors'):
            print('Winner: Draw')
    
# Play game puts it all together  where the above helper functions are used to play
# rock paper scissors with the player

def play_game():
    show_rules()
    
    player, computer = get_computer_choice()
    
    declare_winner(player,computer)
    
    






