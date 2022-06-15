#-------------------------------------------------------
# This program will play rock paper scissors with you!
#-------------------------------------------------------
rock = ('rock')
paper = ('paper')
scissors = ('scissors')
value = input('Pick: Rock, Paper, or Scissors ').lower()
if (value == rock) or (value == paper) or (value == scissors):
    import random
    value_1 = random.randint(1,3)
else: 
    value_1 = (4)
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
elif (value == rock) and (value_1 == 3):
        print('You Won!') 
elif (value == paper) and (value_1 == 1):
        print('You Won!')
elif (value == paper) and (value_1 == 2):
        print('We tied!')
elif (value == paper) and (value_1 == 3):
        print('I Won!')
elif (value == scissors) and (value_1 == 1):
        print('I Won!')
elif (value == scissors) and (value_1 == 2):
        print('You Won!')
elif (value == scissors) and (value_1 == 3):
        print('We Tied!')
elif (value_1 == 4):
    print('No cheating! Pick a valid value')
else:
    print('Something went wrong, try again :(')


