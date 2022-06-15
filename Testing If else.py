User_Real = ('asajid4')
Pass_Real = ('Macewan12')

print('Please enter the following credentials:')
User = input('Username: ')
Pass = input('Password: ')

if (User == User_Real):
    Part_1 = ('true')
else:
    Part_1 = ('false')

if (Pass == Pass_Real):
    Part_2 = ('true')
else:
    Part_2 = ('false')
if (Part_1 == ('true') and Part_2 == ('true')):
     print('Login Succesful')
else: 
    print('Please Check Credentials')





    



    
