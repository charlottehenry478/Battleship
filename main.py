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
human.printShipGrid()
print("Place submarine")
human.placeShips("S")
human.printShipGrid()
print("Place cruiser")
human.placeShips("C")
human.printShipGrid()
print("Place battleship")
human.placeShips("B")
human.printShipGrid()
print("Place aircraft carrier")
human.placeShips("A")
human.printShipGrid()

print("Player two place ships now:")
computer.placeShips("D")
computer.placeShips("S")
computer.placeShips("C")
computer.placeShips("B")
computer.placeShips("A")

humanHits = human.getHitCount()
computerHits = computer.getHitCount()

while(humanHits < 17 and computerHits < 17):
    print("Player one make guess:")
    human.makeGuess()
    human.printGuessGrid()
    human.printShipGrid()
    humanHits = human.getHitCount()

    print("Player two make guess:")
    computer.makeGuess()
    computerHits = computer.getHitCount()

if(humanHits >= 17):
    print("Congratulations, player one won!")
else:
    print("Player two won. Better luck next time!")