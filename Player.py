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
        hitCount = 0

    def printShipGrid(self): #prints where the player places the ship on the board
        for r in self.shipGrid:
            for c in r:
                print(c, end=" ")
            print()

    def printGuessGrid(self): #prints where the player has guessed about where their opponent's ship is
        for r in self.guessGrid:
            for c in r:
                print(c, end=" ")
            print()

    def placeShips(self, ship):
        pass    #this just means the method doesn't do anything, its just a placeholder for the
                #subclasses to overwrite

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


    def checkLegalPlacement( self , row , col , horiz , ship ):  # checks if ship fits legally (fits, and spaces are empty)
        if( horiz == "H"):  # checks if ship fits in grid horizontally
            if( col + self.spacesOfShip(ship) > 9 ):
                return False
            else:
                for a in range(col, self.spacesOfShip(ship)):
                    if self.shipGrid[a, col] != "~":
                        return False
                return True
        else:  # checks if ship fits in grid vertically
            if (row + self.spacesOfShip(ship) > 9):
                return False
            else:
                for a in range(row, self.spacesOfShip(ship)):
                    if self.shipGrid[a, col] != "~":
                        return False
                return True



    def placeShipInGrid( self , row , col , horiz , ship):#this method will place the ships on the board
        if (horiz == "H"):
            for c in range(col, col + self.spacesOfShip(ship)):
                self.shipGrid[row][c] = ship
        elif (horiz == "V"):
            for r in range(row, row + self.spacesOfShip(ship)):
                self.shipGrid[r][col] = ship

    def makeGuess(self):#this method is overwritten in the ComputerPlayer and HumanPlayer classes
        pass

    def legalGuess(self, row, col):#confirms whether or not the guess is valid
        if self.guessGrid[row, col] == "x":
            return False

    def takeShots(self, oppBoard, guessCoordinates):  # oppBoard is opponent board, guessCoordinates is an array returned from makeGuess method
        row = guessCoordinates[0]
        col = guessCoordinates[1]
        if oppBoard[row, col] == "~":
            print("Miss")
            self.guessGrid[row, col] = "x"
        elif oppBoard[row, col] != "~":
            print("Hit!")
            self.hitCount += 1







