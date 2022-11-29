from cmu_112_graphics import * 
from classes import * 
from mazeScreen import * 

def homeMode_redrawAll(app, canvas):
    font = 'Monospace 30 bold' 

    canvas.create_image(app.width/2, app.height/2, image=app.homeImg)
    canvas.create_text(app.width/2, 100, text=f'Welcome to Find the Cats, {app.username}!',
                       font=font, fill='black') 

# When you press the play button, take you to gameMode
# When you press cat-alog button, take you to catalogMode
def homeMode_mousePressed(app, event):
    x = event.x
    y = event.y
   
    if (x > 185 and x < 420 and y < 240 and y > 170):
        app.mode = 'gameMode'
 
    elif (x > 185 and x < 420 and y < 325 and y > 255):
        app.mode = 'catalogMode'
 