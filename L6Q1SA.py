#---------------------------------------
# Integrity Pledge: All work being 
# submitted is mine and mine alone: A.S
#---------------------------------------
# Name: Ahmed Sajid
# Program: L6Q1SA.py
#---------------------------------------
# Purpose: This program will analyze a sequence of user inputs; it will
# prompt the user for a sentence, it will determine various charachteristics of 
# the sentence, and it will display permutations of the original sentence
#--------------------------------------

# Prompt user for a sentence that is greater than 10 charachters and ends in a '.'

def get_input():
    sentence = input('Enter 10 or more chars ending with a period: \n-> ')
    senlen = len(sentence)
    while (senlen < 10) or (sentence[-1] != '.'):
        sentence = input('-> Error! Try again: ')
        senlen = len(sentence)
    string = sentence
    return string

# Prints out the ogirinal string, determins and outputs the : string lentgh, second char, second last char, and it will
# switch the first 3 chars and the last 3 chars


def explore_chars(string):
    print()
    print('Original:', string)
    print('Length: ', len(string), 'chars')
    print('2nd char: ', string[1])
    print('2nd last: ', string[-2])
    x = int(len(string))
    print('Switched: ', string[(x-3):(x)],string[3:(x-3)], string[0:3], sep = "")


# Calculates the sum of all digits in the string

def sum_digits(string):
    summ = 0
    for x in string:
        if x.isdigit() == True:
            y = int(x)
            summ = summ + y
    print('Digit sum: ',summ)

# Master string puts it all together

def explore_string():
    string = get_input()
    explore_chars(string)
    sum_digits(string)



    

    
    
    






