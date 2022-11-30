from cmu_112_graphics import * 
import random 
 
#Maze Generators

#https://en.wikipedia.org/wiki/Maze_generation_algorithm
    #got idea for DFS, Prims, Kruskal's

class Maze:   
    def __init__(self, rows, cols):
        #Initialize rows and cols
        self.rows = rows
        self.cols = cols

        #Set the dimensions of the board
        #Idea from https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
        self.margin = 50
        self.cellSize = 50  
        self.gridWidth = self.cols * self.cellSize
        self.gridHeight = self.rows * self.cellSize
     
        #Initialize the list of nodes by appending to the empty list 
        self.nodes = []
        for i in range(cols):
            #For each column, multiply by length of row
            temp = [0]*rows  
            #Append the new row list of nodes
            self.nodes.append(temp) 

        #Initialize how wide the path is
        self.pathWidth = 10 
      
    #Method to create the nodes from cell
    def createNodes(self):
        #Iterate through every grid position and add it as a node
        for i in range(self.rows):
            for j in range(self.cols):  
                self.nodes[i][j] = Node((i, j)) 
    
    #Inspired from https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html 
    #Check if the next move is within the defined grid dimensions
    def isInGrid(self, row, col):
        if 0 <= row and row < self.rows: #Check rows
            if 0 <= col and col < self.cols: #Check cols
                return True
        return False

    #Depth-First Search
    def depthFirstSearch(self):
        #Create Nodes for all the locations
        self.createNodes() 
        #Create a set of all the visited locations
        visitedNodes = set() 
 
        #Recursively call helper function
        startingLocation = (0,0)
        self.depthFirstSearchHelper(startingLocation, visitedNodes) 

    def depthFirstSearchHelper(self, currentCell, visitedNodes):
        #For each cell, add to visited set
        visitedNodes.add(currentCell)

        #CurrentCell stores the coordinate points of cell location
        #Row, zeroth index. Col, first index. 
        row = currentCell[0]
        col = currentCell[1]

        #Get all the unvisited neighbors
        neighborNodes = self.getUnvisitedNeighbors(visitedNodes,row,col)

        #As long as there are unvisited neighbors, randomly select a neighbor to visit
        while neighborNodes != []:
            neighborNodes = random.choice(neighborNodes)

            #get the newRow and newCol from neighborNodes
            possNewRow = neighborNodes[0]
            possNewCol = neighborNodes[1] 

            #At the location, add the neighbors
            self.nodes[row][col].mutualAddNeighbors(self.nodes[possNewRow][possNewCol])

            #Recursivly call the Helper, pass in neighbor nodes and visited nodes
            self.depthFirstSearchHelper(neighborNodes, visitedNodes)

            #Backtracking: if the helper does not yield result,
            #              reset the neighbor nodes to original row and col
            neighborNodes = self.getUnvisitedNeighbors(visitedNodes,row, col) 
    
    def getUnvisitedNeighbors(self, visited, row, col):
        #initlize empty list
        result = []

        #possible directions (up,down,left,right)
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)] 

        #Check legality of the new points after applying the directions
        for drow, dcol in directions:
            #if the new point is in the grid (valid move)
            if self.isInGrid(drow+row, dcol+col):
                #Check if the new point has been visited
                #If has been visited, pass
                if (drow+row, dcol+col) in visited:
                    pass
                #Else, add new point to unvisited result
                else:
                    result.append((drow+row, dcol+col))
        return result  

    #from https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
    def getCellBounds(self, location):
        row, col = location 
        x = self.margin + (col+0.5) * self.cellSize
        y = self.margin + (row+0.5) * self.cellSize 
        return (x, y)
     
    def redrawAll(self, canvas):
        #For each cell
        for row in range(self.rows):
            for col in range(self.cols):  

                node = self.nodes[row][col] 

                #For all the neighbors in neighboring nodes
                for neighbor in node.getNeighbors():
                    #Use drawMaze method in Node to draw the maze
                    node.drawMaze(canvas, neighbor, self.pathWidth, self.getCellBounds) 

#Node class, stores all the nodes location and its neighbors
class Node():

    def __init__(self, location): 
        self.location = location 
        #Initialize empty set of neighbors
        self.neighbors = set()  

    #Method to get the neightbor nodes
    def getNeighbors(self):
        return self.neighbors

    #Method of add neighbors to "other"
    def mutualAddNeighbors(self, other):
        self.neighbors.add(other)
        other.neighbors.add(self)

    # Lotto helped me with this part
    def drawMaze(self, canvas, other, margin, convertToCoords): 

        xSelf, ySelf = convertToCoords(self.location)
        xOther, yOther = convertToCoords(other.location) 

        canvas.create_rectangle(xSelf-margin, ySelf-margin, 
                                  xOther+margin, yOther+margin, fill='black') 


# maze = Maze(10, 10)
# print(maze.depthFirstSearch())

# def redrawAll(app, canvas): 
#     maze.redrawAll(canvas)  

# runApp(width=600, height=600)  
