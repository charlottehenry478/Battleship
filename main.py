from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer

print("Welcome to Battleship!")

print("Player one place ships now:")
human = HumanPlayer()
computer = ComputerPlayer()

human.printGuessGrid()
human.printShipGrid()
print("Place destroyer")
human.placeShips("D")
print("Place submarine")
human.placeShips("S")
print("Place cruiser")
human.placeShips("C")
print("Place battleship")
human.placeShips("B")
print("Place aircraft carrier")
human.placeShips("A")
human.printShipGrid()

print("Player two place ships now:")
computer.printGuessGrid()
computer.printShipGrid()
computer.placeShips("D")
computer.placeShips("S")
computer.placeShips("C")
computer.placeShips("B")
computer.placeShips("A")
computer.printShipGrid()

humanHits = human.hitCount()
computerHits = computer.hitCount()

while(humanHits < 17 and computerHits < 17):
    print("Player one make guess:")
    human.makeGuess()
    human.printGuessGrid()
    human.printShipGrid()

    print("Player two make guess:")
    computer.makeGuess()
    computer.printGuessGrid()
    computer.printShipGrid()

if(humanHits >= 17):
    print("Congratulations, player one won!")
else:
    print("Player two won. Better luck next time!")