import random

class Player:

    def __init__(self):
        self.shipGrid = [["~","~","~","~","~","~","~","~","~","~"],
                          ["~","~","~","~","~","~","~","~","~","~"],
                          ["~","~","~","~","~","~","~","~","~","~"],
                          ["~","~","~","~","~","~","~","~","~","~"],
                          ["~","~","~","~","~","~","~","~","~","~"],
                          ["~","~","~","~","~","~","~","~","~","~"],
                          ["~","~","~","~","~","~","~","~","~","~"],
                          ["~","~","~","~","~","~","~","~","~","~"],
                          ["~","~","~","~","~","~","~","~","~","~"],
                          ["~","~","~","~","~","~","~","~","~","~"] ]
        self.guessGrid = [["~","~","~","~","~","~","~","~","~","~"],
                          ["~","~","~","~","~","~","~","~","~","~"],
                          ["~","~","~","~","~","~","~","~","~","~"],
                          ["~","~","~","~","~","~","~","~","~","~"],
                          ["~","~","~","~","~","~","~","~","~","~"],
                          ["~","~","~","~","~","~","~","~","~","~"],
                          ["~","~","~","~","~","~","~","~","~","~"],
                          ["~","~","~","~","~","~","~","~","~","~"],
                          ["~","~","~","~","~","~","~","~","~","~"],
                          ["~","~","~","~","~","~","~","~","~","~"] ]

    def printShipGrid(self):
        for r in self.shipGrid:
            for c in r:
                print(c, end=" ")
            print()

    def printGuessGrid(self):
        for r in self.guessGrid:
            for c in r:
                print(c, end=" ")
            print()

    def placeShips(self, ship):
        pass

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


    def checkLegalPlacement( self , row , col , horiz , ship ):
        if( horiz == "H"):
            if( col + self.spacesOfShip(ship) > 9 ):
                return False
            else:
                return True
        else:
            if (row + self.spacesOfShip(ship) > 9):
                return False
            else:
                return True



    def placeShipInGrid( self , row , col , horiz , ship):
        if (horiz == "H"):
            for c in range(col, col + self.spacesOfShip(ship)):
                self.shipGrid[row][c] = ship
        elif (horiz == "V"):
            for r in range(row, row + self.spacesOfShip(ship)):
                self.shipGrid[r][col] = ship







