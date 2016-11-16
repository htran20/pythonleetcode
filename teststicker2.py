from cImage import *
from math import *
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def nsize(oldimage,n):       #n = ratio of new over old
    oldw = oldimage.getWidth()
    oldh = oldimage.getHeight()
    
    newim = EmptyImage(int(oldw*n),int(oldh*n))
    
    for row in range(newim.getHeight()):
        for col in range(newim.getWidth()):
            originalCol = col//n
            originalRow = row//n
            oldpixel = oldimage.getPixel(originalCol ,originalRow)
            
            newim.setPixel(col,row,oldpixel)
            
    return newim
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def sticker(filename):
    myWin = ImageWin("Test",1000,1000)
    
    nim = EmptyImage(1000,1000)
    nim.draw(myWin)
    im = FileImage(filename)
    
    h = im.getHeight()
    w = im.getWidth()
    im.draw(myWin)
    
    
    mouse = [0,0]
    
    while mouse[0]<=w and mouse[0]>=0 and mouse[1]<=h and mouse[1]>=0:
        mouse=myWin.getMouse()
        if mouse[0]>w or mouse[0]<0 or mouse[1]>h or mouse[1]<0:
            break
        for a in range (-5,5,1):
            if (mouse[0]+a)<w and (mouse[0]+a)> 0: #make the Pixel index is not out of range 
                for b in range(-5,5,1):
                    if (mouse[1]+b)<h and (mouse[1]+b)>0:#make the Pixel index is not out of range 
                        if a*a+b*b<= 25: #circle with radius =5
                            
                            p = im.getPixel(mouse[0]+a,mouse[1]+b)
                            red=p[0]
                            green=p[1]
                            blue=p[2]
                            if red>235:
                                red=235
                            if green>235:
                                green=235
                            if blue>235:
                                blue=235
                
                            im.setPixel(mouse[0]+a,mouse[1]+b,Pixel(red+20,green+20,blue+20))
                            im.draw(myWin)
    myWin.exitonclick()
    im.save("C:\Users\htran\Desktop\\mickey1.gif")