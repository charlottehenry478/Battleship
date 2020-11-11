import random

class Player:

    def __init__(self):
        rows, cols = (10, 10)
        self.placeArr = [["~"] * cols] * rows
        self.guessArr = [["~"] * cols] * rows

    def printShipGrid(self):
        for r in self.placeArr:
            for c in r:
                print(c, end=" ")
            print()

    def printGuessGrid(self):
        for r in self.guessArr:
            for c in r:
                print(c, end=" ")
            print()

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

# I need to finish this method
    def checkLegalPlacement( self , row , col , horiz , spaces ):
        return True

    #I am not sure this works yet
    def placeShipInGrid( self , row , col , horiz , ship):
        if (horiz == True):
            for c in range(0, self.spacesOfShip(ship)):
                self.placeArr[col + c] = ship
        elif (horiz == False):
            for r in range(0, self.spacesOfShip(ship)):
                self.placeArr[row + r] = ship



    def placeShips(self, ship):  # places ships
        spaces = self.spacesOfShip(ship)
    #code you wrote focusing on computer player
        xCoor = random.randint(0, 9)
        yCoor = random.randint(0, 9)
        direction = random.randint(0, 1)
        horiz = True
        if (direction == 1):
            horiz = False


