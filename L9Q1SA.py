#  ----------------------------------------------------
#
#  Academic Integrity Pledge: 
#  I hereby acknowledge this program is my own work. 
#  I have not copied from anyone/anywhere 
#  and I have not let others copy my work.
#
#  Name:      Ahmed Sajid
#  Program:   L9Q1SA.py
#  
#  Purpose: This program will fix a broken image of a giraffe
#  ----------------------------------------------------
from PIL import Image
picture = Image.open("zebra_broken.png")

# This will switch the green and blue pixels of the image to fix the bottom half

def fix_bottom(picture):
    from PIL import Image
    pic = picture
    for x in range(pic.width):
        for y in range(int(pic.height/2),pic.height):
            col = pic.getpixel((x,y))
            pic.putpixel((x,y),(col[0],col[2],col[1]))
    
            
    return pic

# This will replace all magenta pixels on the right side with black pixels

def fix_right_side(picture):
    from PIL import Image
    pic = picture
    for x in range(int(pic.width/2),pic.width):
        for y in range(int(pic.height)):
            red,green,blue = pic.getpixel((x,y))
            if green == 0 and red == 255 and blue == 255:
                pic.putpixel((x,y),(0,0,0))
    return pic
    
            
# This is the main function that will put it all together

def fix_picture():
    pic = picture
    pic = fix_bottom(pic)
    pic = fix_right_side(pic)
    pic.save('zebra_fixed.png')
    pic.show()
    

   