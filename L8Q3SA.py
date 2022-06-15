#---------------------------------------
# Integrity Pledge: All work being 
# submitted is mine and mine alone: A.S
#---------------------------------------
# Name: Ahmed Sajid
# Program: L8Q3SA.py
#---------------------------------------
# Purpose: This program will display and calculate weighted marks for a student
# and will remove the lowest one before outputting a weighted total of marks
#--------------------------------------
original_marks = [19.5, 20, 45.0, 50, 20.5, 50]

# This will apply the weighted score to each mark and return the new values


def get_weighted_marks(original_marks, weight):
    print()
    n = len(original_marks)
    wmarks = list((''))
    for i in range(0,n-1,2):
        x = i + 1
        wmarks.append(((original_marks[i]/original_marks[x])*weight))
    print(len(wmarks), 'weighted marks: ', end = '')    
    print(wmarks)
    return wmarks

# This will determine the smallest mark so that it may be easily omitted

def find_smallest(marks):
    n = len(marks)
    m = 10000000
    for i in range(0,n):
        if marks[i] <= m:
            m = marks[i]
    print()
    print('Smallest mark:', m)
    return m


# This will calculate the total marks received considering the omitted mark
# then this function will display the overall total


def total_marks(marks, weight):
    top = 0
    bottom = 0
    for i in marks:
        top = i + top

    else:
        bottom = len(marks*weight)
    print(top,'out of', bottom)
            

# This is the main function and will put it all together.            
        
            
def calc_lab_mark(original_marks, weight):
    
    marks = get_weighted_marks(original_marks, weight)
    smallest = find_smallest(marks)
    marks.remove(smallest)
    print("\nTotal (omitting smallest): ", end = '')
    total_marks(marks, weight)

    











    

    
    
    






