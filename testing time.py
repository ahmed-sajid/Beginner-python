import time

string = list('54321')
numb = 0
print('T-minus ', end = "")
for char in range (0,len(string)):
    print(string[int(numb)], sep = " ", end = " ")
    numb = numb + 1
    time.sleep(1.5)
print('Blastoff!')
    
    
    