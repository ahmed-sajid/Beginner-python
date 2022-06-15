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
answer = 'n'
i = 1

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
    value = ((int(step * -5) + 1))
    print(value, '', sep = " ", end = "")
    for i in range(1,5):
        value = (value + step)
        print(value, sep = "", end = " ")
        i = i + 1
    print('_')
  

# If the user choses to count down
    

elif (direction == 'd'):
    value = ((int(step * 5) + 1))
    print(value, '', sep = " ", end = "")
    for i in range(1,5):
        value = (value - step)
        print(value, sep = "", end = " ")
        i = i + 1
    print('_', end = " ")
    for i in range(5,11):
        value = (value - step)
        if (value != 1):
            print(value, sep = "", end = " ")
        i = i + 1  


# Finally the user gets to pick wether or not to view the answer.


print()
answer = input('Show answer (y or n)? ').lower()
if (answer == 'y'):
    print('Answer: 1')