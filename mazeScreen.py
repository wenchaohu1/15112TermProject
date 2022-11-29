from cmu_112_graphics import * 
from classes import *
from mazeGeneration import *
from usefulFunctions import *
from catalogScreen import *
# Game Screen Mode

def gameMode_redrawAll(app, canvas):

    #draw Maze & background
    canvas.create_image(app.width/2, app.height/2, image=app.blankImg)
    app.testMaze.redrawAll(canvas)   

    # draw player
    canvas.create_image(app.player.x, app.player.y, image=app.player.img)
      
    # draw cats
    canvas.create_image(app.cat1.x, app.cat1.y, image=app.cat1.img) 

    # if player close to cat, display "press enter to catch cat!"
    if app.ableToCaptureCat == True:
        canvas.create_text(app.width/2, 35, text="Press enter to make catch the cat!")

def gameMode_timerFired(app):
    #Constantly check if the player is close to the cat
    if distance(app.player.x, app.player.y, app.cat1.x, app.cat1.y) <= 25:
        app.ableToCaptureCat = True
    else:
    # elif distance(app.player.x, app.player.y, app.cat1.x, app.cat1.y) > 25:
        app.ableToCaptureCat = False

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
    
    # elif event.key == "Return" or event.key =="Enter":
    #     app.mode = "collectionsScreen"
    
    # elif distance(app.player.x, app.player.y, app.cat1.x, app.cat1.y) <= 50: 

    elif app.ableToCaptureCat == True:
        if event.key == "Return" or event.key == "Enter" :
            app.mode = "catalogMode"  
        
    
# helper to help Move player 
def movePlayer(app, drow, dcol):
    drow = drow * 25
    dcol = dcol * 25
    app.player.x += drow
    app.player.y += dcol
 
    if not inBounds(app):
        app.player.x -= drow
        app.player.y -= dcol  
     
    else:
        return True
        

def inBounds(app): 
    #If the player is in the bounds
    if (app.player.x >= 10 and app.player.x <= 590 and app.player.y >= 10 and app.player.y <=590):
        return True
    else:
        return False
 

