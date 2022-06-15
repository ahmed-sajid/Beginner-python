#---------------------------------------
# Integrity Pledge: All work being 
# submitted is mine and mine alone: A.S
#---------------------------------------
# Name: Ahmed Sajid
# Program: L2Q1SA.py
#---------------------------------------
# Purpose: This program will ask the user
# for a series of pieces of information
# and will use the resulting information by
# incorporating it into a story.
#---------------------------------------

# This is where the user inputs their information

print('Please enter the following:')
A = input('\t1. a place: ').title()
B = input('\t2. a family member: ')
C = input('\t3. a type of food: ')
D = input('\t4. an adjective: ')
E = input('\t5. an activity: ')
print()

# A story will be made using the information from above

print('Here is a story using your words:') 
print()

#This is the resulting story

print('After the pandemic, I want to travel to (1) ' + A + ' with my (2) ' + B + ".")
print('I must try the (3) ' + C + " there because I heard it's really (4) " + D + ".")
print( 'After eating, we will be doing a lot of (5) ' + E + '.', end = "")
print(" I can't wait!") 

