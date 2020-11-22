from HumanPlayer import HumanPlayer
from ComputerPlayer import ComputerPlayer

print("Welcome to Battleship!")

human = HumanPlayer()
computer = ComputerPlayer()

print("Player one place ships now:")
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

print("Player two place ships now.")
computer.placeShips("D")
computer.placeShips("S")
computer.placeShips("C")
computer.placeShips("B")
computer.placeShips("A")

while(True):  # after ships are placed, this loop runs the game until one player wins
    print("Player one make guess:")
    print("Your guess grid:")
    human.printGuessGrid()
    guess1 = human.makeGuess()
    human.takeShots(computer, guess1)
    print()

    print("Player two make guess.")
    guess2 = computer.makeGuess()
    computer.takeShots(human, guess2)
    print("Your ship grid:")
    human.printShipGrid()

    if(human.getHitCount() == 17):  # if the human has sunk every ship
        break
    elif(computer.getHitCount() == 17):  # if the computer has sunk every ship
        break

if(human.getHitCount() >= 17):  # if the human won
    print("Congratulations, player one won!")
else:  # if the computer won
    print("Player two won. Better luck next time!")