trials = 0
neg = 0
pos = 0
zero = 0
numt = 0
trial_1 = 0
numt_1 = 0
user = 'admin_area51'
pass_ = 'TopSecret69'
attempt = 0
sec = 3
sec_1 = 4


while (attempt < sec):
     print()
     auser = input('What is your username? ').lower()
     print()
     apass = input('What is your password? ')
     if (user == auser) and (pass_ == apass):     
          while (trials < 50):
               import random
               num = random.randint(-1000, 1000)     
               if (num < 0):
                   neg = (int(neg) + 1)
                   
                   
               elif (num > 0):
                   pos = (int(pos) + 1)
                   
               elif (num == 0):
                   zero = (int(zero) + 1)
               trials = (int(trials) + 1)
               numt = (numt + num)
               print('You got ', neg, ' negative values!', sep = "")
               print()
               print('You got ', pos, ' positive values!', sep = "")
               print()
               print('You got ', zero, ' zeros!', sep = "")
               print()
               print('The number of simulations was ', (pos + neg + zero), sep ="")
               print()
               print('The sum of all your values was ', (numt), sep ="")
     elif (user != auser) or (pass_ != apass):
          attempt = (int(attempt) + 1)
          sec_1 = (int(sec_1) - 1)
          
          
     if (user != auser) and (attempt != sec) or (pass_ != apass) and (attempt != sec):
          print()
          print('Invalid credentials, please try again ')
          print()
          print('**Warning, you have ', (int(sec_1) - 1), ' attempts left**', sep="")
          
          
if (attempt >= 2):
     print()
     print("**Attempting to gain unlawful access to")
     print('secure government property is a federal crime.')
     print( "Police have been notifed and have been dispatched")
     print("to this location.**")
     input('This program will self destruct immediately, input access key to cancel ')
     
     
     



