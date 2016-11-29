# -*- coding: utf-8 -*-
#Name: Hieu Tran
#Purpose:

from cImage import *
from math import *
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Start-CopiedCode-Python Programming in ConText, 2nd Edition, 6.51: Listing 6.9
def nsize(oldimage,n):
    
    oldimage = FileImage(oldimage)
    oldw = oldimage.getWidth()
    oldh = oldimage.getHeight()
    
    newim = EmptyImage(oldw//n,oldh//n)
    
    for row in range(newim.getHeight()):
        for col in range(newim.getWidth()):
            originalCol = col*n
            originalRow = row*n
            oldpixel = oldimage.getPixel(originalCol ,originalRow)
            
            newim.setPixel(col,row,oldpixel)     
    return newim
#End-CopiedCode-
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Start-myCode
def sticker(filename):
    myWin = ImageWin("Test",1000,1000)
    
    nim = EmptyImage(1000,1000)
    for a in range (950,1000):
        for b in range(0,50):
            nim.setPixel(a,b,Pixel(255,0,0))
    for a in range (950,1000):
        for b in range(50,100):
            nim.setPixel(a,b,Pixel(0,255,0))
    for a in range (950,1000):
        for b in range(100,150):
            nim.setPixel(a,b,Pixel(0,0,255))
    for a in range (950,1000):
        for b in range(150,200):
            nim.setPixel(a,b,Pixel(255,255,0))
    nim.draw(myWin)
    im = FileImage(filename)
    
    h = im.getHeight()
    w = im.getWidth()
    
    # I adjust the size of image according to ImageWin
    if h>=w and h>=1000:
        n = h//975 + 1
        im = nsize(filename,n)
        h = im.getHeight()
        w = im.getWidth()
    if w>h and w>=1000:
        n = w//975 + 1
        im = nsize(filename,n)
        h = im.getHeight()
        w = im.getWidth()
    
    im.draw(myWin)
    
    undo = 0#using this variable for undo
    mouse = [0,0]
    mouse1 =[999,999] # this mouse1 is used for undo ( backup previous mouse)
    count=0
    e = 20 #default of light intensity
    r = 5
    wors = 1
    
    while mouse[0]<=w and mouse[0]>=0 and mouse[1]<=h and mouse[1]>=0:
        mouse=myWin.getMouse()
        if mouse[0]>=950 and mouse[0]<1000 and mouse[1]>=50 and mouse[1]<100:
            e = input("input the light or dark intensity of each click (must be an integer in (-255,255)) ex:20; input: ")
            if e<=-255 or e>=255:
                break
            else:
                mouse = [0,0] # update mouse so that we're still in while loop
                continue
        elif mouse[0]>=950 and mouse[0]<1000 and mouse[1]>=100 and mouse[1]<150:
            # enhance the area of a circle with radius = n pixel( I recommend use max 5 pixel)
            r = input("input a postive number ex:4; input = ")
            if r<0:
                break
            else:
                mouse = [0,0] # update mouse so that we're still in while loop
                continue
        elif mouse[0]>=950 and mouse[0]<1000 and mouse[1]>=0 and mouse[1]<50:    
            count = 0
            if undo == 0:
                break
            elif undo == 1:
                layer=EmptyImage(2*r+1,2*r+1)
                layer.setPosition(mouse1[0]-r,mouse1[1]-r)
                for a in range (-r,r+1,1):
                    count = count + 1
                    if (mouse1[0]+a)<w and (mouse1[0]+a)> 0: #make the Pixel index is not out of range 
                        for b in range(-r,r+1,1):
                            count = count +1
                            if (mouse1[1]+b)<h and (mouse1[1]+b)>0:#make the Pixel index is not out of range 
                                if a*a+b*b<= r*r: # enhance picture by a circle with each click 
                                    im.setPixel(mouse1[0]+a,mouse1[1]+b,Pixel((L[count])[0],(L[count])[1],(L[count])[2]))
                                    layer.setPixel(r+a,r+b,Pixel((L[count])[0],(L[count])[1],(L[count])[2]))
                                else:
                                    layer.setPixel(r+a,r+b,Pixel((L[count])[0],(L[count])[1],(L[count])[2]))
                    
                layer.draw(myWin)
                undo = 0 # update undo so that we can undo 1 time, if more function will break
                mouse = [0,0] # update mouse so that it's still in while loop 
            elif undo ==2:
                layer=EmptyImage(n,d)
                layer.setPosition(mouse1[0]-n//2,mouse1[1]-d//2)
                for a in range(-n//2,n//2):
                    count = count + 1
                    for b in range(-d//2,d//2):
                        count = count + 1
                        if (mouse1[0]+a)>=0 and (mouse1[0]+a)<w and (mouse1[1]+b)>=0 and (mouse1[1]+b)<h:
                            layer.setPixel(a+n//2,b+d//2,Pixel(L[count][0],L[count][1],L[count][2]))
                            im.setPixel(mouse1[0]+a,mouse1[1]+b,Pixel(L[count][0],L[count][1],L[count][2]))
                layer.draw(myWin)     
                print "ngu"
                undo = 0
                mouse = [0,0]
                  
        elif mouse[0]<w and mouse[0]>=0 and mouse[1]<h and mouse[1]>=0:
            count = 0
            if wors == 1:
                mouse1 = mouse
                L={} # reset new L here
                undo = 1
                layer=EmptyImage(2*r+1,2*r+1)
                layer.setPosition(mouse[0]-r,mouse[1]-r)
                for a in range (-r,r+1,1):
                    count = count + 1
                    if (mouse[0]+a)<w and (mouse[0]+a)>= 0: #make the Pixel index is not out of range 
                        for b in range(-r,r+1,1):
                            count = count + 1
                            if (mouse[1]+b)<h and (mouse[1]+b)>=0:#make the Pixel index is not out of range 
                                p = im.getPixel(mouse[0]+a,mouse[1]+b)
                                L[count] = p
                                red=p[0]
                                green=p[1]
                                blue=p[2]
                                if a*a+b*b<=r*r: #circle with radius =5
                                    
                                    if red>255-e:
                                        red=255-e
                                    if red< -e:
                                        red = -e
                                    if green>255-e:
                                        green=255-e
                                    if green < -e:
                                        green= -e
                                    if blue>255-e:
                                        blue=255-e
                                    if blue< -e:
                                        blue = -e
                                
                                    im.setPixel(mouse[0]+a,mouse[1]+b,Pixel(red+e,green+e,blue+e))
                                    layer.setPixel(r+a,r+b,Pixel(red+e,green+e,blue+e))
                                else:
                                    layer.setPixel(r+a,r+b,Pixel(red,green,blue))
                layer.draw(myWin)
            elif wors == 0:
                mouse1 =mouse
                L = {}
                undo = 2
                layer.setPosition(mouse[0]-n//2,mouse[1]-d//2)
                for a in range(-n//2,n//2):
                    count = count + 1
                    for b in range(-d//2,d//2):
                        count = count + 1
                        if (mouse[0]+a)>=0 and (mouse[0]+a)<w and (mouse[1]+b)>=0 and (mouse[1]+b)<h:
                            m=bow.getPixel(a+n//2,b+d//2)
                            m2=im.getPixel(mouse[0]+a,mouse[1]+b)
                            L[count] = m2
                            if m[0]>50 or m[1]>50 or m[2]>50:
                                layer.setPixel(a+n//2,b+d//2,Pixel(m[0],m[1],m[2]))
                                im.setPixel(mouse[0]+a,mouse[1]+b,Pixel(m[0],m[1],m[2]))
                            else:
                               layer.setPixel(a+n//2,b+d//2,Pixel(m2[0],m2[1],m2[2]))
                        else:
                            layer.setPixel(a+n//2,b+d//2,Pixel(0,0,0))
                layer.draw(myWin)
                
                wors = 1
        
        elif mouse[0]>=950 and mouse[0]<1000 and mouse[1]>=150 and mouse[1]<200:
            kinh = FileImage("C:\Users\htran\Desktop\\kinh.png")
            kinh.setPosition(850,0)
            n=kinh.getWidth()
            d=kinh.getHeight()
            
            tim = FileImage("C:\Users\htran\Desktop\\tim.png")
            tim.setPosition(850,100)
            
            hieu = FileImage("C:\Users\htran\Desktop\\hieu.png")
            hieu.setPosition(850,200)
            
            kinh.draw(myWin)
            tim.draw(myWin)
            hieu.draw(myWin)
            #t = 1
            mouse2=myWin.getMouse()
            if mouse2[0]>=850 and mouse2[0]<950 and mouse2[1]>=0 and mouse2[1]<100:
                bow = kinh
            elif mouse2[0]>=850 and mouse2[0]<950 and mouse2[1]>=100 and mouse2[1]<200:
                bow = tim
            elif mouse2[0]>=850 and mouse2[0]<950 and mouse2[1]>=200 and mouse2[1]<300:
                bow = hieu
                
            layer = EmptyImage(n,d)
            layer.setPosition(850,0)
            layer.draw(myWin)
            layer.setPosition(850,100)
            layer.draw(myWin)
            layer.setPosition(850,200)
            layer.draw(myWin)
            wors = 0
            mouse=[0,0]
        else:
            break                         
    myWin.exitonclick()
    im.save("C:\Users\htran\Desktop\\mickey1.jpg")
#End-MyCode
sticker("C:\Users\htran\Desktop\\ca.jpg")