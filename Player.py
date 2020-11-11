class Player:

import random

    def __init__(self, t):  # constructor, type is human/computer and both grids
        self.type = t
        rows, cols = (10, 10)
        placeArr = [["~"] * cols] * rows
        guessArr = [["~"] * cols] * rows


    def spacesOfShip(self, ship):  # helper method to determine the number of spaces each ship occupies
        if (ship == "D" or ship == "Destroyer"):
            return 2
        elif (ship == "C" or ship == "Cruiser"):
            return 3
        elif (ship == "S" or ship == "Submarine"):
            return 3
        elif (ship == "B" or ship == "Battleship"):
            return 4
        elif (ship == "A" or ship == "Aircraft Carrier"):
            return 5


    def placeShips(self, ship):  # places ships
        spaces = self.spacesOfShip(ship)
        xCoor = 0
        yCoor = 0
        horiz = True
        loopRun = True
        while(loopRun):
            if (self.type == "human"):
                xCoor = input("Enter the x coordinate where ship starts")
                yCoor = input("Enter the y coordinate where ship starts")
                horiz = input("Is the ship horizontal? (True/False)")
            else:
                xCoor = random.randint(0,9)
                yCoor = random.randint(0,9)
                direction = random.randint(0,1)
                if (direction == 1):
                    horiz == False

            inGrid = False
            if (horiz == True & xCoor + spaces < 10):
                inGrid == True
            if (horiz == False & yCoor + spaces < 10):
                inGrid == False

            spaceEmpty = False
            if (horiz == True):
                for x in range(0, spaces):
                    if self.placeArr[[xCoor + x] != "~"]:
                        spaceEmpty = False
                        break

            if (horiz == True & xCoor + spaces < 10):
                inGrid == True

            if(inGrid | spaceEmpty == False ):
                print("Error, ship does not fit")
                continue

            else:
                loopRun = False
                if (horiz == True):
                    for x in range(0,spaces):
                        self.placeArr[xCoor + x] = ship
                elif (horiz == False):
                    for x in range(0,spaces):
                        self.placeArr[yCoor + x] = ship



    def makeMoves(self):
        coorX = 0
        coorY = 0
        if (self.type == "human"):
             coorX = input("Enter the x coordinate you want to attack")
             coorY = input("Enter the y coordinate you want to attack")
        else:
            coorX = random.randint(0,9)
            coorY =
            break

            if(inGrid | spaceEmpty == False ):
                print("Error, ship does not fit")
                continue
            else:
                loopRun = False
                if (horiz == True):
                    for x in range(0,spaces):
                        self.placeArr[xCoor + x] = ship
                elif (horiz == False):
                    for x in range(0,spaces):
                        self.placeArr[yCoor + x] = ship

    def makeMoves(self):
        coorX = 0
        coorY = 0
        if (self.type == "human"):
             coorX = input("Enter the x coordinate you want to attack")
             coorY = input("Enter the y coordinate you want to attack")
        else:
            coorX = random.randint(0,9)
            coorY = random.rantint(0,9)
        self.guessArr[coorX][coorY] =

    def hitOrNot(self, x, y):