#---------------------------------------
# Integrity Pledge: All work being 
# submitted is mine and mine alone: A.S
#---------------------------------------
# Name: Ahmed Sajid
# Program: L7Q2SA.py
#---------------------------------------
# Purpose: This program will explore a list that countains information
# about game scores.
#--------------------------------------
scores = ["ANA", 2000, "BOB", 1250, "MAX", 3000, "JOE", 1000]

# This will display the initial scores

def display_scores(scores):
    print()
    print('NAME\tSCORE')
    x = 0
    for i in scores:
        while (x < (len(scores))):
            print(scores[x], end ='\t')
            x = x + 1
            print(scores[x])
            x = x + 1
    
# This will allow the user to add a new score to the list and return the new list 
    
def add_score(scores):
    print()
    name1 = list((''))
    points1 = list((''))
    name = input("What is the player's name? ").upper()
    points = input('What score did ' + name + ' get? ')
    x = 0
    while x < 3:
        for i in name:
            name1.append(i)
            x = x + 2
    points1.append(points)
    name1 = name1[0:3]
    name1 = (''.join(name1))
    scores.append(name1)
    points1 = (''.join(points1))
    points1 = int(points1)
    scores.append(points1)
    return scores

# This will count the total sum of the scores.

def total_scores(scores):
    print()
    summ = 0
    for i in scores:
        if type(i) == int:
            summ = summ + i
    print('The scores total', summ ,'points.')

def manage_scores(scores):
    display_scores(scores)
    scores = add_score(scores)
    display_scores(scores)
    total_scores(scores)

manage_scores(scores)