from cmu_112_graphics import * 
from classes import *
from mazeScreen import *
 

def catalogMode_redrawAll(app, canvas): 
    canvas.create_image(app.width/2, app.height/2, image=app.catalogImg)

def catalogMode_mousePressed(app, event):
    x = event.x
    y = event.y

    print(x,y)
   
    if (x > 185 and x < 420 and y < 240 and y > 170):
        app.mode = 'gameMode'
 
    elif (x > 185 and x < 420 and y < 325 and y > 255):
        app.mode = 'catalogMode'