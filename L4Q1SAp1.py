#  ----------------------------------------------------
#
#  Academic Integrity Pledge: 
#  I hereby acknowledge this program is my own work. 
#  I have not copied from anyone/anywhere 
#  and I have not let others copy my work.
#
#  Name:      Ahmed Sajid
#  Program:   L4Q1SA.py
#  
#  Purpose:   This program will display either an ascending 
#  or descending sequence of integers based on user input values
#  with one number from the sequence missing.
#  ----------------------------------------------------

# These are just variables used in the program

step = 0
direction = 'default'
value = 0
ss = 0
value = 0
value_2 = 0
value_3 = 0
value_4 = 0
value_5 = 0
value_6 = 0
value_7 = 0
value_8 = 0
value_9 = 0
value_10 = 0
value_11 = 0
answer = 'n'

# First the program will ask the user for an initial value to act as the step

step = int(input('Enter number (1 to 10): '))
while (int(step) < 1) or (int(step) > 10):
    if (int(step) < 1) or (int(step) > 10):
        step = int(input('-> Error! Try again: '))
print()   

# Then it will ask whether they want to count up or down

direction = input('Count up or down (U or D): ').lower()
while (direction != 'u') and (direction != 'd'):
    if (direction != 'u') and (direction != 'd'):
        direction = (input('-> Invalid! Try again: ')).lower()   
    

print()

# It will now print a series of values with one integer missing

print('What is the missing number? ')

# If the user choses to count up 

if (direction == 'u'):
    while (ss != 6):
        value = ((step * -5) + 1)
        value_2 = (int(value + int(step)))
        value_3 = (int(value_2 + int(step)))
        value_4 = (int(value_3 + int(step)))
        value_5 = (int(value_4 + int(step)))
        value_6 = (int(value_5 + int(step)))
        ss = 6
        print(value , value_2 , value_3 , value_4 , value_5 ,' _ ' , sep = " ")

# If the user choses to count down

elif (direction == 'd'):
    while (ss != 11):
        value = ((step * -5) + 1)
        value_2 = (int(value + int(step)))
        value_3 = (int(value_2 + int(step)))
        value_4 = (int(value_3 + int(step)))
        value_5 = (int(value_4 + int(step)))
        value_6 = (int(value_5 + int(step)))
        value_7 = (int(value_6 + int(step)))
        value_8 = (int(value_7 + int(step)))
        value_9 = (int(value_8 + int(step)))
        value_10 = (int(value_9 + int(step)))
        value_11 = (int(value_10 + int(step)))
        ss = 11
        print(value_11 , value_10 , value_9 , value_8 , value_7 ,' _ ' , value_5, value_4, value_3, value_2, value, sep = " ")
print()

# Finally the user gets to pick wether or not to view the answer.

answer = input('Show answer (y or n)? ').lower()
if (answer == 'y'):
    print('Answer: 1')