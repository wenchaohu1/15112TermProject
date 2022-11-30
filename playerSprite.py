from cmu_112_graphics import *

def appStarted(app):   
    # playerImg: https://www.pinterest.com/pin/721631540269147334/
    spritestrip = app.loadImage('images/forwardPlayer.png') 

    # Width & height from YT tutorial on sprites using PIL:
    # https://www.youtube.com/watch?v=X4Fe04BfTDk&t=166s 
    width, height = spritestrip.size 
    print(width, height)

    app.sprites = [ ]
    for i in range(4):
        sprite = spritestrip.crop((309 * i,0, 309 + 309 * i, height))
        app.sprites.append(sprite)
        
    app.spriteCounter = 0

def timerFired(app):
    app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites)

def redrawAll(app, canvas): 
    canvas.create_image(300, 300, image=ImageTk.PhotoImage(app.sprites[app.spriteCounter]))

runApp(width=600, height=600)