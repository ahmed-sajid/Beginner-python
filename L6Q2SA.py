#---------------------------------------
# Integrity Pledge: All work being 
# submitted is mine and mine alone: A.S
#---------------------------------------
# Name: Ahmed Sajid
# Program: L6Q2SA.py
#---------------------------------------
# Purpose: This program will rearrange the letters in a phrase and then
# allow the user to guess the original phrase
#--------------------------------------

# This will swap each adjacent charachter in the string and return the changed screen. If the string length
# is odd then it will take out the last charachter and add it back in after the shuffling.

def swap_adj(string):
        original = string
        s = list((string))
        string_1 = s
        even = len(string)
        s1 = s[-1]
        if even%2 != 0:
                del s[-1]
        
        for i in range(0, len(string)-1, 2):
                s[i], s[i+1] = s[i+1], s[i]
        
        if even%2 != 0:
                s.insert(0, s1)
        string = s
        string = (''.join(string))
        
        return string 
                  
   
 # This will swap the first 2 charachters and the last 2 charachters, and it will switch the 4th with the 3rd
 # charachter

def switch_letters(string):
        string = list((string))
        s = list((string))
        s1 = list((s[0:2]))
        s2 = list((s[len(string)-2:len(string)]))
        for i in range(0,2):
                a1, a2 = s2[0], s2[1]
                
        for i in range(len(string)-2,len(string)):
                a3, a4 = s1[0], s1[1]   
        
        a5 = s[3]
        a6 = s[len(string) - 3]
        s[0:2] = a1, a2
        s[len(string)-2:len(string)] = a3, a4
        s[3] = a6
        s[len(string) - 3] = a5
        string_1 = s
        string_1 = (''.join(string_1))
        return string_1

# Display the shuffled string to the user before obtaining the user's guess and 
# indicating wether the user's guess matches the original string. 


def get_guess(original, string_1):
        original = list((original))
        string_1 = list((string_1))
        for i in range(len(original)):
                original[i] = original[i].lower() 
                string_first = original[0]
        for i in range(len(string_1)):
                string_1[i] = string_1[i].lower()
        for i in string_1:
                if (i == string_first):
                        index = string_1.index(i)
                        string_1[index] = string_1[index].upper()
        print()
        print('Here are the letters:', ''.join(string_1))
        guess = input('Enter guess: ').lower()
        guess = guess.strip()
        guess = list((guess))
        
        step = 0
        for i in guess:
                if i.isspace() == False and (step != 1):
                        index = guess.index(i)
                        x = guess[index]
                        step = 1
                        space = list((guess[0:index]))
                        
        for i in space:
                if (i != x):
                        del guess[0]
        if (guess == original):
                print('You correctly guessed', ''.join(original), end = '.')
                print()
        else:
                print('The phrase was', ''.join(original), end = '.')
                print()
                               
        
        
# This function puts it all together.

def guess_phrase(original):
        string = swap_adj(original)
        string_1 = switch_letters(string)
        get_guess(original, string_1)






    

    
    
    






