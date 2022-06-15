#  ----------------------------------------------------
#
#  Academic Integrity Pledge: 
#  I hereby acknowledge this program is my own work. 
#  I have not copied from anyone/anywhere 
#  and I have not let others copy my work.
#
#  Name:      Ahmed Sajid
#  Program:   L9Q2SA.py
#  
#  Purpose: This program will draw a snowflake based on the users 
#  inputed level of detail.
#  ----------------------------------------------------


from PIL import Image, ImageDraw  

#''' --------------- DO NOT MODIFY THIS FUNCTION ---------------'''          

# Purpose:  Recursive function to draw a snowflake pattern on an image
def draw_snowflakes(image, x, y, size, level):

    # Exit the recursive call if no more detail levels are needed
    if level <= 0:
        return

    # If detail level is too high, the program takes a very long time to finish
    if level > 4:
        raise Exception('Too much detail requested!')
   
    # Draw a white snowflake of the given size on the given image 
    # centered at the given x and y coordinate           
    start_x = x - size // 2
    start_y = y - size // 2
                     
    amt = 0             
    for temp_y in range(start_y, start_y + size):
        
        # Draw vertical line of snowflake
        image.putpixel((x, temp_y), (255, 255, 255)) 
        
        # Draw diagonal lines of snowflake
        amt += 1        
        image.putpixel((start_x + amt, temp_y), (255, 255, 255))
        image.putpixel((start_x + size - amt, temp_y), (255, 255, 255))
     
    # Draw horizontal line of snowflake    
    for temp_x in range(start_x, start_x + size):
        image.putpixel((temp_x, y), (255, 255, 255)) 
            
    # Setup variables for the next set of recursive calls
    new_level = level - 1
    new_size = size // 3

    # Calculate the coordinates for the new snowflakes
    for new_y in [y - size, y, y + size]:
        for new_x in [x - size, x, x + size]:
            
            # Only call the function if the coordinates are different 
            # from the previous coordinates
            if not (new_x == x and new_y == y):
                draw_snowflakes(image, new_x, new_y, new_size, new_level)


#''' ----------------------------------------------------------- 
   # ------------------ INSERT YOUR CODE BELOW -----------------         
    #----------------------------------------------------------- '''

#This function draws the background rectangles

def make_background():
    img = Image.new("RGB",(640,640),(0,0,255)) 
    h = img.height
    w = img.width
    a = 255
    
    #Left Rectangle
    for x in range(int(w*.1),int(w/2)):
        for y in range(int(h*.1),int(h*.9)):
            img.putpixel((x,y),(0,a,0))
        a = a - 1
    #Right Rectangle
    a = 0
    b = 0
    for x in range(int(w/2),int(w*.9),):
        for y in range(int(h*.1),int(h*.9)):
            img.putpixel((x,y),(0,a,b))
        a = a + 1
        b = b + 1
    #Center Rectangle
    for x in range(int(w*.3),int(w*.7)):
        for y in range(int(h*.3),int(h*.7)):
            img.putpixel((x,y),(0,0,0))    
    return img
                         
#The main Function that will ask the user for a detail value then draw
#the snowflakes based on that detail value
def create_picture():
    detail = int(input('Choose a level of detail (max 4): '))
    while detail < 0 or detail > 4:
        detail = int(input('Choose a level of detail (max 4): '))
    img = make_background()
    y = int(img.width/2)
    x = int(img.height/2)
    size = int(img.width*(1/3))
    draw_snowflakes(img,x,y,size,detail)
    img.save('snowflakes.png')
    img.show()

create_picture() 

end = input('type anything to end')