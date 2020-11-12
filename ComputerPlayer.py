from Player import Player

import random

class ComputerPlayer( Player ):


    def placeShips(self, ship):  # places ships
        while (True):
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            direction = random.randint(0, 1)
            horiz = "V"
            if (direction == 1):
                horiz = "H"

            inGrid = self.checkLegalPlacement(row, col, horiz, ship)
            if (inGrid == False):
                continue
            self.placeShipInGrid(row, col, horiz, ship)
            break