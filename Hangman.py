#---------------------------------------
# Integrity Pledge: All work being 
# submitted is mine and mine alone: A.S
#---------------------------------------
# Name: Ahmed Sajid
# Program: Hangman
#---------------------------------------
# Purpose: This program will play hangman with you
#--------------------------------------

def play_hangman():
    endstat = input('Do you want to play hangman? ').lower()
    endstat = 'yes'
    while endstat != 'yes' and endstat != 'no':
        endstat = input('Do you want to play hangman? ').lower()
    print()
    if endstat == 'yes':
        Wordbank = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
        import random
        index = random.randint(0,(len(Wordbank)))
        secret = Wordbank[index-1]
        secret = 'baboon'
        secret_1 = []
        for i in range(0,len(secret)):
            secret_1.append(secret[i])

        word = []
        progress = list(('_')*len(secret))
        used = []
        x = 7
        print(f'Your word has {len(secret)} letters in it! Good Luck! ')
        while x > 0 :
            
            if (''.join(progress) == secret):
                print('You win')
                break

            print()
            print(f'You have {x} tries left!')
            print()
            guess = str(input('Guess a letter(type "used" for a list of used letters): '))
            while len(guess) > 1 and guess != 'used' and guess != secret:
                guess = str(input('Guess one letter(type "used" for a list of used letters): '))

            if guess == secret:
                print('You guessed the word!')

                x = -5



            elif guess == 'used':
                print(sorted(used))




            elif guess in secret_1:
                for i in range(len(secret_1)):
                    if guess in secret_1:
                        index = secret_1.index(guess)
                        progress[index] = (guess)
                        secret_1[index] = ''
                y = 0   
                for i in range(len(progress)):
                    print(f'{progress[y]} ', end = '')
                    y = y + 1
                    
                used.append(guess)
            
            elif guess in used:
                guess = guess.upper()
                print()
                print(f'You already Guessed {guess} !')
                print()
            else:
                print('Sorry, guess again!')
                print()
                used.append(guess)
                x = x - 1
        if (''.join(progress) != secret) and x != -5:
            print('Sorry, you lose!')
            print(f'The word was "{secret}.')

            
                        
                        
                    







play_hangman()