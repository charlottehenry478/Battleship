class Player:

    def __init__(self, t):
        self.type = t

    def spacesOfShip(self, ship):  # helper method to determine the number of spaces each ship occupies
        if (ship == "D" | ship == "Destroyer"):
            return 2
        elif (ship == "C" | ship == "Cruiser"):
            return 3
        elif (ship == "S" | ship == "Submarine"):
            return 3
        elif (ship == "B" | ship == "Battleship"):
            return 4
        elif (ship == "A" | ship == "Aircraft Carrier"):
            return 5

    def placeShips(self, ship):  # places ships
        spaces = self.spacesOfShip(ship)
        xCoor = 0
        yCoor = 0
        bool = True
        while(bool):
            if (self.type == "human"):
                # user input
            else:
                # generate random numbers within grid

            if(#ship does not fit):
                print("Error, ship does not fit")
            else:
                bool = False
        # place ships here 


    def makeMoves(self):


