from Player import Player

import random

class ComputerPlayer( Player ):


    def placeShips(self, ship):  # places ships
        while (True):  # generates random guess
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            direction = random.randint(0, 1)
            horiz = "V"
            if (direction == 1):  # changes direction
                horiz = "H"

            inGrid = self.checkLegalPlacement(row, col, horiz, ship)
            if (inGrid == False):  # if placement is invalid
                continue
            self.placeShipInGrid(row, col, horiz, ship)
            break

    def makeGuess(self):  # this will generate a random guess by the Computer Player
        while(True):  # generates random guess
            guessRow = random.randint(0, 9)
            guessCol = random.randint(0, 9)
            if self.legalGuess(guessRow, guessCol) == False:  # if guess is invalid
                continue
            else:  # if guess is valid
                break
        return [guessRow, guessCol]
