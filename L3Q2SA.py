#  ----------------------------------------------------
#
#  Academic Integrity Pledge: 
#  I hereby acknowledge this program is my own work. 
#  I have not copied from anyone/anywhere 
#  and I have not let others copy my work.
#
#  Name:      Ahmed Sajid
#  Program:   L3Q2SA.py
#  
#  Purpose:   Take Data from drivers and calculate
#  the fine that the driver has to pay based on their speed
#  and the speed limit. 
#  ----------------------------------------------------

# To start, the program will ask the driver what the
# speed limit is and what speed they were travelling at

limit = input('a) What is the speed limit? ')
driver_speed = input('b) What speed were you travelling? ')
dif = (int(driver_speed) - int(limit))

if (int(dif) > 50):
    ticket = input('c) Do you have previous speeding tickets (YES or NO)? ').lower()

# The program will take the speed limit and driver speed data
# and give a response based on that data 

# If either underspeeding 

print()
if (int(limit) - int(driver_speed) >= 11):
    print('Driving ', (int(limit) - int(driver_speed)), ' KM below the limit is unsafe.', sep = "")


# If speeding and limit is 40

if (int(limit) == 40) and (dif >= 1) and (dif <= 15):
    print('You were driving ', driver_speed, ' KM in a 40 KM zone. ', sep = "")
    print('Your speed was ', dif, ' KM over the limit. ', sep = "")
    print('Edmonton residential speed limits are now 40 KM.')
    print('This is a warning. Drive safely! ')

# If speeding and limit is not 40

elif (int(limit) != 40) and (dif >= 1) and (dif <= 15):
    print('You were driving ', driver_speed, ' KM in a ', limit, ' KM zone. ', sep = "")
    print('Your speed was ', dif, ' KM over the limit. ', sep = "")
    print('Your fine is $', (75 + 3 * dif), '.', sep ="")
    
# If speeding by >15 and <50

elif (dif >= 16) and (dif <= 30):
    print('You were driving ', driver_speed, ' KM in a ', limit, ' KM zone. ', sep = "")
    print('Your speed was ', dif, ' KM over the limit. ', sep = "")
    print('Your fine is $', (100 + 5 * dif), '.', sep ="")

elif (dif >= 31) and (dif <= 50):
    print('You were driving ', driver_speed, ' KM in a ', limit, ' KM zone. ', sep = "")
    print('Your speed was ', dif, ' KM over the limit. ', sep = "")
    print('Your fine is $', (125 + 10 * dif), '.', sep ="")

# If speeding by >50

elif (dif > 50) and (ticket == 'no'):
    print('You were driving ', driver_speed, ' KM in a ', limit, ' KM zone. ', sep = "")
    print('Your speed was ', dif, ' KM over the limit. ', sep = "")
    print('Your fine is $', (235 + 15 * dif), '.',  sep ="")

elif (dif > 50) and (ticket == 'yes'):
    print('You were driving ', driver_speed, ' KM in a ', limit, ' KM zone. ', sep = "")
    print('Your speed was ', dif, ' KM over the limit. ', sep = "")
    print('Your license is now suspended for 1 month. ')

# If going the limit or under by less than 11

elif (int(driver_speed) == int(limit)) or (int(limit) - int(driver_speed) <= 10):
        print('You were driving safely. Well done! ')

        

    



