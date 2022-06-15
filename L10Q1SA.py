#  ----------------------------------------------------
#
#  Academic Integrity Pledge: 
#  I hereby acknowledge this program is my own work. 
#  I have not copied from anyone/anywhere 
#  and I have not let others copy my work.
#
#  Name:      Ahmed Sajid
#  Program:   L10Q1SA.py
#  
#  Purpose: This program will draw a picture
#  ----------------------------------------------------
from PIL import ImageDraw, Image


# This function will draw a colorful robot using a variety
# of shapes and colors

def draw_picture():
    # New Image
    
    img = Image.new("RGB",(500,500),(52,198,235))
    
    # Set up image draw
    
    draw = ImageDraw.Draw(img)
        
    # Body
    
    draw.rectangle([(50,50),(450,450)],(91,97,107),(0,0,0))
    
    # Metal Lines
    
    x = 75
    
    for i in range(8):
        
        draw.line([(50,x),(450,x)],(0,0,0),1)
        
        x = x + 50    
    
    # Mouth
    
    draw.rectangle([(200,300),(300,350)],(72,7,110),(0,0,0))
   
    # Eyes
    
    draw.ellipse([(100,100),(200,200)],(104,62,240),(0,0,0))
    
    draw.ellipse([(300,100),(400,200)],(104,62,240),(0,0,0))
    
    # Ears and Nose
    
    draw.polygon([(250,200),(200,255),(300,255)],(74,4,4),(0,0,0))
    
    draw.polygon([(25,150),(50,175),(50,125)],(173,57,7),(0,0,0))
    
    draw.polygon([(475,150),(450,175),(450,125)],(173,57,7),(0,0,0))
    
    # Title
    
    draw.text((200,25),"A Colorful Robot",(0,0,0))
    
    # Save
    
    img.save("shape_picture.png")
    
    # Show image
    
    img.show()
    

    

   