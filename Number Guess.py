A = input('Give me a random number. ')
import random
B = random.randint(1, 10)
value =(int(A)*int(B)) 
print('Your % is ' + str(int(A)%int(B)))
print('Your product is ' + str(value))
C = input('What was the random number generated? ')
if (str(C) == str(B)):
    print('Good Job! The correct answer was ' + str(B))

else:
    print('Incorrect, the correct answer was ' + str(B))
if (str(C) == str(B)):
    print('You got 100%!')
else: 
    print('You got 0%, better luck next time!')

