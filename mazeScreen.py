from cmu_112_graphics import * 
from classes import *
from mazeGeneration import *
from usefulFunctions import *
from catalogScreen import *
# from playerSprite import *

# Game Screen Mode

def gameMode_redrawAll(app, canvas):

    #draw Maze & background
    canvas.create_image(app.width/2, app.height/2, image=app.blankImg)
    app.maze.redrawAll(canvas)   

    # draw player
    canvas.create_image(app.player.x, app.player.y, image=app.player.img)  
      
    # draw cats
    canvas.create_image(app.cat1.x, app.cat1.y, image=app.cat1.img) 

    # if player close to cat, display "Press enter to catch cat!"
    if app.ableToCaptureCat == True:
        canvas.create_text(app.width/2, 35, text="Press enter to make catch the cat!")

def gameMode_timerFired(app):
    # Constantly check if the player is close to the cat
    # Yes, app.ableToCaptureCat = True
    if distance(app.player.x, app.player.y, app.cat1.x, app.cat1.y) <= 25:
        app.ableToCaptureCat = True
    else: 
        app.ableToCaptureCat = False
    
    # Frames of sprite
    # app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites)

def gameMode_keyPressed(app, event):  
    # using arrow keys to move
    if event.key == "Left": 
        # app.playerImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/leftPlayer.png"),1/10))
        movePlayer(app, -1, 0)

    elif event.key == "Up":
        app.playerImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/backwardPlayer.png"),1/10))
        movePlayer(app, 0, -1)

    elif event.key == "Down":
        app.playerImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/forwardPlayer.png"),1/10))
        movePlayer(app, 0, +1)

    elif event.key == "Right":
        # app.playerImg = ImageTk.PhotoImage(app.scaleImage(app.loadImage("images/rightPlayer.png"),1/10))
        movePlayer(app, +1, 0) 

    #if the condition to capture cat is true and if use press enter, change mode
    elif app.ableToCaptureCat == True:
        if event.key == "Return" or event.key == "Enter" :
            app.mode = "catalogMode"  
        
# helper to help Move player 
def movePlayer(app, drow, dcol):
    # Move player faster, by 25 pixels  
    app.player.x += drow * 25
    app.player.y += dcol * 25  

    # Check bounds
    if not inBorders(app):
        app.player.x -= drow
        app.player.y -= dcol  
     
    else:
        return True
 
def inBorders(app): 
    #If the player is in the bounds
    if ((app.player.x >= 10 and app.player.x <= 590) and 
        (app.player.y >= 10 and app.player.y <=590)):
        return True
    else:
        return False
 

