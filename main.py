import numpy as np
from utils import userInputRestart, routeGame, userInputRoute, userInputBoundaries, getStartingCoordinates
import sys

game = 1 # Used to determine to carry on game or not

while(game):
    route, leaveTrail = userInputRoute() # Call this function to gather dat from the user
    route = open(route + '.txt', 'r') # Open file as read only 'r'
    Lines = route.readlines()

    xStart, yStart = getStartingCoordinates(Lines)
    xBoundary, yBoundary = userInputBoundaries(xStart, yStart)

    arr = np.zeros((yBoundary, xBoundary), dtype=int) # Make a new Array of zeros
    
    routeGame(Lines, xBoundary, yBoundary, arr, leaveTrail)
    game = userInputRestart()

sys.exit("Route Game Complete")
