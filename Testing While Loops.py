num = input('Type start to start! ')
score = 0
score_1 = 0
while (num == 'start'):
    rock = ('rock')
    paper = ('paper')
    scissors = ('scissors')
    value = input('Pick: Rock, Paper, or Scissors ').lower()
    if (value == 'score'):
        value_1 = (6)
    if (value == 'stop'):
        num = ('stop')
    if (value == rock) or (value == paper) or (value == scissors):
        import random
        value_1 = random.randint(1,3)
    if (value == 'stop'):
        value_1 = (5)
    if (value_1 != 6) and (value_1 != 5) and (value != rock) and (value != paper) and (value != scissors):
        value_1 = 4
    
    if (int(value_1) == int(1)):
        print('I picked rock')
    elif (int(value_1) == int(2)):
        print('I picked paper')
    elif (int(value_1) == int(3)):
        print('I picked scissors')
    
    
    if (value == rock) and (value_1 == 1):
        print('We tied!')
    elif (value == rock) and (value_1 == 2):
            print('I Won!')
            score_1 = score_1 + 1
    elif (value == rock) and (value_1 == 3):
            print('You Won!')
            score = score + 1
    elif (value == paper) and (value_1 == 1):
            print('You Won!')
            score = score + 1
    elif (value == paper) and (value_1 == 2):
            print('We tied!')
    elif (value == paper) and (value_1 == 3):
            print('I Won!')
            score_1 = score_1 + 1
    elif (value == scissors) and (value_1 == 1):
            print('I Won!')
            score_1 = score_1 + 1
    elif (value == scissors) and (value_1 == 2):
            print('You Won!')
            score = score + 1
    elif (value == scissors) and (value_1 == 3):
            print('We Tied!')
    elif (value_1 == 4):
        print('No cheating! Pick a valid value')
    elif (value_1 == 5):
        print('Thanks for playing!')
    elif (value_1 == 6):
        print('I have', score_1, ', you have', score)
    value_1 = 0
        


if (num != 'start') and (num != 'stop'):
    print('Error, invalid input; restart program ')
