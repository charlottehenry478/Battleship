from Player import Player

class HumanPlayer( Player ):



    def placeShips(self, ship):  # places ships
        spaces = self.spacesOfShip(ship)
        rCoor = 0
        cCoor = 0
        horiz = True
        loopRun = True
        while(loopRun):
            row = input("Enter the row coordinate where ship starts")
            col = input("Enter the col coordinate where ship starts")
            horiz = input("Is the ship horizontal? (True/False)")


            inGrid = self.checkLegalPlacement( row , col , horiz , spaces)
            if( inGrid == False ):
                continue
            self.placeShipInGrid( row , col , horiz , ship)





