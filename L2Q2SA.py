#---------------------------------------
# Integrity Pledge: All work being 
# submitted is mine and mine alone: A.S
#---------------------------------------
# Name: Ahmed Sajid
# Program: L2Q2SA.py
#---------------------------------------
# Purpose: This program will ask the user
# for their name, then will use their name
# to ask for the amount of courses the user  
# is taking this year, then will ask the user
# how many courses they have taken previously.
# The program will then calculate the students
# tuition, the number of courses the student will
# have taken at the end of the year, and the amount
# of courses that the student has left to take.
#---------------------------------------

# This is where the student inputs thier data

name = input("What is the student's name? ").title()
Course = input('How many courses is ' + str(name) + ' taking this school year? ')
Course_taken = input('How many courses were completed previously? ') 
print()

# This is where the program takes the data and gives its output

print(str(name) + ' is taking ' + str(Course) + ' courses this school year.')
print('Each course costs $210 so tuition will total $', int(Course) * int(210), '.', sep = "")
print('Students must complete 40 courses to graduate.')
print('After finishing', int(Course) + int(Course_taken), 'courses,', name, 'will have', int(40) - (int(Course) + int(Course_taken)), 'courses left.')