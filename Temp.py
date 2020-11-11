def makeMoves(self):
    coorX = 0
    coorY = 0
    if (self.type == "human"):
        coorX = input("Enter the x coordinate you want to attack")
        coorY = input("Enter the y coordinate you want to attack")
    else:
        coorX = random.randint(0, 9)
        coorY = random.randint(0, 9)
        break

    if (inGrid | spaceEmpty == False):
        print("Error, ship does not fit")
        continue
    else:
        loopRun = False
        if (horiz == True):
            for x in range(0, spaces):
                self.placeArr[xCoor + x] = ship
        elif (horiz == False):
            for x in range(0, spaces):
                self.placeArr[yCoor + x] = ship


def makeMoves(self):
    coorX = 0
    coorY = 0
    if (self.type == "human"):
        coorX = input("Enter the x coordinate you want to attack")
        coorY = input("Enter the y coordinate you want to attack")
    else:
        coorX = random.randint(0, 9)
        coorY = random.rantint(0, 9)
    self.guessArr[coorX][coorY] =


def hitOrNot(self, x, y):