#Get cell row and col
def getRow(app, y):
    return int((y - app.margin) / app.cellSize) 

def getCol(app, x):
    return int((x - app.margin) / app.cellSize)
    
# Check distance to object (button) user is trying to press
def distance(x0, y0, x1, y1):
    x = (x0-x1)**2
    y = (y0-y1)**2
    return ((x + y)**0.5)
 