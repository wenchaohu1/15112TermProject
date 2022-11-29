from cmu_112_graphics import * 
import random 
 
#Maze Generators

#https://en.wikipedia.org/wiki/Maze_generation_algorithm
    #got idea for DFS, Prims, Kruskal's

class Maze:  
    #Initialize 
    def __init__(self, rows, cols):
        #Initialize rows and cols
        self.rows = rows
        self.cols = cols

        #Set the dimensions of the board
        #Idea from https://www.cs.cmu.edu/~112/notes/notes-animations-part2.html
        self.margin = 50
        self.cellSize = 50 

        #GridHeight/Gridwidth = number ofrows/cols * cellSize
        self.gridWidth = self.cols * self.cellSize
        self.gridHeight = self.rows * self.cellSize
     
        #Initialize the list of nodes by appending to the empty list 
        self.nodes = []
        for index in range(cols):
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
    
    # Idea from Wikipedia are in numbered comments
    # https://en.wikipedia.org/wiki/Maze_generation_algorithm#Randomized_Prim's_algorithm
    def prims(self): 
        startingPoint = (0,0) #default start @ (0,0)

        #1. Start with a grid full of walls
        walls = self.getWalls(startingPoint)

        #Create Nodes for all the locations
        self.createNodes() 

        #Create a set of all the visited locations
        visitedNodes = set() 

        #2. Pick a cell, mark it as part of the maze. Add the walls of the cell to the wall list.
        #Add the starting point to visitedNodes
        visitedNodes.add(startingPoint) 

        #3. While there are walls in the list: 
        while walls != []:
            #1. Pick a random wall from the list
            wall = random.choice(walls)

            ## wall[0] is the starting point, which is already accounted for
            nextPossEdge = wall[1]

            #if the next possible edge is already in visited, then pass
            if nextPossEdge in visitedNodes: 
                pass

            #else,add the wall as nodes
            else:
                currWall = wall[0][0]
                nextWall = wall[0][1]
                self.nodes[currWall][nextWall].mutualAddNeighbors(self.nodes[wall[1][0]][wall[1][1]])
                
                #Add to the set of visited nodes
                visitedNodes.add(nextPossEdge) 
                walls = walls + self.getWalls(nextPossEdge)
                # print(self.getWalls(nextPossEdge))
            
            #2. Remove the wall from the list.
            #Backtrack, if there are no walls, remove the wall 
            walls.remove(wall)

    #return with possible corrdinate points that may connects startingLocation to nextlocation
    def getWalls(self, location):

        #possible directions (up,down,left,right)
        dir  = [(-1, 0), (1, 0), (0, 1), (0, -1)]  

        #initialize row and col
        row = location[0]
        col = location[1]
        
        #Initialize empty list of results
        result = []
        
        #If the new points of new move are valid, 
        for drow, dcol in dir:
            if self.isInGrid(drow+row, dcol+col):
                # append to list of edges (result)
                result.append(((row, col), (drow+row, dcol+col)))

        # print(result)
        return result
  
    #Kruskal's algorithm: Note that simply running classical Prim's on a graph with random edge weights would create mazes stylistically identical to Kruskal's, because they are both minimal spanning tree algorithms. Instead, this algorithm introduces stylistic variation because the edges closer to the starting point have a lower effective weight.
    def kruskal(self):
        pass
    #1. Create a list of all walls, and create a set for each cell, each containing just that one cell.
    #2. For each wall, in some random order:
        #1. If the cells divided by this wall belong to distinct sets:
            #1. Remove the current wall.
            #2. Join the sets of the formerly divided cells.
    #Method that returns all Unvisited neighbors as a list  

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
                #draw the node at the specific cell
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
 
 