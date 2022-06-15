#  ----------------------------------------------------
#
#  Academic Integrity Pledge: 
#  I hereby acknowledge this program is my own work. 
#  I have not copied from anyone/anywhere 
#  and I have not let others copy my work.
#
#  Name:      Ahmed Sajid
#  Program:   MT1Q7SA
#
#  ----------------------------------------------------
import random


# Variables

Wordbank = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

index = random.randint(0,2)
secret = ''
already_guesses = ''
correct_letters = ''
endstat = ""


def play_game():
    secret = Wordbank[index]
    print(secret)
    revealed = ('_ ' * len(secret))
    gamestat = input('Do you want to play hangman? ')
    endstat = 'no'
    while (gamestat != 'yes') and (gamestat != 'no'):
        gamestat = input('Yes or No, Do you want to play hangman? ').title
    while (endstat == 'no'):
        guess = input('Guess a letter: ')
        if guess in secret:
                i = secret.find(guess)
                print(i)
                revealed = revealed[:i] + guess + revealed[i+1]
                print(revealed)
                
            
            
            
        
               

play_game()
    
    
    
        

    



    
    



    
