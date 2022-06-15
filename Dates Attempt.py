#---------------------------------------
# Integrity Pledge: All work being 
# submitted is mine and mine alone: A.S
#---------------------------------------
# Name: Ahmed Sajid
# Program: L8Q3SA.py
#---------------------------------------
# Purpose: Exam Question
#--------------------------------------

dates = ['07-20-2003','01-01-2001','09-09-2009']

def change_dates(dates):
    dates_ind = str(dates)
    dates_t=[]
    
    for i in dates_ind:
        if i.isdigit() == True:
            dates_t.append(i)
    a = (len(dates_t))
    b = len(dates)
    x = 8
    c = 0
    dates_o = []
    for i in range(0,b):
        dates_o.append(dates_t[c+4:x])
        dates_o.append('-')
        dates_o.append(dates_t[c:x-6])
        dates_o.append('-')
        dates_o.append(dates_t[c+2:x-4])
        c = c + 8
        x = x + 8
    dates_1 =str(dates_o)
    dates_x = dates_o
    dates_o = []
    for i in dates_1:
        if i.isdigit() == True or i == '-':
            dates_o.append(i)    
    dates = []
    c = 0
    x = 10
    for i in range(b):
        dates.append(''.join(dates_o[c:x]))
        c = c + 10
        x = x + 10
    dates.append('2000-01-01')
    dates = (sorted(dates))
    print('Sorted Dates (YYYY-MM-DD):\n',(dates))
    print()
    print('Dates with Alphabetic Month Codes: ')
    
    months = ['XXX', 'JAN', 'FEB', 'MAR', 'APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    x = 2
    c = 6
    for i in range(b):
        a = (''.join(dates_x[x]))
        a = int(a)
        dates_x[x] = (months[a])
        
        x = x + 5
    dates_f = []
    x = 0
    for i in range(len(dates_x)):
        
        dates_f.append((''.join(dates_x[x])))
        x = x + 1
    c = 0
    d = 5
    x = 1
    for i in range(b):
        print('Date ',x,': ',''.join(dates_f[c:d]),sep = '')
        c = c + 5
        d = d + 5
        x = x + 1
    c = 0
    d = 5
    
    print()
    
    dates_final=[]
    for i in range(b):
        dates_final.append(''.join(dates_f[c:d]))
        c = c + 5
        d = d + 5
    print('The final list is:',sorted(dates_final))
           
    
    
        
            
    
        
        
    
        

        
        

    
    
        
        
            
        
        
        
        
         
        
        
        
       
        
                
            
            
                
change_dates(dates)
    


    
    
    


        
             
