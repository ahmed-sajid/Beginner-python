#  ----------------------------------------------------
#
#  Academic Integrity Pledge: 
#  I hereby acknowledge this program is my own work. 
#  I have not copied from anyone/anywhere 
#  and I have not let others copy my work.
#
#  Name:      Ahmed Sajid
#  Program:   L10Q2SA.py
#  
#  Purpose: This program will create a collage from a chosen image
# by inversing, tiling, making a puzzle out of, and making greyscale parts of the image
# until ultimately combining them

#  ----------------------------------------------------
from PIL import Image,ImageDraw

# This will inverse the colors in a small range of the image

def inverse(file_name):
    
    img = Image.open(file_name)
    w = img.width
    h = img.height
    
    # Inverses colors in a small range
    
    for x in range(int(w*.75),w):
        for y in range(h):
            red,green,blue = img.getpixel((x,y))
            img.putpixel((x,y),(255 - red, 255 - green, 255 - blue))
    # Label
    draw = ImageDraw.Draw(img)
    draw.text((5,5),'Inverse',(255,215,0))
    
    return img

# This will ask the user if they wish to rotate the picture, and, if yes, will rotate it before tiling it

def tile(file_name):
    
    # opens image
    
    img = Image.open(file_name)
    
    small = img.resize((int(img.width/4),int(img.height/4)))
    
    # Ask user if they wish to rotate the tile and error check it
    
    rotate = input('Rotate tile (yes or no)? ').lower()
    
    while rotate != 'yes' and rotate != 'no':
        rotate = input('Rotate tile (yes or no)? ').lower()
    
    # If yes, rotates it and adds a label
    
    if rotate == 'yes':
        angle = 180
        small = small.rotate(angle)
        draw = ImageDraw.Draw(img)
        draw.text((5,5),'Tile and rotate',(255,215,0))
    else:
        draw = ImageDraw.Draw(img)
        draw.text((5,5),'Tile',(255,215,0))        
        
    # Paste it 4 times to tile it
    
    img.paste(small,(int(0),int(img.height*.75)))
    
    img.paste(small,(int(img.width * 0.25),int(img.height*.75)))
    
    img.paste(small,(int(img.width * 0.5),int(img.height*.75)))
    
    img.paste(small,(int(img.width * 0.75),int(img.height*.75)))
    
    return img

# This will make a puzzle out of the image and then paste the saved pieces in a new order

def puzzle(file_name):
    
    # opens Image
    
    img = Image.open(file_name)
    
    puzzle = []
    
    # crops and stores parts of the image
    
    x = 0.25
    y = 0
    for i in  range(4):
        cropped = img.crop((int(img.width*y),0,int(img.width*x),int(img.height*0.25)))
        x = x + 0.25
        y = y + 0.25
        puzzle.append(cropped)
    
    # pastes the 4 cropped pictures in a new order
    
    img.paste(puzzle[2],(int(img.width * 0),int(img.height*0)))
    img.paste(puzzle[0],(int(img.width * .25),int(img.height*0)))
    img.paste(puzzle[3],(int(img.width * .5),int(img.height*0)))
    img.paste(puzzle[1],(int(img.width * .75),int(img.height*0)))
    
    # Labels the image
    
    draw = ImageDraw.Draw(img)
    draw.text((5,5),'Puzzle',(255,215,0))      
    
    return img    

# This will make the first quarter of the image greyscale

def greyscale(file_name):
    
    # opens image
    
    img = Image.open(file_name)
    
    # makes a small portion of the image greyscaled
    
    w = img.width
    h = img.height
    
    for x in range(0,int(w*.25)):
        for y in range(h):
            red,green,blue = img.getpixel((x,y))
            
            average = int((red+green+blue)/3)
            
            img.putpixel((x,y),(average,average,average)) 
   
    # Label
    
    draw = ImageDraw.Draw(img)
    draw.text((5,5),'Greyscale',(255,215,0))     
    
    return img

# This will put it all together, show and save your collage

def make_collage(file_name):
    
    # opens image to get dimensions
    
    img = Image.open(file_name)
    
    # gets images from previous helper functions and saves them
    
    img1 = inverse(file_name)
    img2 = tile(file_name)
    img3 = puzzle(file_name)
    img4 = greyscale(file_name)
    
    # creates a new canvas for the collage
    
    w = img.width*2
    h = img.height*2
    
    img = Image.new('RGB',(w,h))  
    
    # creates, saves and shows the collage
    
    img.paste(img1,(int(img.width * 0),int(img.height*0)))
    img.paste(img2,(int(img.width * .5),int(img.height*0)))
    img.paste(img3,(int(img.width * 0),int(img.height*.5)))
    img.paste(img4,(int(img.width * .5),int(img.height*.5)))
    
    img.show()
    img.save('collage.png')
make_collage('shape_picture.png')
         
       
        
             
    
    

    

            
    

   