#  ----------------------------------------------------
#
#  Academic Integrity Pledge: 
#  I hereby acknowledge this program is my own work. 
#  I have not copied from anyone/anywhere 
#  and I have not let others copy my work.
#
#  Name:      Ahmed Sajid
#  Program:   L4Q2SA.py
#  
#  Purpose:   This program will take an input from the user
#  then it will generate a random integer and use the two
#  numbers to perform serial subtraction. The program
#  will tally up the total number of questions and the 
#  user's score and display them at the end.
#  ----------------------------------------------------

tot = 0
score = 0

# First the program will get a minuend from the user's input

minn= int(input('Choose a number between 30 and 50 : '))

while (minn < 30) or (minn > 50):
    minn = int(input('-> Invalid. Try again: '))
print()

# Then the program will generate a random subtrahend

import random
sub = int(random.randint(5,9))

# Then the computer will start doing its serial subtractions

print('Serial subtraction:')

while (minn >= sub):
    print(minn, '-', sub, sep = " ", end = "")
    user = int(input(' = '))
    answer = int(minn - sub)
   
    if (answer == user):
        print('-> Correct! ')
        minn = answer
        print()
        tot = int(tot + 1)
        score = int(score + 1)
   
    else:
        print('-> Incorrect!')
        minn = answer
        print()
        tot = int(tot + 1)
        
# Now the computer will display the total number of questions and the user's score

print('Total questions: ', tot, sep = "")
print('Total correct:   ', score, ' (', int((int(score) / int(tot) * 100)), '%)', sep = "")
        

    



    