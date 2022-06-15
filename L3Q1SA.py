#  ----------------------------------------------------
#
#  Academic Integrity Pledge: 
#  I hereby acknowledge this program is my own work. 
#  I have not copied from anyone/anywhere 
#  and I have not let others copy my work.
#
#  Name:      Ahmed Sajid
#  Program:   L3Q1SA.py
#  
#  Purpose:   Take Data from Customers
#  and use the data to calculate customers order  
#  and their receipt including a tip
#  ----------------------------------------------------

# List of Variables

C = 3
T = 4
W = 0
P2 = 7
P4 = 10
P8 = 12
E = 8
EB = 11
M = 5
T1_2 = 1 
T3_4 = 0.75
T5 = 0.50
Sub_total = 0

# Start of Order

# Customer Drink Order

print("Customer's order:")
drink = input('1. Would you like coffee, tea, or water (c, t, w)? ').lower()
if (drink == 'c'):
    print('Coffee', 'costs $' + str(C))
    Sub_total = (Sub_total + C)
elif (drink == 't'):
     print('Tea','costs $' + str(T))
     Sub_total = (Sub_total + T)
elif (drink == 'w'):
    print('No extra cost')
    Sub_total = (Sub_total + 0)
print()

# Customer Food Order

food = input('2. Would you like (A) pancakes, (B) eggs, or (C) a muffin (A, B, C)? ').lower() 
if (food == 'a'):
    num = input('-> How many pancakes? Choose 2, 4, or 8: ')
    if (num == '2'):
        print('Choice (A)', 'costs $' + str(P2))
        Sub_total = (Sub_total + P2)
    elif (num == '4'):
         print('Choice (A)','costs $' + str(P4))
         Sub_total = (Sub_total + P4)
    elif (num == '8'):
        print('Choice (A)','costs $' + str(P8)) 
        Sub_total = (Sub_total + P8)
elif (food == 'b'):
    bacon = input('-> Add bacon for $3 (Yes or No)? ').lower()
    if (bacon == 'yes'):
        print('Choice (B) costs $' + str(EB))
        Sub_total = (Sub_total + EB)
    else:
        print(' Choice (B) costs $' + str(E))
        Sub_total = (Sub_total + E)
elif (food == 'c'):
    print('Choice (C) costs $' + str(M))
    Sub_total = (Sub_total + M)
print()

# Customer Optional Toast Order

toast = input('3. How many pieces of toast would you like? Enter a number: ')
if (int(toast) == 0):
    print('No extra cost')
elif (int(toast) == 1):
    print('1 piece costs $1')
    Sub_total = (Sub_total + 1)
elif (int(toast) > 0) and (int(toast) <= 2):
    print(str(toast), ' pieces cost $', (int(toast) * 1), sep = "")
    Sub_total = (Sub_total + (int(toast) * 1))
elif (int(toast) > 0) and (int(toast) > 2) and (int(toast) <= 4):
    print(str(toast), ' pieces cost $', (float(toast) * 0.75), sep = "")
    Sub_total = (Sub_total + (float(toast) * 0.75))
elif (int(toast) > 0) and (int(toast) >= 5):
    print(str(toast), ' pieces cost $', (float(toast) * 0.50), sep = "")
    Sub_total = (Sub_total + (float(toast) * 0.50))
print()

# Final Price Calculations

print('Sub-total: $', Sub_total, sep = "")
if (Sub_total <= 20):
    tip = float(input('Enter gratuity: $'))
elif (Sub_total > 20):
    Sub_tip = (float(Sub_total) * 0.15)
    print('15% gratuity: $', Sub_tip, sep = "")
if (Sub_total > 20):
    print('Total owed: $', Sub_total + Sub_tip, sep = "")
else:
    print('Total owed: $', float(Sub_total) + float(tip), sep = "")