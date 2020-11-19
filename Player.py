import random

class Player:

    def __init__(self):  # constructor
        # each player gets a grid to place their ships on (shipGrid)
        # each player gets a grid to guess on (guessGrid)
        # each player gets an int to keep track of their hit number (hitCount)
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
        self.hitCount = 0

    def printShipGrid(self): #prints where the player places the ship on the board
        for r in self.shipGrid:  # traverses grid to print
            for c in r:
                print(c, end=" ")
            print()

    def printGuessGrid(self): #prints where the player has guessed about where their opponent's ship is
        for r in self.guessGrid:  # traverses grid to print
            for c in r:
                print(c, end=" ")
            print()

    def getHitCount(self):
        return self.hitCount

    def placeShips(self, ship):
        # this just means the method doesn't do anything, its just a placeholder for the
        # subclasses to overwrite
        pass

    def spacesOfShip(self, ship):  # helper method to determine the number of spaces each ship occupies
        if (ship == "D" or ship == "Destroyer"):  # if ship is D
            return 2
        elif (ship == "C" or ship == "Cruiser"):  # if ship is C
            return 3
        elif (ship == "S" or ship == "Submarine"):  # if ship is S
            return 3
        elif (ship == "B" or ship == "Battleship"):  # if ship is B
            return 4
        elif (ship == "A" or ship == "Aircraft Carrier"):  # if ship is A
            return 5


    def checkLegalPlacement( self , row , col , horiz , ship ):  # checks if ship fits legally (fits, and spaces are empty)
        if( horiz == "H"):  # checks if ship fits in grid horizontally
            if( col + self.spacesOfShip(ship) > 9 ):  # if ship doesn't fit
                return False
            else:  # if ship fits
                for a in range(col, col + self.spacesOfShip(ship)):  # checks if there is a ship there already
                    if self.shipGrid[row][a] != "~":  # if there is already a ship placed
                        return False
                return True
        else:  # checks if ship fits in grid vertically
            if (row + self.spacesOfShip(ship) > 9):  # if ship doesn't fit
                return False
            else:  # if ship fits
                for a in range(row, row + self.spacesOfShip(ship)):  # checks if there is a ship there already
                    if self.shipGrid[a][col] != "~": # if there is already a ship placed
                        return False
                return True



    def placeShipInGrid( self , row , col , horiz , ship):  # this method will place the ships on the board
        if (horiz == "H"):  # if ship is horizontally positioned
            for c in range(col, col + self.spacesOfShip(ship)):
                self.shipGrid[row][c] = ship
        elif (horiz == "V"):  # if ship is vertically positioned
            for r in range(row, row + self.spacesOfShip(ship)):
                self.shipGrid[r][col] = ship

    def makeGuess(self):  # this method will return the coordinates of the player's guess
        # this just means the method doesn't do anything, its just a placeholder for the
        # subclasses to overwrite
        pass

    def legalGuess(self, row, col):  # helper method to confirm whether or not the guess is valid
        if (row < 0 or row > 9):  # if guess is out of bounds
            return False
        if (col < 0 or col > 9):  # if guess is out of bounds
            return False
        if self.guessGrid[row][col] == "x" or self.guessGrid[row][col] == "-":
        # if they have already guessed this space
            return False

    def takeShots(self, opponent, guess):  # method that actually takes shots at opponent's ships
        # oppBoard is opponent board, guessCoordinates is an array returned from makeGuess method
        row = guess[0]
        col = guess[1]
        if opponent.shipGrid[row][col] == "~":  # if they miss
            print("Miss")
            self.guessGrid[row][col] = "-"
            opponent.shipGrid[row][col] = "-"
        elif opponent.shipGrid[row][col] != "~":  # if they hit
            print("Hit!")
            letter = opponent.shipGrid[row][col]
            self.guessGrid[row][col] = "x"
            opponent.shipGrid[row][col] = "x"
            self.hitCount += 1
            if self.sunkShip(letter, opponent) == True:
                print("You sunk " + letter)


    def sunkShip(self, ship, opponent):
        for x in opponent.shipGrid:
            if x == ship:
                return False
        return True