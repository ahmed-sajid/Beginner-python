from PIL import Image


def show_picture(name):
    from PIL import Image
    pic = Image.open(name)
    pic.show()
    return


def show_picture1(name):
    from PIL import Image
    pic = Image.open(name)
    return pic

def remove_red(name):
    from PIL import Image
    for x in range(pic.width):
        for y in range(pic.height):
            col = pic.getpixel((x,y))
            pic.putpixel((x,y),(100,150,col[2]))
            
def count_pixel(pic,color):
    from PIL import Image
    count = 0
    for x in range(pic.width):
        for y in range(pic.height):
            if pic.getpixel((x,y)) == color:
                count = count + 1
    print(count)
    return count
            
def show_new_image(w,h,color):
    img = Image.new("RGB",(w,h))
    for x in range(img.width):
        for y in range(img.height):
            img.putpixel((x,y),(color))
    img.show()
    
def draw_line(pic,color):
    img = Image.open(pic)
    for x in range(600,601):
        for y in range(img.height):
            img.putpixel((x,y),(color))  
    img.show()
    


pic = show_picture1('Eren.jpg')
print('The width of the picture is:', pic.width)
print('The height of the picture is:', pic.height)
print('\nThe picture is', pic.width,'x',pic.height)

draw_line('Eren.jpg',(25,230,150))
