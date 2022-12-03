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

    # if player is close to cat, display "Press enter to catch cat!"
    if app.ableToCaptureCat == True:
        canvas.create_text(app.width/2, 35, 
                           text="Press enter to make catch the cat!", fill = "white")

def gameMode_timerFired(app):
    # Constantly check if the player is close to the cat
    # If Yes, app.ableToCaptureCat = True
    if distance(app.player.x, app.player.y, app.cat1.x, app.cat1.y) <= 25:
        app.ableToCaptureCat = True
    else: 
        app.ableToCaptureCat = False
    
    # Frames of sprite
    # app.spriteCounter = (1 + app.spriteCounter) % len(app.sprites)
 
        
 

def gameMode_keyPressed(app, event):  
    # using arrow keys to move
    if event.key == "Left":  
        movePlayer(app, -1, 0)

    elif event.key == "Up": 
        movePlayer(app, 0, -1)

    elif event.key == "Down": 
        movePlayer(app, 0, +1)

    elif event.key == "Right": 
        movePlayer(app, +1, 0) 

    #if the condition to capture cat is true and if user pressed enter, change mode
    elif app.ableToCaptureCat == True:
        if event.key == "Return" or event.key == "Enter":
            #Cat is captured, move to its screen, add to catalog 
            
            app.mode = "catalogMode"  
        
# helper to help Move player 
def movePlayer(app, drow, dcol):
    row = drow
    col = dcol

    drow *= 25
    dcol *= 25
    # Move player faster, by 25 pixels 
    app.player.x += drow 
    app.player.y += dcol 
    
    # Check bounds
    if not inBorders(app): 
        app.player.x -= drow
        app.player.y -= dcol  
        print("not in bounds")
    
    if inWall(app, row, col): 
        app.player.x -= drow
        app.player.y -= dcol  
        print("in the walls!")

# Check if player crashes into wall
def inWall(app, row, col):  
    if (row, col) in app.maze.walls:
        return True
    return False 

def inBorders(app): 
    #If the player is in the bounds
    if ((app.player.x > 40 and app.player.x <= 560) and 
        (app.player.y >= 40 and app.player.y <= 560)):
        return True
    else:
        return False
 

