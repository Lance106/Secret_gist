import matplotlib.pyplot as plt
import numpy as np
import sys

def updateChart(arr, count, xBoundary, yBoundary):
    
    xLabels = range(1, xBoundary + 1)
    yLabels = range(1, yBoundary + 1)

    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    plt.axis([0, xBoundary, 0, yBoundary])
    plt.pcolormesh(arr, edgecolors ='k', linewidths = 1)
    ax.set_yticks(np.arange(arr.shape[0]) + 0.5, minor=False)
    ax.set_xticks(np.arange(arr.shape[1]) + 0.5, minor=False)
    ax.set_xticklabels(xLabels[0:])
    ax.set_yticklabels(yLabels[0:])

    plt.show()

    return

def userInputRoute():
    
    route = input("Enter Route \n")
    userStopGame(route)
    
    leaveTrail = input("Leave Trail Yes or No \n")
    userStopGame(leaveTrail)
    
    return route, leaveTrail

def userInputBoundaries(xStart, yStart):
    print("\n")
    print("Starting X Co-ordinate = %s" %xStart)
    xBoundary = input("Enter X Boundary \n")
    userStopGame(xBoundary)
    xBoundary = int(xBoundary) # Cast to an int
    
    
    print("\n")
    print("Starting Y Co-ordinate = %s" %yStart)
    yBoundary = input("Enter Y Boundary \n")
    userStopGame(yBoundary)
    yBoundary = int(yBoundary)
    
    return xBoundary, yBoundary

def getStartingCoordinates(Lines):
    
    count = 0
    
    for line in Lines:
        if count == 0:
            xStart = int((line.strip()))
        elif count == 1:
            yStart = int((line.strip())) 
            break
        count = count + 1

    return xStart, yStart

def printArray(arr, X, Y):
    
    print(arr)
    print(X,Y)
    print("")
    
    return

def leaveTrailDecision(leaveTrail, arr, xBoundary, yBoundary):
    
    if leaveTrail == 'No':
        arr = np.zeros((xBoundary, yBoundary)) # refresh don't leave trail
    else:
        arr = arr
    
    return arr

def countNumberDirections(route):
    
    count = 0

    with route as fp:
        for count, line in enumerate(fp):
            pass
    return count # number of lines in file count + 1 - (2 starting co-ordinates)

def printCoordinates(direction, Y, X):
    
    if direction == "N":
        print("Going North")
    elif direction == "S":
        print("Going South")
    elif direction == "E":
        print("Going East")
    elif direction == "W":
        print("Going West")
        
    print(X, Y)
    
    return

def routeGame(Lines, xBoundary, yBoundary, arr, leaveTrail):
    
    count = 0 # Used to keep track of line open of file in for loop and to set the block colour
    
    ## This will get the co-ordinates of travel one at a time
    for line in Lines:
        
        if count == 0:
            X = int((line.strip()))
            if(X > xBoundary):
                sys.exit("Starting X Co-ordinate out of bounds") 
        elif count == 1:
            Y = int((line.strip()))
            if(Y > yBoundary):
                sys.exit("Starting Y Co-ordinate out of bounds") 
            arr[Y-1][X-1] = count
            updateChart(arr, count, xBoundary, yBoundary) # Updates the chart with the new 3D Array
        else:
            if line.strip() == 'N':
                Y = Y + 1
                printCoordinates("N", Y, X)
            elif line.strip() == 'S':
                Y = Y - 1
                printCoordinates("S", Y, X)
            elif line.strip() == 'E':
                X = X + 1
                printCoordinates("E", Y, X)
            elif line.strip() == 'W':
                X = X - 1
                printCoordinates("W", Y, X)
            else:
                print("Error in Direction")
                sys.exit("Invalid Direction")
            
            # arr[Y][X] is opposite for the graph display i.e. you would assume arr[X][Y]
            arr[Y-1][X-1] = count # Updates the value for the 2D Matrix array with count value for colour
            
            updateChart(arr, count, xBoundary, yBoundary) # Updates the chart with the new 3D Array

            if((Y == yBoundary) or (X == xBoundary) or (Y == 0) or ( X == 0)):
                arr[Y-1][X-1] = count # Updates the value for the 2D Matrix array with count value for colour
                sys.exit("Route Out of Bounds") 
        

            arr = leaveTrailDecision(leaveTrail, arr, xBoundary, yBoundary)
             
        count = count + 1
    
    return

def userInputRestart():
    
    game = input("Restart the Game? Yes/ No \n")  
    
    if game == "Yes":
        game = 1
    elif game == "No":
        game = 0
        print("User Stopped Game")
    userStopGame(game)
    
    return game

def userStopGame(stopMessage):
    
    if stopMessage == "Stop":
        sys.exit("User Stopped Game")
        
    return