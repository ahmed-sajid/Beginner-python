#---------------------------------------
# Integrity Pledge: All work being 
# submitted is mine and mine alone: A.S
#---------------------------------------
# Name: Ahmed Sajid
# Program: L7Q1SA.py
#---------------------------------------
# Purpose: This program will simulate an election. It will display the candidates
# generate and display the votes, and tally the results.
#--------------------------------------

# This will print the voting options by displaying each candidate

def display_candidates(candidates):
    print()
    x = 0
    print('Voting options: ')
    while (x < len(candidates)):
        print('-> Candidate', x, ': ', candidates[x])
        x = x + 1
    return

# This will create a list of random integers to simulate votes in an election.

def generate_votes(candidates):
    print()
    x = 0
    print('Generating', (len(candidates) * 10), 'votes between', x, 'and ', end = '')
    for i in candidates:        
        x = x + 1
    print(x-1)
    import random
    x = 0
    summ = 0
    votes = list(('_' * (len(candidates) * 10)))
    candidates = list((candidates))
    for i in range(0, 10 * len(candidates)):
        rand = (random.randint(0, len(candidates) - 1))
        votes[x] = rand
        x = x + 1
        n = len(votes)
    return votes

# This will display the generated votes

def display_votes(votes):
    n = len(votes)
    x = 0
    summ = 0
    for i in range(n):
        if x%8 == 0:
            print('\n')
        print(votes[x], '\t', end = "")            
        
        x = x + 1

# This will add up all the votes and show the total for each candidate

def tally_votes(candidates, votes):
    running = len(candidates)
    n = len(votes)
    x = 0
    y = 0
    summ = 0
    total = list((''))
    while x < running:
        num = votes.count(x)
        total.append(num)
        x = x + 1
        num = 0
    print('\n')
    print('Results: ')
    x = 0
    while (x < running):
        print('-> ', candidates[x], ': ', total[x],' votes', sep = '')
        x = x + 1   
            
    
# This puts it all together into one function. 
        
def voting_results(candidates):
    display_candidates(candidates)
    votes = generate_votes(candidates)
    display_votes(votes)
    tally_votes(candidates, votes)





    

    
    
    






