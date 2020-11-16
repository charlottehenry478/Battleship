from Player import Player

class HumanPlayer( Player ):


    def placeShips(self, ship):  # places ships
        while(True):
            row = int(input("Enter the row coordinate where ship starts"))
            col = int(input("Enter the col coordinate where ship starts"))
            horiz = input("Horizontal or Vertical? (H/V)")
            if( row > 9 or row < 0 or col > 9 or col < 0): # if placement is out of bounds
                continue
            horiz = horiz.upper()
            if( horiz != "V" and horiz != "H"):  # if direction is invalid
                continue
            inGrid = self.checkLegalPlacement( row , col , horiz , ship)
            if( inGrid == False ):  # if placed invalidly
                continue
            self.placeShipInGrid( row , col , horiz , ship)
            break

    def makeGuess(self) :#generates a guess from user input about where the Computer Player's ship will be
        while(True):
            guessRow = str(input("Please enter your guess for the row"))
            guessCol = str(input("Please enter your guess for the column"))
            if self.legalGuess(guessRow, guessCol) == False:  # if guess is invalid
                continue
        return [guessRow, guessCol]




