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
already_guessed= ''
correct_letters = ''
endstat = ""
secret = Wordbank[index]
secret = list(('baboon banana'))




def play_game():
    print(secret)
    secret1 = list((secret))
    revealed = '_ ' * len(secret)
    revealed = revealed.split()
    revealed = list((revealed))
    gamestat = input('Do you want to play hangman? ')
    endstat = 'no'
    while (gamestat != 'yes') and (gamestat != 'no'):
        gamestat = input('Yes or No, Do you want to play hangman? ').lower
    while (endstat == 'no'):
        guess = input('Guess a letter: ')
        for i in guess:
            if i in secret1:
                for i in secret1:
                    index = secret.find(guess)
                    secret1[i] = 0
                    revealed[index] = i
                   
                    if i in secret1:
                        index = secret.find(i)
                        secret1[i] = 0
                        revealed[index] = i
            print(revealed)
                        
                
                
                

                
            
            
            
        
               

play_game()
    
    
    
        

    



    
    



    
